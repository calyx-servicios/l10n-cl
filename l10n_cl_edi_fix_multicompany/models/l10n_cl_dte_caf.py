from odoo import api, fields, models
from odoo.exceptions import UserError
from odoo.tools.translate import _


class L10nClDteCaf(models.Model):
    _inherit = 'l10n_cl.dte.caf'

    def action_enable(self):
        """
        This method gathers information from the caf file, analyze the tags and validate it, comparing the vat
        number of the company, with the vat present in the CAF.
        """
        result = self._decode_caf().xpath('//AUTORIZACION/CAF/DA')[0]
        self.start_nb = int(result.xpath('RNG/D')[0].text)
        self.final_nb = int(result.xpath('RNG/H')[0].text)
        l10n_latam_document_type_code = result.xpath('TD')[0].text
        self.l10n_latam_document_type_id = self.env['l10n_latam.document.type'].search(
            [('code', '=', l10n_latam_document_type_code),('country_id','=',self.company_id.country_id.id)])
        self.issued_date = result.xpath('FA')[0].text
        rut_n = result.xpath('RE')[0].text
        if not self.company_id.vat:
            raise UserError(_('The VAT of your company has not been configured. '
                              'Please go to your company data and add it.'))
        if not self.sequence_id:
            raise UserError(_('You should select a DTE sequence before enabling this CAF record'))
        if self._l10n_cl_format_vat(rut_n) != self._l10n_cl_format_vat(
                self.company_id.vat):
            raise UserError(_('Company vat %s should be the same that assigned company\'s vat: %s!') % (
                rut_n, self.company_id.vat))
        if self.l10n_latam_document_type_id != self.sequence_id.l10n_latam_document_type_id:
            raise UserError(_('SII Document Type for this CAF is %s and selected sequence associated document type '
                              'is %s. This values should be equal for DTE Invoicing to work properly!') % (
                l10n_latam_document_type_code, self.sequence_id.l10n_latam_document_type_id.code))
        # this value updates to the caf being used, but dont take into account that could be another caf as in use
        self.sequence_id.number_next_actual = self.start_nb
        self.status = 'in_use'
