
from __future__ import unicode_literals
from frappe import _


def get_data():
    return [
        {
            "label": _("Auto"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Auto",
                    "label": _("Auto"),
                    "description": _("Auto")
                },
                {
                    "type": "doctype",
                    "name": "Autohersteller",
                    "label": _("Autohersteller"),
                    "description": _("Autohersteller")
                }
            ]
        }
         
        
    ]
