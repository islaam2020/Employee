# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class ResEmployee(models.Model):
    _name = 'res.employee'
    _rec_name = 'name'

    name = fields.Char(string="Employee First Name", required=True, )
    name_last = fields.Char(string="Employee Last Name", required=True, )
    email = fields.Char(string="Email", required=False, )