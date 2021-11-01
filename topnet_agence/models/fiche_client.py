# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import ValidationError
import re


class Clients(models.Model):
    _name = 'client.fiche'
    _description = 'fiche clients '
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'

    _sql_constraints = [
        ('cin_pass_uniq', 'unique(email)', 'Numero de cin/passeport existe déja'),
        ('email_admi_uniq', 'unique(email_admi)', 'Email existe déja'),
        ('email_tech_uniq', 'unique(email_tech)', 'Email existe déja'),
        ('email_pri_uniq', 'unique(email_pri)', 'Email existe déja'),
    ]


    id_contrat = fields.Char(string='Numéro contrat', required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))
    name = fields.Char(string="Nom et Prénom du gérant")
    cin_pass = fields.Integer(string="Numéro CIN/Passeport")
    raison = fields.Char(string="Raison sociale")
    registre = fields.Char(string="Registre de commerce")
    tva = fields.Integer(string="Code TVA")
    Exonéré = fields.Selection([("oui", "Oui"), ("non", "Non")])
    douane = fields.Integer(string="Code en douane")
    activity = fields.Char(string="Activité de l'entreprise")
    correspondance = fields.Char(string="Adresse de correspondance")
    Ville = fields.Char(string="Ville")
    postale = fields.Integer(string="Code postale")
    tel = fields.Char(string="Tél")
    fax = fields.Char(string="Fax")
    installation = fields.Char(string="Adresse d'installation")
    ville2 = fields.Char(string="Ville")
    postale2 = fields.Integer(string="Code postale")
    tel2 = fields.Char(string="Tél")
    fax2 = fields.Char(string="Fax")
    #  Contact Administratif et Financiers

    nom = fields.Char(string="Nom et Prénom")
    Tel_admi = fields.Char(string="Tél")
    gsm_admi = fields.Char(string="GSM")
    email_admi = fields.Char(string="Email")

    #  Contact technique

    nom_tech = fields.Char(string="Nom et Prénom")
    tel_tech = fields.Char(string="Tél")
    gsm_tech = fields.Char(string="GSM")
    email_tech = fields.Char(string="Email")

    email_pri = fields.Char(string="Email principale")
    type_offre = fields.Selection ([('Fibre Optique','Fibre Optique'),('Voip Access','Voip Access'),('Rapido Pro','Rapido Pro')], default="Fibre Optique")
    debit = fields.Selection ([("20","20"),("30","30"),("50","50"),("100","100")], default="20")
    active = fields.Boolean(string="Active", default="Ture")
    state = fields.Selection([
        ('dossier', 'Dossier'),
        ('suivi', 'Suivi'),
    ], string='Status', readonly=True, default='dossier')

    @api.model
    def create(self, vals):
        if vals.get('id_contrat', _('New')) == _('New'):
            vals['id_contrat'] = self.env['ir.sequence'].next_by_code('topnet.client.sequence') or _('New')
        result = super(Clients, self).create(vals)
        return result

    # @api.constrains('name', 'cin_pass', 'tel', 'fax', 'tel2', 'fax2', 'tel_admi', 'gsm_admi', 'nom_tech', 'tel_tech', 'gsm_tech')
    # def check_name(self):
    #     for rec in self:
    #         if len(str(abs(self.tel))) != 8:
    #             raise ValidationError(_('Numéro de tel doit contenir seulement 8 chiffres'))
    #         elif len(str(abs(self.cin_pass))) != 8:
    #             raise ValidationError(_('Nméro de cin / passeport doit contenir seulement 8 chiffres'))
    #         elif len(str(abs(self.fax))) != 8:
    #             raise ValidationError(_('Nméro de fax doit contenir seulement 8 chiffres'))
    #         elif len(str(abs(self.tel2))) != 8:
    #             raise ValidationError(_('Numéro de tel doit contenir seulement 8 chiffres'))
    #         elif len(str(abs(self.fax2))) != 8:
    #             raise ValidationError(_('Nméro de fax doit contenir seulement 8 chiffres'))
    #         elif len(str(abs(self.tel_admi))) != 8:
    #             raise ValidationError(_('Nméro de tel doit contenir seulement 8 chiffres'))
    #         elif len(str(abs(self.gsm_admi))) != 8:
    #             raise ValidationError(_('Nméro de gsm doit contenir seulement 8 chiffres'))
    #         elif len(str(abs(self.tel_tech))) != 8:
    #             raise ValidationError(_('Nméro de tel doit contenir seulement 8 chiffres'))
    #         elif len(str(abs(self.gsm_tech))) != 8:
    #             raise ValidationError(_('Nméro de gsm doit contenir seulement 8 chiffres'))
    #         elif len(self.name) > 20:
    #             raise ValidationError(_('Nom trop long'))
    #         elif len(self.nom_tech) > 20:
    #             raise ValidationError(_('Nom trop long'))
    #
    # @api.constrains('email_admi', 'email_tech', 'email_pri')
    # def validate_email(self):
    #   for obj in self:
    #    if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$",obj.email) == None:
    #     raise ValidationError("Vérifier votre adresse mail : %s" % obj.email)
    #     return True


