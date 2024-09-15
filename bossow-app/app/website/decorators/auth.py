from flask import  session, redirect, url_for, flash
from functools import wraps

def is_authenticated(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if 'user_id' not in session:
            flash('Para acessar essa página, é necessário estar logado.', category='error')
            return redirect(url_for('profiles.login'))

        return f(*args, **kwargs)
    return wrapper

def has_permission(permission):
    def has_permission_f(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if session['user_permission'] != permission:
                flash('Sem permissão de acesso!') 
                return redirect(url_for('index'))

            return f(*args, **kwargs)
        return wrapper
    return has_permission_f