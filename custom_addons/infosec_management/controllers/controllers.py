# from odoo import http


# class InfosecManagement(http.Controller):
#     @http.route('/infosec_management/infosec_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/infosec_management/infosec_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('infosec_management.listing', {
#             'root': '/infosec_management/infosec_management',
#             'objects': http.request.env['infosec_management.infosec_management'].search([]),
#         })

#     @http.route('/infosec_management/infosec_management/objects/<model("infosec_management.infosec_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('infosec_management.object', {
#             'object': obj
#         })

