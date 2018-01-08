# -*- coding: utf-8 -*-
# Copyright 2018 Humanytek - Manuel Marquez <manuel@humanytek.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from openerp import fields, models


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    invoices_paid = fields.Boolean(
        related='sale_id.invoices_paid',
        string='Invoices Paid')
