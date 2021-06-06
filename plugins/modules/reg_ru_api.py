import httpx
import json


class REGRUAPIConnector:

    def __init__(self, username='test', password='test') -> None:
        self.username = username
        self.password = password
        self.base_url = 'https://api.reg.ru/api/regru2/'

    def make_credentials(self):
        return {
            'username': self.username,
            'password': self.password,
        }

    def make_url(self, endpoint):
        return self.base_url + endpoint

    def make_get_api_call(self, endpoint, payload={}):
        payload = {**payload, **self.make_credentials()}
        endpoint = self.make_url(endpoint)
        return httpx.get(url=endpoint, params=payload).json()

    def make_post_json_default_request_payload(self):
        return {
            'input_format': 'json',
            'output_format': 'json',
            'io_encoding': 'utf8',
            'show_input_params': 0,
        }

    def make_post_json_default_request_payload_params(self):
        return {
            'output_content_type': 'application/json'
        }

    def prepare_post_json_request_payload(self, payload):
        params = {
            **payload,
            **self.make_credentials(),
            **self.make_post_json_default_request_payload_params()
        }
        return {
            'input_data': json.dumps(params, ensure_ascii=False),
            **self.make_post_json_default_request_payload()
        }

    def make_post_api_call(self, endpoint, payload={}):
        payload = {**payload, **self.make_credentials()}
        endpoint = self.make_url(endpoint)
        return httpx.get(url=endpoint, params=payload).json()

    def nop(self):
        return self.make_get_api_call('nop')

    def zone_get_resource_records(self, domain):
        domains = [{'dname': domain}]
        return self.make_post_api_call('zone/get_resource_records', {
            'domains', domains
        })

    def zone_add_alias(self, domain, subdomain, ip_address):
        domains = [{'dname': domain}]
        return self.make_post_api_call('zone/add_alias', {
            'domains': domains,
            'subdomain': subdomain,
            'ipaddr': ip_address
        })
