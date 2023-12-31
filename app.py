from src.main import create_app

from src.resController import add_restful_routes
from flask_restful import Api

app=create_app()
api=Api(app)

add_restful_routes(api=api)
if __name__ == "__main__":
    
    app.run(host='0.0.0.0',port=10038)
