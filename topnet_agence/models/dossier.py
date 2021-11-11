# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Topnet_dossier(models.Model):
    _name = 'topnet.dossier'
    _description = 'dossier topnet '
    _inherit = ['mail.thread', 'mail.activity.mixin']


    @api.model
    def create(self, values):
        vals_dossier = {
            'id_contrat': values.get('id_contrat'),

        }
        user_id = self.env['client.fiche'].sudo().create(vals_dossier)
        values.update(id_contrat=id_contrat.id)
        res = super(Topnet_dossier, self).create(values)

        return res

    id_contrat = fields.Char(string='Numéro contrat', readonly=True)
    dossier_id = fields.Many2one('topnet.dossier', ondelete='set null', string="agent", index=True)
    doc1 = fields.Image(string="Registre de commerce", max_width=90, max_height=90, verify_resolution=True, required=True)
    doc2 = fields.Image(string="CIN gérant", max_width=90, max_height=90, verify_resolution=True, required=True)
    doc3 = fields.Image(string="Contrat TOPNET", max_width=90, max_height=90, verify_resolution=True, required=True)
    doc4 = fields.Image(string="Contrat TT", max_width=90, max_height=90, verify_resolution=True, required=True)

    dossier_id = fields.Many2one('client.fiche', string='Dossier')



