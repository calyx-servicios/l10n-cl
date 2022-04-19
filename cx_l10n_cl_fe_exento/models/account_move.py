from odoo import models


class AccountMove(models.Model):
    _inherit = "account.move"

    def exento(self):
        exento = sum(
            [
                l.price_subtotal
                for l in self.mapped("invoice_line_ids")
                if l.tax_ids.amount == 0
            ]
        )
        return exento if exento else (exento * -1)
