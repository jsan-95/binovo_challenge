# -*- coding: utf-8 -*-
from odoo.exceptions import UserError
from odoo.tests import tagged
from odoo.tests.common import TransactionCase


@tagged('post_install', '-at_install')
class TestSales(TransactionCase):

    def setUp(self):
        super(TestSales, self).setUp()
        self.product_1 = self.env.ref('product.product_product_1')
        self.product_2 = self.env.ref('product.product_product_2')
        self.partner_1 = self.env.ref('base.res_partner_1')

        self.sale = self.env['sale.order'].create({
            'partner_id': self.partner_1.id,
            'order_line': [(0, 0, {
                'product_id': self.product_1.id,
                'product_uom_qty': 0,
                'price_unit': 750.00,
            })],
        })

    def test_clean_lines(self):
        assert len(self.sale.order_line) == 1
        self.sale.clean_lines()
        assert len(self.sale.order_line) == 0

        self.sale.order_line = [(0, 0, {
            'product_id': self.product_1.id,
            'product_uom_qty': 0,
            'price_unit': 750.00,
        }), (0, 0, {
            'product_id': self.product_2.id,
            'product_uom_qty': 0,
            'price_unit': 750.00,
        })]

        assert len(self.sale.order_line) == 2
        self.sale.clean_lines()
        assert len(self.sale.order_line) == 0

        self.sale.order_line = [(0, 0, {
            'product_id': self.product_1.id,
            'product_uom_qty': 2,
            'price_unit': 750.00,
        }), (0, 0, {
            'product_id': self.product_2.id,
            'product_uom_qty': 4,
            'price_unit': 750.00,
        })]

        assert len(self.sale.order_line) == 2
        self.sale.clean_lines()
        assert len(self.sale.order_line) == 2

    def test_action_confirm(self):
        with self.assertRaises(UserError):
            self.sale.action_confirm()

        self.sale.order_line = [(0, 0, {
            'product_id': self.product_2.id,
            'product_uom_qty': 3,
            'price_unit': 750.00,
        })]

        with self.assertRaises(UserError):
            self.sale.action_confirm()

        self.sale.clean_lines()

        assert self.sale.action_confirm()
