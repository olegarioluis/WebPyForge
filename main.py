from flask import Flask
from routes.login import login_route
from routes.Register import register_route
from routes.page import page_route


app = Flask(__name__)

app.register_blueprint(login_route)
app.register_blueprint(register_route)
app.register_blueprint(page_route)


if __name__ == '__main__':
    app.run(debug=True)
