# -*- coding: utf-8 -*-
{
    'name': "Escolares",

    'summary': """ Gestor de Alumnos y Materias""",

    'description': """Este modulo permite gestionar las materias que curan los alumnos""",

    'author': "Jose Antonio Gonzalez Soriano",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'views/views.xml',
        'views/alumnos.xml',
        'views/materias.xml',
        'views/carreras.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],
}