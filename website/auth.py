from flask import Blueprint

auths=Blueprint('auths',__name__)

@auths.route('/login')
def login():
    return "<h1>Sou a tela de Login</h1>"

@auths.route('/logout')
def logout():
    return "<h1>Sou a tela de Logout</h1>"

@auths.route('/sign-up')
def sign_up():
    return "<h1>Sou a tela de sign-up</h1>"