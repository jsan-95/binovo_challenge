# -*- coding: utf-8 -*-

from odoo import models, fields


class Blog(models.Model):
    _inherit = 'blog.blog'

    company_id = fields.Many2one('res.company', string='Company',
                                 default=lambda self: self.env.user.company_id)


class BlogPost(models.Model):
    _inherit = 'blog.post'

    company_id = fields.Many2one('res.company', 'Company', store=True,
                                 readonly=True, related='blog_id.company_id')
