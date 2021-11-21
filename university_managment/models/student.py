from odoo import models, fields,api,_

#
# class ResPartners(models.Model):
#     _inherit = 'res.partner'
#
#     @api.model
#     def create(self, vals_list):
#         res = super(ResPartners, self).create(vals_list)
#         print("yes working")
#         # do the custom coding here
#         return res


class UniversityStudent(models.Model):
    _name = 'university.student'
    _inherit = ['mail.thread','mail.activity.mixin',]
    _description = 'student inscription'
    _rec_name = 'f_name'



    reference = fields.Char(string='student reference', required=True, copy=False, readonly=True,
                            default=lambda self: _('New'))
    student_id = fields.Many2one('res.users', ondelete='set null', string="User", index=True)
    f_name = fields.Char(string='First Name', tracking = True)
    l_name = fields.Char(string='Last Name',tracking = True)
    identity_card = fields.Char(string='Identity card',required = True,tracking = True)
    gender = fields.Selection([('male','Male'),('female','Female')])
    date_of_birth = fields.Date(string='Date of birth')
    date_inscription = fields.Datetime(string='Date of inscription')
    e_mail = fields.Text(string='E-mail')
    phone = fields.Char(string='Phone number')
    departments_id = fields.Many2one(comodel_name='university.department', string='Departement')
    class_id = fields.Many2one(comodel_name='university.class', string='Classe')

    @api.model
    def create(self, values):
        if values.get('reference', _('New')) == _('New'):
            values['reference'] = self.env['ir.sequence'].next_by_code('university.student.seq') or _('New')
        result = super(UniversityStudent, self).create(values)
        return result

    @api.model
    def create(self, values):
        print("aziz")
        vals_user = {
            'name': values.get('f_name'),
            'login': values.get('e_mail'),
            #'password': values.get('mot_passe'),
            # other required field
        }
        user_id = self.env['res.users'].sudo().create(vals_user)
        values.update(student_id=user_id.id)
        res = super(UniversityStudent, self).create(values)
        return res





