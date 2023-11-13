from src.main import create_app
from src.controller import add_new_routes

app=create_app()
add_new_routes(app=app)

if __name__ == "__main__":
    
    app.run(host='0.0.0.0',port=10038)
