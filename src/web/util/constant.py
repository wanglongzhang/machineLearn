#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import jwcrypto.jwk as jwk

PROJECT_DIR = os.path.join(os.path.dirname(__file__), "..")
CODE_TEMPLATE_DIR = os.path.join(PROJECT_DIR, "template", "code")
DAL_DIR = os.path.join(PROJECT_DIR, "dal")
CONTROLLER_DIR = os.path.join(PROJECT_DIR, "controller")
#print(PROJECT_DIR)

key = jwk.JWK.generate(kty='RSA', size=2048)
priv_pem = key.export_to_pem(private_key=True, password=None)
pub_pem = key.export_to_pem()
private_key = jwk.JWK.from_pem(priv_pem)
public_key = jwk.JWK.from_pem(pub_pem)

jwt_algorithm = "RS256"
