# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Agent(models.Model):
    _name = 'agent.fiche'
    _description = 'fiche agent'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'nom'

    user_id = fields.Many2one('res.users',
                              ondelete='set null', string="User", index=True)
    nom = fields.Char(string="Nom", required=True)
    prenom = fields.Char(string="Prenom", required=True)
    adresse = fields.Char(string="Adresse", required=True)
    naissance = fields.Date(string="Date de naissance", required=True)
    num_cin_num_passeport = fields.Integer(string=" N°cin / N°passeport", required=True)
    matricule = fields.Char(string="Matricule", required=True)
    email = fields.Char(string="Email", required=True, track_visibility="always")
    telephone = fields.Integer(string="Téléphone")
    role = fields.Selection([("administrateur", "Administrateur"), ("responsable agences", "Responsable agences"),
                             ("chef agence", "Chef agence"), ("agent", "Agent")], required=True, track_visibility="always")
    # agence = fields.Selection([("Topnet Agence centre urbain nord", "Topnet Agence centre urbain nord"),
    #                            ("Topnet Agence Tunis", "Topnet Agence Tunis"),
    #                            ("Topnet Agence Bardo", "Topnet Agence Bardo"),
    #                            ("Topnet Agence Ennasr", "Topnet Agence Ennasr"),
    #                            ("Topnet Agence La Marsa", "Topnet Agence La Marsa"),
    #                            ("Topnet Agence Le Passage", "Topnet Agence Le Passage"),
    #                            ("Topnet Agence Bizerte", "Topnet Agence Bizerte"),
    #                            ("Topnet Agence Nabeul", "Topnet Agence Nabeul"),
    #                            ("Topnet Agence Khzema", "Topnet Agence Khzema"),
    #                            ("Topnet Agence Sousse", "Topnet Agence Sousse"),
    #                            ("Topnet Agence Monastir", "Topnet Agence Monastir"),
    #                            ("Topnet Agence Sfax", "Topnet Agence Sfax"),
    #                            ("Topnet Agence Taib Mhiri Sfax", "Topnet Agence Taib Mhiri Sfax"),
    #                            ("Topnet Agence El Mourouj", "Topnet Agence El Mourouj"),
    #                            ("Topnet Agence Gabes", "Topnet Agence Gabes")])
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
            # other required field
        }
        user_id = self.env['res.users'].sudo().create(vals_user)
        values.update(user_id=user_id.id)
        res = super(Agent, self).create(values)

        return res
