from flask_app import app
#                               ! DON'T Forget to import ALL Controllers Here
from flask_app.controllers import users
from flask_app.controllers import categories
from flask_app.controllers import myaapointements
from flask_app.controllers import businesses



if __name__ == '__main__':
    app.run(debug =True)