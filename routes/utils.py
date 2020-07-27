#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import wraps
from flask import jsonify

def json_response(fn):
    @wraps(fn)
    def get_result(*args, **kwargs):
        result = fn(*args, **kwargs)
        response = jsonify(result), 400
        return response
    return get_result
