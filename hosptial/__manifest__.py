{
    'name':'Hospital Mangment system',
    'author':'odoo develover',
    'version': '1.2',
    'website':'www.odoo.com',
    'Summary':'this is a test app',
    'installable': True,
    'application': True,
    "depends":['mail'],
    'data':[
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/menu.xml',
        'views/patient.xml',
        'views/doctor.xml',
            
    ]
}