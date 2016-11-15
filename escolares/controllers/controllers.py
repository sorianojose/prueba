# -*- coding: utf-8 -*-
from openerp import http

# class Escolares(http.Controller):
#     @http.route('/escolares/escolares/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/escolares/escolares/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('escolares.listing', {
#             'root': '/escolares/escolares',
#             'objects': http.request.env['escolares.escolares'].search([]),
#         })

#     @http.route('/escolares/escolares/objects/<model("escolares.escolares"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('escolares.object', {
#             'object': obj
#         })