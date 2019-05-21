
from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		'fieldname': 'Autohersteller',
		'transactions': [
			{
				'label': _('Autos'),
				'items': ['Auto']
			}
			
		]
	}
