import json
import logging
import requests


logger = logging.getLogger(__name__)

HEADERS = {
    'X-Auth': 'chong.kim',
}


def fetch_product_listing():
    url = 'https://careers.undercovertourist.com/assignment/1/products/'
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        logger.error(f'Error fetching {url} with status code: {response.status_code}\n{response.text}')
        return None
    return json.loads(response.text)


def fetch_product_detail(product_id):
    url = f'https://careers.undercovertourist.com/assignment/1/products/{product_id}'
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        logger.error(f'Error fetching {url} with status code: {response.status_code}\n{response.text}')
        return None
    return json.loads(response.text)

# returns True if successful otherwise False
def post_purchase(product_id, purchase):
    url = f'https://careers.undercovertourist.com/assignment/1/products/{product_id}/purchase'
    payload = {
        'customer_email': purchase.customer_email,
        'customer_name': purchase.customer_name,
        'customer_phone': purchase.customer_phone,
        'quantity': purchase.quantity,
    }
    response = requests.post(url, json=payload, headers=HEADERS)
    if response.status_code != 200:
        logger.error(f'Error posting {url} with status code: {response.status_code}\n{response.text}')
        return False
    return True
