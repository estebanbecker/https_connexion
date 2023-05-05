# -*- coding: utf-8 -*-
"""

Created on May 2022
@author: Mr ABBAS-TURKI

"""

from tools.core import Configuration
from ca.core import CertificateAuthority
from server.core import Server
import print_pems as ppems  #a été ajouté pour l'impression

RESOURCES_DIR = "resources/"
CA_PRIVATE_KEY_FILENAME = RESOURCES_DIR + "ca-private-key.pem"
CA_PUBLIC_KEY_FILENAME = RESOURCES_DIR + "ca-public-key.pem"
SERVER_PRIVATE_KEY_FILENAME = RESOURCES_DIR + "server-private-key.pem"
SERVER_CSR_FILENAME = RESOURCES_DIR + "server-csr.pem"
SERVER_PUBLIC_KEY_FILENAME = RESOURCES_DIR + "server-public-key.pem"
CA_PASSWORD = "XsFa$qN2H9bq^&Y@osMdR5Nqn6T2oDghC&Zij*xgSzXW!7m*hYDToVZukWFKVsaZo9hjSaprUftufpimcSdvhg2k!BwcZp5E4LjGoFEe$QHkLv65ozk*MGee8#BFfsHL"
SERVER_PASSWORD = "5LeRev7Swfa&Gr$prQ#HJT@35Tj3#D*Y2HrojYt2FX@^dJDr2VrnXAiaAS6SGUbL4VnNu%wPD^fKoqjrA#CV*sAKdrL*9WUwxgDCX*#Yg2jCb!j#*pF*HTsToLffi5ub"

CA_CONFIGURATION = Configuration("FR", "Territoire de Belfort", "Belfort", "EstebanBecker_CA", "localhost") 
SERVER_CONFIGURATION = Configuration("FR", "Territoire de Belfort", "Belfort", "EstebanBecker_SER", "localhost") 

# Création de l'autorité de certification
certificate_authority = CertificateAuthority(CA_CONFIGURATION, CA_PASSWORD, CA_PRIVATE_KEY_FILENAME, CA_PUBLIC_KEY_FILENAME)
    # regardez en haut et ca/core.py


# Création du server
server =Server(SERVER_CONFIGURATION, SERVER_PASSWORD, SERVER_PRIVATE_KEY_FILENAME, SERVER_CSR_FILENAME)
    # regardez en haut et server/core.py

# Signature du certificat par l'autorité de certification
signed_certificate = certificate_authority.sign(server._csr, SERVER_PUBLIC_KEY_FILENAME)

#impression des certificats à compléter regardez #print_pems

print("CA public key :")
ppems.print_perms(CA_PUBLIC_KEY_FILENAME)



print("finished ...")
