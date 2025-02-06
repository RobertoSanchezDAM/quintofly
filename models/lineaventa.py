# -- coding: utf-8 --

from odoo import models, fields, api

class LineaVenta(models.Model):
    _name = 'quintofly.lineaventa'
    _description = 'Línea de Venta'

    venta_id = fields.Many2one('quintofly.venta', string="Venta", required=True)
    subtotal = fields.Float("Subtotal", required=True)
    vuelo_id = fields.Many2one('quintofly.vuelo', string="Vuelo asociado", required=True)
    num_horas = fields.Integer("Número de horas", required=True)
