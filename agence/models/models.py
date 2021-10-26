# -*- coding: utf-8 -*-

from odoo import models, fields, api


class agence(models.Model):
    _name = 'agence.agence'
    _description = 'agence.agence'
    _rec_name='Nom'


    Nom = fields.Char(string ="Nom",required=True)
    Adresse = fields.Char(string="Adresse", required=True)
    Ville = fields.Char(string="Ville", required=True)
    Fax = fields.Char(string="Fax")




#
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100






