from flask_app import app
from flask import request ,render_template, session, redirect, flash
from flask_app.models.user import User
from flask_app.models.category import Category 
from flask_app.models.business import Business

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)     #               we are creating an object called bcrypt,
#                          which is made by invoking the function Bcrypt with our app as an argument




@app.route('/businesses/<business_id>/destroy')
def delete_business(business_id ):
    if 'user_id' in session:
        Business.delete({'id':business_id})

    return redirect('/main_page')