# -*- coding: utf-8 -*-
from odoo import http

# class EnriqueGarcia(http.Controller):
#     @http.route('/enrique_garcia/enrique_garcia/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/enrique_garcia/enrique_garcia/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('enrique_garcia.listing', {
#             'root': '/enrique_garcia/enrique_garcia',
#             'objects': http.request.env['enrique_garcia.enrique_garcia'].search([]),
#         })

#     @http.route('/enrique_garcia/enrique_garcia/objects/<model("enrique_garcia.enrique_garcia"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('enrique_garcia.object', {
#             'object': obj
#         })