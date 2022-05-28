from flask import Flask
from security import token_required


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config['SECRET_KEY'] = 'mysecretkey'

    import src.security as security
    app.register_blueprint(security.bp)
    
    @app.route('/unprotected')
    def unprotected():
        return 'Unprotected route!'

    @app.route('/onlyadmins')
    @token_required('admin')
    def onlyadmins():
        return 'Only admins route'

    @app.route('/onlyusers')
    @token_required('user')
    def onlyusers():
        return 'Only users route'

    return app

create_app().run()