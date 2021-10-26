# -*- coding: utf-8 -*-

from odoo import models, fields, api


class agence(models.Model):
    _name = 'agence.dossier'
    _description = 'agence.dossier'


    Nom = fields.Char(string ="Nom",required=True)
