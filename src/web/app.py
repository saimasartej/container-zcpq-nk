import logging

from flask import Flask



def configure_logging():
    # register root logging
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('logger.log').setLevel(logging.INFO)




def create_app():
    app = Flask(__name__)
    configure_logging()
    register_blueprints(app)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
