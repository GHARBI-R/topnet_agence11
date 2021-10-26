# -*- coding: utf-8 -*-
# from odoo import http


# class Depot(http.Controller):
#     @http.route('/depot/depot/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/depot/depot/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('depot.listing', {
#             'root': '/depot/depot',
#             'objects': http.request.env['depot.depot'].search([]),
#         })

#     @http.route('/depot/depot/objects/<model("depot.depot"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('depot.object', {
#             'object': obj
#         })
