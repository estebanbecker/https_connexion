# -*- coding: utf-8 -*-
"""

Created on May 2022
@author: Mr ABBAS-TURKI

"""

from flask import Flask

# définir le message secret
SECRET_MESSAGE = "Je_suis_un_super_mot_de_passe" # A modifier
app = Flask(__name__)


@app.route("/")
def get_secret_message():
    return SECRET_MESSAGE


if __name__ == "__main__":

    # HTTPS version
    context = ('server-public-key.pem', 'server-private-key.pem')
    app.run(debug=True, host="0.0.0.0", port=8081, ssl_context=context)
   
