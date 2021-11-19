# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import re


class Abonnements (models.Model):
    _name = 'abonnement'
    _description = 'demande abonnement  '
    _inherit = ['mail.thread', 'mail.activity.mixin']
    # _rec_name = 'name'

    def action_valider(self):
        for rec in self:
            rec.state = 'valider'

    def action_non_valider(self):
        for rec in self:
            rec.state = 'non_valider'

    @api.depends('state')
    def action_depot(self):
         for rec in self:
            if rec.state == 'valider':
               return {
                  'name': _('Déposer'),
                  'domain': [],
                  'view_type': 'form',
                  'res_model': 'topnet.dossier',
                  'view_id': False,
                  'view_mode': 'tree,form',
                  'type': 'ir.actions.act_window',
                  }
            for rec in self:
                rec.state = 'dossier'



    state = fields.Selection([
        ('nouveau', 'Nouveau'),
        ('valider', 'Valide'),
        ('non_valider', 'Non valide'),
        ('dossier', 'Dépot Dossier'),

    ], string='Status', readonly=True, default='nouveau')

    id_contrat = fields.Char(string='Numéro contrat', required=True, copy=False, readonly=True,
                             index=True, default=lambda self: _('New'))

    client_id = fields.Many2one('res.users', ondelete='set null', string="User", index=True)

    installation = fields.Char(string="Adresse d'installation", required=True)
    ville2 = fields.Char(string="Ville" ,required=True)
    postale2 = fields.Integer(string="Code postale", required=True)
    tel2 = fields.Integer(string="Tél")
    fax2 = fields.Integer(string="Fax")

    type_offre = fields.Selection(
        [('Fibre Optique', 'Fibre Optique'), ('Voip Access', 'Voip Access'), ('Rapido Pro', 'Rapido Pro')],
        default="Fibre Optique", required=True)
    debit = fields.Selection([("20", "20"), ("30", "30"), ("50", "50"), ("100", "100")], default="20", required=True)
    active = fields.Boolean(string="Active", default="True")

    #
    # dossier_id = fields.Many2one('topnet.dossier', string='Related Dossier')
    # related_dossier_id = fields.Many2one('topnet.dossier', string='Dossier')




    @api.constrains('tel2', 'fax2')
    def check_name(self):
        for rec in self:

            if len(str(self.tel2)) != 8:
                raise ValidationError(_('Numéro de tel doit contenir seulement 8 chiffres'))
            elif len(str(self.fax2)) != 8:
                raise ValidationError(_('Nméro de fax doit contenir seulement 8 chiffres'))


    # @api.model
    # def create(self, values):
    #     vals_user = {
    #         'name': values.get('name'),
    #         'login': values.get('email_pri'),
    #         # 'password': values.get('mot_passe'),
    #         # other required field
    #     }
    #     client_id = self.env['res.users'].sudo().create(vals_user)
    #     values.update(client_id=client_id.id)
    #     res = super(Clients, self).create(values)
    #
    #     return res
