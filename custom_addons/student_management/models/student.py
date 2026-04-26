from odoo import models, fields, api

class StudentManagement(models.Model):
    _name = 'student.management'  # ✅ Энэ нь яг таарч байх ёстой
    _description = 'Student Management'
    
    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    email = fields.Char(string='Email')