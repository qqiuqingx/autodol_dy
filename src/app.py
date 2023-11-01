from main import create_app
from controller import add_new_routes

app=create_app()
add_new_routes(app=app)

if __name__ == "__main__":

    app.run()
