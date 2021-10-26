# -*- coding: utf-8 -*-

from odoo import models, fields, api


class depot(models.Model):
    _name = 'depot.depot'
    _description = 'depot.depot'

    doc = fields.Binary(string="Registre de commerce", required=True)
    doc2 = fields.Binary(string="CIN gérant", required=True)
    doc3 = fields.Binary(string="Contrat TOPNET", required=True)
    doc4 = fields.Binary(string="Contrat TT", required=True)

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
