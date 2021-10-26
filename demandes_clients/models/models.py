# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError



class demandes_clients(models.Model):
    _name = 'demandes_clients.demandes_clients'
    _description = 'demandes_clients.demandes_clients'

    ID_contrat = fields.Integer(string="ID_contrat")
    name = fields.Char(string="Nom et Prénom du gérant", required=True)
    cin_pass = fields.Integer(string="Numéro CIN/Passeport", required=True)
    raison = fields.Char(string="Raison sociale", required=True)
    registre = fields.Char(string="Registre de commerce", required=True)
    tva = fields.Integer(string="Code TVA", required=True)
    Exonéré = fields.Selection([("oui", "Oui"), ("non", "Non")], required=True)
    douane = fields.Integer(string="Code en douane", required=True)
    activity = fields.Char(string="Activité de l'entreprise", required=True)
    correspondance = fields.Char(string="Adresse de correspondance", required=True)
    Ville = fields.Char(string="Ville", required=True)
    postale = fields.Integer(string="Code postale", required=True)
    tel = fields.Integer(string="Tél", required=True)
    fax = fields.Integer(string="Fax", required=True)
    installation = fields.Char(string="Adresse d'installation", required=True)
    ville2 = fields.Char(string="Ville", required=True)
    postale2 = fields.Integer(string="Code postale", required=True)
    tel2 = fields.Integer(string="Tél", required=True)
    fax2 = fields.Integer(string="Fax", required=True)
    #  Contact Administratif et Financiers

    nom = fields.Char(string="Nom et prénom", required=True)
    Tel_admi = fields.Integer(string="Tél", required=True)
    gsm_admi = fields.Integer(string="GSM", required=True)
    email_admi = fields.Char(string="E mail", required=True)

    #  Contact technique

    nom_tech = fields.Char(string="Nom et Prénom", required=True)
    tel_tech = fields.Integer(string="Tél", required=True)
    gsm_tech = fields.Integer(string="GSM", required=True)
    email_tech = fields.Char(string="E mail", required=True)

    email_pri = fields.Char(string="E mail principale", required=True)
    type_offre = fields.Char(string="Type de l'offre", required=True)
    debit = fields.Char(string="Débit", required=True)

@api.constrains('name', 'cin_pass', 'tel', 'fax', 'tel2', 'fax2', 'tel_admi', 'gsm_admi', 'nom_tech', 'tel_tech', 'gsm_tech')
def check_name(self):
    for rec in self:
        if len(str(abs(self.tel))) != 8:
            raise ValidationError(_('Numéro de tel doit contenir seulement 8 chiffres'))
        elif len(str(abs(self.cin_pass))) != 8:
                raise ValidationError(_('Nméro de cin / passeport doit contenir seulement 8 chiffres'))
        elif len(str(abs(self.fax))) != 8:
                raise ValidationError(_('Nméro de fax doit contenir seulement 8 chiffres'))
        elif len(str(abs(self.tel2))) != 8:
                raise ValidationError(_('Numéro de tel doit contenir seulement 8 chiffres'))
        elif len(str(abs(self.fax2))) != 8:
                raise ValidationError(_('Nméro de fax doit contenir seulement 8 chiffres'))
        elif len(str(abs(self.tel_admi))) != 8:
                raise ValidationError(_('Nméro de tel doit contenir seulement 8 chiffres'))
        elif len(str(abs(self.gsm_admi))) != 8:
                raise ValidationError(_('Nméro de gsm doit contenir seulement 8 chiffres'))
        elif len(str(abs(self.tel_tech))) != 8:
                raise ValidationError(_('Nméro de tel doit contenir seulement 8 chiffres'))
        elif len(str(abs(self.gsm_tech))) != 8:
                raise ValidationError(_('Nméro de gsm doit contenir seulement 8 chiffres'))
        elif len(self.name) > 20:
                raise ValidationError(_('Nom trop long'))
        elif len(self.nom_tech) > 20:
                raise ValidationError(_('Nom trop long'))


#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
