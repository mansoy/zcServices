from flask import Flask


def create_app(config_name = 'default'):
    app = Flask(__name__) #, static_folder=None)
    # app.url_map.default_subdomain = 'www'
    # 开启SERVER_NAME和sub_domain子域名之后，static需要重新自己添加路由
    # #要自己添加的static路由生效，必须开头的Flask先将static_folder=None才行，
    # app.config['SERVER_NAME'] = 'anspider.dev:5000'
    # app.static_url_path = "/static"
    # app.static_folder = "static"
    # app.add_url_rule(app.static_url_path + '/<path:filename>', endpoint='static', view_func=app.send_static_file, subdomain="odds")
    # app.add_url_rule(app.static_url_path + '/<path:filename>', endpoint='static', view_func=app.send_static_file, subdomain="data")
    # app.add_url_rule(app.static_url_path + '/<path:filename>', endpoint='static', view_func=app.send_static_file)
    # print(app.url_map)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .db import data as data_blueprint
    app.register_blueprint(data_blueprint, url_prefix='/data')

    from .test import mstest as mstest_blueprint
    app.register_blueprint(mstest_blueprint, url_prefix='/test')

    from .odds import odds as odds_blueprint
    app.register_blueprint(odds_blueprint, url_prefix='/odds')

    # app.config.update({
    #     'SERVER_NAME': 'mansoy.com:5000'
    # })
    
    return app
