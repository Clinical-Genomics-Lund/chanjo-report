#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os

sys.path.append('/opt/chanjo-report/chanjo_report/')

from chanjo_report.server.app import create_app


class Config:
    #SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:////opt/chanjodb/chanjo.coverage.sqlite3"
    

application = create_app(config=Config)
            
