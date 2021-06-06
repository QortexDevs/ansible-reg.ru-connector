#!/usr/bin/env python

from re import U
import httpx
from ansible.module_utils.basic import AnsibleModule
from .reg_ru_api import REGRUAPIConnector
ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: reg_ru_nop
short_description: Checks REG.RU API health
version_added: '2.9'
description:
    - Module that checks REG.RU API health
requirements: [ httpx ]
author:
    - QortexDevs (@qortex)
options:
    username:
        description:
            - Valid REG.RU API username
        required: true
        type: str
    password:
        description:
            - Valid REG.RU API password
        required: true
        type: str
"""

EXAMPLES = """
# Retrieves all the  information from the computes of GNS3 server
- name: Retrieve all the facts of a GNS3 server computes
  gns3_facts:
    url: http://localhost
    get_images: all
    get_compute_ports: yes
  register: computes_info
- debug: var=computes_info
# Retrieves only basic facts data of the GNS3 server computes
- gns3_facts:
    url: http://localhost
  register: computes_info
- debug: var=computes_info
"""

RETURN = """
login:
    description: Current REG.RU API user login
    type: str
user_id:
    description: Current REG.RU API user id
    type: int
"""


def main():
    module = AnsibleModule(
        argument_spec=dict(
            username=dict(type="str", required=True),
            password=dict(type="str", required=True),
        )
    )

    username = module.params["username"]
    password = module.params["password"]

    reg_ru_connector = REGRUAPIConnector(username, password)
    zones_resource_records = reg_ru_connector.zone_get_resource_records(['qortex.ru'])

if __name__ == "__main__":
    main()
