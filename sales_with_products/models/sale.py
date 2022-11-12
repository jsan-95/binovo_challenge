# -*- coding: utf-8 -*-

from odoo import _, api, models
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def action_confirm(self):
        for sale in self.order_line:
            if sale.product_uom_qty <= 0:
                raise UserError(
                        _('It is not allowed to confirm an order with '
                          'products quantity to zero'))

        return super(SaleOrder, self).action_confirm()

    @api.multi
    def clean_lines(self):
        self.ensure_one()
        for sale in self.order_line:
            if sale.product_uom_qty <= 0:
                sale.unlink()

