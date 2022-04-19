from odoo import models


class AccountMove(models.Model):
    _inherit = "account.move"

    def exento(self):
        exento = 0
        for l in self.mapped("invoice_line_ids"):
            for _ in l.mapped("tax_ids").filtered(lambda t: t.amount == 0):
                exento += l.price_subtotal
                break
        return exento if exento > 0 else (exento * -1)
