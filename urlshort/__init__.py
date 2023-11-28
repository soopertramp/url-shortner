from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = 'svsvs64s4vd4vd4vd'

    from . import urlshort
    app.register_blueprint(urlshort.bp)

    return app