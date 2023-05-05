# -*- coding: utf-8 -*-
"""

Created on May 2022
@author: Mr ABBAS-TURKI

"""

import pem

RESOURCES_DIR = "resources/"
CA_PRIVATE_KEY_FILENAME = RESOURCES_DIR + "ca-private-key.pem"
CA_PUBLIC_KEY_FILENAME = RESOURCES_DIR + "ca-public-key.pem"
SERVER_PRIVATE_KEY_FILENAME = RESOURCES_DIR + "server-private-key.pem"
SERVER_CSR_FILENAME = RESOURCES_DIR + "server-csr.pem"
SERVER_PUBLIC_KEY_FILENAME = RESOURCES_DIR + "server-public-key.pem"


def print_perms(filename: str):
    #print the content of the file
    print(pem.parse_file(filename))
    print("file content :")
    with open(filename, 'r') as f:
        print(f.read())

def uncrypte_perms(filename: str, password: str):
    #print the content of the file
    cert = pem.parse_file(filename, password=password)
    print(cert)

    
