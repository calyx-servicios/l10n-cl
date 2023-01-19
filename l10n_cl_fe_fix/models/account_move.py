from odoo import api, fields, models, tools
from odoo.exceptions import UserError

class AccountMove(models.Model):
    _inherit = "account.move"

    def send_exchange(self):
        commercial_partner_id = self.commercial_partner_id or self.partner_id.commercial_partner_id
        att = self._create_attachment()
        if commercial_partner_id.es_mipyme:
            return
        body = "XML de Intercambio DTE: %s" % (self.name)
        subject = "XML de Intercambio DTE: %s" % (self.name)
        dte_email_id = self.company_id.dte_email_id or self.env.user.company_id.dte_email_id
        dte_receptors = commercial_partner_id.child_ids + commercial_partner_id
        email_to = commercial_partner_id.dte_email + "," or ""
        for dte_email in dte_receptors:
            if not dte_email.send_dte or not dte_email.email:
                continue
            if dte_email.email in ["facturacionmipyme2@sii.cl", "facturacionmipyme@sii.cl"]:
                resp = self.env["sii.respuesta.cliente"].sudo().search([("exchange_id", "=", att.id)])
                #resp.estado = "0"
                #FIX
                resp.recep_envio = "0"
                continue
            if not dte_email.email in email_to:
                email_to += dte_email.email + ","
        if email_to == "":
            return
        values = {
            "res_id": self.id,
            "email_from": dte_email_id.name_get()[0][1],
            "email_to": email_to[:-1],
            "auto_delete": False,
            "model": "account.move",
            "body": body,
            "subject": subject,
            "attachment_ids": [[6, 0, att.ids]],
        }
        send_mail = self.env["mail.mail"].sudo().create(values)
        send_mail.send()
