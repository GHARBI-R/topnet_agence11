
from odoo import http
from odoo.http import request


class University(http.Controller):
    # Sample Controller Created
    @http.route('/topnet/client/', website=True, auth='public')
    def university_student(self, **kw):
        return http.request.render("topnet_agence.client_page", {
        })\



    # creation dans la base de données
    @http.route('/creer/client', type="http", auth='public', website=True)
    def creeruser(self, **kw):

        http.request.env['client.fiche'].sudo().create(kw)
        return http.request.render('topnet_agence.client_page_thanks', {})
