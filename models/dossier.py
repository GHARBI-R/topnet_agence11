# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class Topnet_dossier(models.Model):
    _name = 'topnet.dossier'
    _description = 'dossier topnet '
    _inherit = ['mail.thread', 'mail.activity.mixin']



    email_pri = fields.Many2one('client.fiche', string='email du gérant')
    # id_contrat_related = fields.Char('Numero de contrat', related='email_pri.id_contrat')
    dossier_id = fields.Many2one('topnet.dossier', ondelete='set null', string="dossier", index=True)


    doc1 = fields.Image(string="Registre de commerce", max_width=90, max_height=90, verify_resolution=True, required=True)
    doc2 = fields.Image(string="CIN gérant", max_width=90, max_height=90, verify_resolution=True, required=True)
    contrat_tt = fields.Binary (string= 'telecharger contrat TT')
    doc3 = fields.Image(string="Contrat TOPNET", max_width=90, max_height=90, verify_resolution=True, required=True)
    doc4 = fields.Image(string="Contrat TT", max_width=90, max_height=90, verify_resolution=True, required=True)

