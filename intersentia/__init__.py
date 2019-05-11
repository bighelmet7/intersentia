from flask import Flask

def create_app(config_obj='intersentia.config.DevelopmentConfig'):
    """
    Returns an app Flask object configurated with the given config_obj.
    """
    app = Flask(__name__)
    app.config.from_object(config_obj)

    from extensions import db
    from extensions import migrate
    # TODO: command to create database and context db_models.
    # understand the concept of session and scoped_session.
    # Create makemigrations and migrate.
    db.init_app(app)
    migrate.init_app(app, db=db, render_as_batch=True)

    from v1.blueprint import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
