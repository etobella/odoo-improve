# Copyright 2018 Creu Blanca
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class ResGroups(models.Model):
    _inherit = 'res.groups'

    trans_implied_ids = fields.Many2many(
        'res.groups', 
        store=True,
        relation='res_groups_trans_implied_rel',
        column1='gid',
        column2='hid',
    )
