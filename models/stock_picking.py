# -*- coding: utf-8 -*-
# Copyright 2018 Humanytek - Manuel Marquez <manuel@humanytek.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from openerp import fields, models, api


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    invoices_paid_persistent = fields.Boolean(
        string='Invoices Paid',
    )

    invoices_paid = fields.Boolean(
        compute='_get_invoices_paid',
        string='Invoices Paid')

    @api.one
    def _get_invoices_paid(self):
        if self.sale_id.invoice_ids:
            self.invoices_paid = True
            for inv in self.sale_id.invoice_ids:
                if inv.state != 'paid':
                    self.invoices_paid = False
                    break
            else:
                self.write({'invoices_paid_persistent': True})
