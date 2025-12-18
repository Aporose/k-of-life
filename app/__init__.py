# app/__init__.py
from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    # 配置
    app.config['SECRET_KEY'] = 'your-secret-key-here'

    # 注册蓝图
    from app.routes import api, web
    app.register_blueprint(api.bp)
    app.register_blueprint(web.bp)

    return app
