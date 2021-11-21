from odoo import models, fields, api, _


class UniversityTeacher(models.Model):
    _name = 'university.teacher'
    _description = 'Teacher management'
    _rec_name = 'f_name'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    date_start = fields.Datetime('Date of start', tracking=True)
    teacher_id = fields.Many2one('res.users', ondelete='set null', string="User", index=True)
    f_name = fields.Char('First Name', tracking=True)
    l_name = fields.Char('Last Name', tracking=True)
    identity_card = fields.Char('Identity card', required=True, tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    date_of_birth = fields.Date('Date of birth', tracking=True)
    date_start = fields.Datetime('Date of start', tracking=True)
    e_mail = fields.Char('E-mail', tracking=True)
    phone = fields.Char('Phone number', tracking=True)
    rue = fields.Char('Rue')
    ville = fields.Char('Ville')
    code_postale = fields.Char('Code postale')
    suggestions = fields.Text('Suggestions')
    departments_id = fields.Many2one(comodel_name='university.department', string='Departement')
    subject_id = fields.Many2one(comodel_name='university.subject', string='Matiere')
    class_ids = fields.Many2many('university.class', 'prof_class_rel', 'f_name', 'class_name', string='Classe')

    # reference = fields.Char(string='teacher reference', required=True, copy=False, readonly=True,
    #                         default=lambda self: _('New'))



    @api.model
    def create(self, values):
        # if values.get('reference', _('New')) == _('New'):
        #     values['reference'] = self.env['ir.sequence'].next_by_code('university.teacher.seq') or _('New')
        # res = super(UniversityTeacher, self).create(values)

        vals_user = {
            'name': values.get('f_name'),
            'login': values.get('e_mail'),
            # 'password': values.get('mot_passe'),
            # other required field
        }
        user_id = self.env['res.users'].sudo().create(vals_user)
        values.update(teacher_id=user_id.id)
        res = super(UniversityTeacher, self).create(values)

        return res
