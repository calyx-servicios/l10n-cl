from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    # To Hide/show document_type_id field
    identification_type_is_rut = fields.Boolean(default=True)

    @api.onchange("l10n_latam_identification_type_id")
    def _compute_identification_type_is_rut(self):
        for record in self:
            if record.l10n_latam_identification_type_id == self.env.ref(
                "l10n_cl.it_RUT"
            ):
                record.identification_type_is_rut = True
            else:
                record.identification_type_is_rut = False

    ###

    @api.onchange("vat")
    def _onchange_vat_cl(self):
        """
        document_number holds the same data that vat has, so we make a copy of it.
        writes field vat to document_number.
        """
        if self.vat:
            if self.vat.upper().startswith("CL"):
                vat = self.vat[2:]
            else:
                vat = self.vat
        if self.vat and self.check_vat_cl(vat):
            self.document_number = self.vat

    def check_vat_cl(self, vat: str) -> bool:
        """
        The check_vat_cl method from the l10n_cl_fe module was not taking away the "-"
        sign before the validation so we do it here. Also remove commas to support
        another format of vat.
        """
        vat = vat.replace("-", "").replace(",", "")
        body, vdig = "", ""
        if len(vat) != 9:
            return False
        else:
            body, vdig = vat[:-1], vat[-1].upper()
        try:
            vali = list(range(2, 8)) + [2, 3]
            operar = "0123456789K0"[
                11
                - (
                    sum(
                        [int(digit) * factor for digit, factor in zip(body[::-1], vali)]
                    )
                    % 11
                )
            ]
            if operar == vdig:
                return True
            else:
                return False
        except IndexError:
            return False
