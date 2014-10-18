# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from ...server.app import create_app
from ...server.config import DefaultConfig


def render_html(api, options=None):
  """Start a Flask server to generate HTML report on request."""
  # spin up the Flask server
  config = DefaultConfig
  config.CHANJO_PANEL = options.get('report.panel')
  config.CHANJO_DB = options.get('db')
  config.CHANJO_DIALECT = options.get('dialect')

  app = create_app(config=config)

  return app.run('0.0.0.0', port=5000, debug=True, use_reloader=True)
