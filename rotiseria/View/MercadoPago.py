import mercadopago
import json

mp = mercadopago.MP("2976477610493912", "36kgwdIqyhQeJylWXK8ftz692RzBWIYg");

def index(request, **kwargs):
    preference = {
        "items": [
        	{
                "title": "Manjares del Beagle",
                "quantity": 2,
                "currency_id": "ARS",
                "unit_price": (float)399.55
            }
        ]
    }
    preferenceResult = mp.create_preference(preference)
    return json.dumps(preferenceResult, indent=4)