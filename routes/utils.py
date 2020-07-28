#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import wraps
from flask import jsonify, g, url_for, redirect, request, session

def json_response(fn):
    @wraps(fn)
    def get_result(*args, **kwargs):
        result = fn(*args, **kwargs)
        response = jsonify(result), 400
        return response
    return get_result

def login_required(fn):
    @wraps(fn)
    def get_result(*args, **kwargs):
        result = fn(*args, **kwargs)
        if check_key(session, 'profile'):
            return fn(*args, **kwargs)
        else:
            return redirect(url_for('auth_route.login', next=request.url))
    return get_result

def check_key(dict, key):
    if key in dict.keys():
        return True
    else:
        return False
    
