# -*- coding: utf-8 -*-
# from odoo import http


# class DemandesClients(http.Controller):
#     @http.route('/demandes_clients/demandes_clients/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/demandes_clients/demandes_clients/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('demandes_clients.listing', {
#             'root': '/demandes_clients/demandes_clients',
#             'objects': http.request.env['demandes_clients.demandes_clients'].search([]),
#         })

#     @http.route('/demandes_clients/demandes_clients/objects/<model("demandes_clients.demandes_clients"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('demandes_clients.object', {
#             'object': obj
#         })
