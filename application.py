#!/usr/bin/env Python
# coding=utf-8

from url import url
import tornado.options
from tornado.options import define, options
import tornado.web
import os

define("debug", default=True, help="debug mode", type=bool)

settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "statics"),
    debug=options.debug,
)

application = tornado.web.Application(handlers=url, **settings)
