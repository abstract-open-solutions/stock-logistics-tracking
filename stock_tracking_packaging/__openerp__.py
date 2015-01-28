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

{'name': 'Stock Packaging Tracking',
 'version': '1.0',
 'author': 'Abstract',
 'website': 'http://abstract.it',
 'license': 'AGPL-3',
 'category': 'Stock',
 'description': """
""",
 'depends': ['stock', 'product'],
 'data': ['views/product_view.xml', 'views/stock_view.xml',
          ],
 'installable': True,
 'application': True,
 }