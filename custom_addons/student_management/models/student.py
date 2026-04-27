from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import re


class StudentManagement(models.Model):
    _name = 'student.management'
    _description = 'Student Management'

    _inherit = ['mail.thread', 'mail.activity.mixin']


    _sql_constraints = [
        ('email_unique', 'unique(email)', 'Имэйл давхцаж болохгүй.'),
    ]

    name = fields.Char(string='Name', required=True, tracking=True)
    age = fields.Integer(string='Age', tracking=True)
    email = fields.Char(string='Email', tracking=True)
    gender = fields.Selection([
        ('male', 'Эрэгтэй'),
        ('female', 'Эмэгтэй'),
        ('other', 'Бусад')
    ], string='Хүйс', default='male', tracking=True)
    enrollment_date = fields.Date(string='Элссэн огноо', default=fields.Date.context_today, tracking=True)
    active = fields.Boolean(string='Идэвхтэй', default=True, tracking=True)

    @api.constrains('email')
    def _check_email(self):
        """Validate email format and uniqueness (when provided)."""
        email_regex = re.compile(r"[^@\s]+@[^@\s]+\.[^@\s]+")
        for rec in self:
            if rec.email and not email_regex.match(rec.email):
                raise ValidationError(_('Имэйл хаяг буруу байна: %s') % rec.email)