# -*- coding: utf-8 -*-

from odoo.tests import tagged
from odoo.tests.common import TransactionCase


@tagged('post_install', '-at_install')
class TestBlogs(TransactionCase):

    def setUp(self):
        super(TestBlogs, self).setUp()
        self.company1 = self.env['res.company'].create({'name': 'Company 1'})
        self.company2 = self.env['res.company'].create({'name': 'Company 2'})

        self.blog = self.env['blog.blog'].create({
            'name': 'Blog 1',
            'subtitle': 'Blog 1',
            'company_id': self.company1.id,
        })

        self.post = self.env['blog.post'].create(
                {'blog_id': self.blog.id, 'name': 'Post 1'})

    def test_change_company(self):
        assert self.post.company_id == self.company1
        self.blog.company_id = self.company2.id
        assert self.post.company_id == self.company2
