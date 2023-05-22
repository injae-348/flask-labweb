from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app,db)
    from . import models

    # 블루프린트
    from .views import main_views,mem_views,index_views,contact_views,news_views,project_views,pub_views,btn_views,auth_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(mem_views.bp)
    app.register_blueprint(index_views.bp)
    app.register_blueprint(contact_views.bp)
    app.register_blueprint(news_views.bp)
    app.register_blueprint(project_views.bp)
    app.register_blueprint(pub_views.bp)
    app.register_blueprint(btn_views.bp)
    app.register_blueprint(auth_views.bp)
    return app