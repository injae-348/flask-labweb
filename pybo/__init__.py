from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

db = SQLAlchemy()
migrate = Migrate()

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()

def page_not_found(e):
    return render_template('404.html'),404

# 애플리케이션 팩토리(create_app()함수)
def create_app():
    app = Flask(__name__)
    app.config.from_envvar('APP_CONFIG_FILE')

    # ORM
    db.init_app(app)
    
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)
    
    migrate.init_app(app,db)
    from . import models

    # 블루프린트 -> 라우팅 함수 체계적으로 관리
    # URL과 함수의 매핑을 관리하는 클래스
    from .views import main_views,mem_views,index_views,contact_views,news_views,project_views,pub_views,auth_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(mem_views.bp)
    app.register_blueprint(index_views.bp)
    app.register_blueprint(contact_views.bp)
    app.register_blueprint(news_views.bp)
    app.register_blueprint(project_views.bp)
    app.register_blueprint(pub_views.bp)
    app.register_blueprint(auth_views.bp)


    return app