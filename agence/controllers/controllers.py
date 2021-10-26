# -*- coding: utf-8 -*-
# from odoo import http


# class Agence(http.Controller):
#     @http.route('/agence/agence/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/agence/agence/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('agence.listing', {
#             'root': '/agence/agence',
#             'objects': http.request.env['agence.agence'].search([]),
#         })

#     @http.route('/agence/agence/objects/<model("agence.agence"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('agence.object', {
#             'object': obj
#         })
