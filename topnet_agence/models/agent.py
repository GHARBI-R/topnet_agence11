# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Agent(models.Model):
    _name = 'agent.fiche'
    _description = 'fiche agent'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'nom'

    user_id = fields.Many2one('res.users', ondelete='set null', string="User", index=True)
    agent_id = fields.Many2one('agent.fiche', ondelete='set null', string="agent", index=True)
    nom = fields.Char(string="Nom", required=True)
    prenom = fields.Char(string="Prenom", required=True)
    adresse = fields.Char(string="Adresse", required=True)
    naissance = fields.Date(string="Date de naissance", required=True)
    num_cin_num_passeport = fields.Integer(string=" N°cin / N°passeport", required=True)
    matricule = fields.Char(string="Matricule", required=True)
    email = fields.Char(string="Email", required=True, track_visibility="always")
    mot_passe = fields.Char(string="Mot de passe", required=True)
    c_mot_passe = fields.Char(string="Confirmation Mot de passe", required=True)
    telephone = fields.Integer(string="Téléphone")
    role = fields.Selection([("administrateur", "Administrateur"), ("responsable agences", "Responsable agences"),
                             ("chef agence", "Chef agence"), ("agent", "Agent")], required=True, track_visibility="always")

    Nom_agence = fields.Many2one('topnet_agence.agence', string='Agence')
    agence_deleg = fields.Selection('Delegation', related='Nom_agence.Delegation')
    agence_Adresse = fields.Char('Adresse', related='Nom_agence.Adresse')
    agence_Fax = fields.Integer('Fax', related='Nom_agence.Fax')
    active = fields.Boolean("Active", default=True)
    image = fields.Binary(string="Image", attachment=True)
    state = fields.Selection([
        ('disponible', 'Disponible'),
        ('abscent', 'Abscent'),
    ], string='Status', readonly=True, default='disponible')

    @api.model
    def create(self, values):
        vals_user = {
            'name': values.get('nom'),
            'login': values.get('email'),
            'password': values.get('mot_passe'),
            # other required field
        }
        user_id = self.env['res.users'].sudo().create(vals_user)
        values.update(user_id=user_id.id)
        res = super(Agent, self).create(values)

        return res
