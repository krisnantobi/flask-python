#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import wraps
from flask import jsonify

def json_response(fn):
    @wraps(fn)
    def get_result():
        result = fn()
        response = jsonify(result)
        return response
    return get_result
