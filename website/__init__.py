from flask import Flask

def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']='1234'    
    from .views import views
    from .auth import auths
    app.register_blueprint(views, url_prefix="/")#página home
    app.register_blueprint(auths, url_prefix="/")#pagina login
    return app