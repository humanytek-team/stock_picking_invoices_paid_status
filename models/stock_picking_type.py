# -*- coding: utf-8 -*-
# Copyright 2018 Humanytek - Manuel Marquez <manuel@humanytek.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from openerp import fields, models, api


class StockPickingType(models.Model):
    _inherit = 'stock.picking.type'

    foo_picking_type = fields.Boolean(
        compute='_get_invoices_paid',
    )

    @api.one
    def _get_invoices_paid(self):
        if self.id != 2:
            return
        pickings = self.env['stock.picking'].search(
            [('origin', 'like', 'SO%'), ('invoices_paid_persistent', '=', False), ('state', '=', 'assigned'), ('picking_type_id', '=', 2)])
        for picking in pickings:
            if picking.sale_id.invoice_ids:
                for inv in picking.sale_id.invoice_ids:
                    if inv.state != 'paid':
                        break
                else:
                    picking.invoices_paid_persistent = True
