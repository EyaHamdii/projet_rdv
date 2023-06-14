from flask_app import app
from flask import request ,render_template, session, redirect, flash
from flask_app.models.user import User
from flask_app.models.category import Category
from flask_app.models.myappointement import Appointment
from flask_app.models.disponibility import Disponibility
from flask_app.models.service import Service

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)     #               we are creating an object called bcrypt,
#                          which is made by invoking the function Bcrypt with our app as an argument



@app.route('/appointments/new')
def new_appointment():
    if 'user_id' in session:

        return render_template("make_appointment.html",dispo=Disponibility.get_all_disponibility(),service=Service.get_all_service())
    return redirect('/')
###ACTION ROUTE#####

@app.route('/Make/appointment' ,methods=['POST'])
def create_appointments():
    data = {
            **request.form,'user_id':session['user_id']
        }
    Appointment.add(data)
        
    return redirect('/appointments/new')

@app.route('/appointments/<appointment_id>/destroy')
def delete_appointment(appointment_id):
    if 'user_id' in session:
        Appointment.delete({'id':appointment_id})
    return redirect('/dashboard')

@app.route('/appointments/<appointment_id>/edit')
def edit_appointment(appointment_id):
    if 'user_id' in session:
        one_appointment=Appointment.get_by_id({'id':appointment_id})
        return render_template("make_appointment.html", appointment=one_appointment)
    return redirect('/')

##################################### ACTION ROUTE #########################################

@app.route('/Make/appointment/update' ,methods=['POST'])
def update_appointment(appointment_id):
    if(Appointment.validate(request.form)):
        Appointment.edit(request.form)
        return redirect('/appointments')
    return redirect('/appointments/'+str(appointment_id)+'/edit')