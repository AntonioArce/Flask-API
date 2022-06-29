from flask import Flask
from config import config

#routes
from routes import Movie

app = Flask(__name__)

def page_not_found(error):
    return "<h1>Not Found Page</h1>",404

if __name__ == '__main__':
    app.config.from_object(config['development'])

    #Blueprint
    app.register_blueprint(Movie.main, url_prefix = '/api/movies')

    #ERROR 
    app.register_error_handler(404,page_not_found)
    app.run()

