{
    'name': 'Student Management',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Manage students',
    'description': """
        Student Management Module
    """,
    'author': 'Your Name',
    'website': '',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/student_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}