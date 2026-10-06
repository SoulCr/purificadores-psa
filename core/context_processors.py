from urllib.parse import quote
from decouple import config


def whatsapp(request):
    numero = config('WHATSAPP_NUMERO', default='')
    mensaje = config('WHATSAPP_MENSAJE', default='Hola! Quiero información sobre los purificadores PSA.')
    url = f'https://wa.me/{numero}?text={quote(mensaje)}' if numero else ''
    return {'whatsapp_url': url, 'whatsapp_numero': numero}