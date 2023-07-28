import logging

from flask import Flask
from werkzeug.utils import find_modules, import_string


def configure_logging():
    # register root logging
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('werkzeug').setLevel(logging.INFO)


def register_blueprints(app):
    """Automagically register all blueprint packages
    Just take a look in the blueprints directory.
    """
    for name in find_modules('blueprints', recursive=True):
        mod = import_string(name)
        if hasattr(mod, 'bp'):
            app.register_blueprint(mod.bp)
    return None


def create_app():
    app = Flask(__name__)
    configure_logging()
    register_blueprints(app)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
