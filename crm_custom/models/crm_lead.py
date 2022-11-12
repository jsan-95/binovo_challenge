# -*- coding: utf-8 -*-
from odoo import fields, models


class Lead(models.Model):
    _inherit = "crm.lead"

    source = fields.Selection([
        ('thirds', 'Thirds'), ('social', 'Social networks'),
        ('internet', 'Internet search')], string="Source")
