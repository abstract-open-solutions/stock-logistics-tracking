# -*- coding: utf-8 -*-
###############################################################################
#
#    Copyright (C) 2015 Abstract srl
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from math import ceil
from openerp.osv import fields, orm


class StockTracking(orm.Model):

    _inherit = 'stock.tracking'

    _columns = {
        'product_ul_id': fields.many2one('product.ul', 'Packaging'),
    }


class StockMove(orm.Model):
    _inherit = 'stock.move'

    _columns = {
        'content_move_id': fields.many2one('stock.move', 'Content move'),
        'packaging_move_id': fields.many2one('stock.move', 'Packaging move'),
    }


class StockPicking(orm.Model):
    _inherit = 'stock.picking'

    def do_partial(self, cr, uid, ids, partial_datas, context=None):
        move_pool = self.pool.get('stock.move')

        res = super(StockPicking, self).do_partial(
            cr, uid, ids, partial_datas, context=context)

        for picking_id in res:
            picking = self.browse(cr, uid, picking_id)
            for move in picking.move_lines:

                packaging_id = move.tracking_id.product_ul_id
                if packaging_id:
                    packaging_qty = move.product_packaging.qty
                    pack_move_data = {
                        'product_id': packaging_id.product_id.id,
                        'product_qty': ceil(move.product_qty / packaging_qty),
                        'product_uom': packaging_id.product_id.uom_id.id,
                        'name': "%s [%s]" % (
                            packaging_id.product_id.name,
                            move.tracking_id.name),
                        'origin': picking.name,
                        'content_move_id': move.id,
                        'type': move.type,
                        'location_id': move.location_id.id,
                        'location_dest_id': move.location_dest_id.id,
                        'partner_id': move.picking_id.partner_id.id,
                        'date': move.date,
                        'state': 'done'
                    }
                    packaging_move_id = move_pool.create(
                        cr, uid, pack_move_data)
                    move.write({'packaging_move_id': packaging_move_id})
                pass
        return res
