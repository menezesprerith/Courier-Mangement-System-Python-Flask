from flask import Flask, render_template, url_for, redirect, session, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField, validators
from wtforms.validators import DataRequired, Email, ValidationError
import bcrypt
import random
import datetime
import time
from flask_mysqldb import MySQL
from fpdf import FPDF
from datetime import datetime

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'courier_management_system'
app.secret_key = 'mini_project'

mysql = MySQL(app)


class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    phone = StringField("Phone", default="+91", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    address = TextAreaField("Address", validators=[DataRequired()])
    submit = SubmitField("Register")


class AdminRegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Register")

    def validate_email(self, field):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM user_login_details where email=%s", (field.data,))
        user = cursor.fetchone()
        cursor.close()
        if user:
            raise ValidationError("Email already taken")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


class BookingForm(FlaskForm):
    weight = SelectField('Weights', choices=[('', 'Select from below---'), ('less than 1 kg', 'less than 1 kg')
        , ('between 1kg and 10kg', 'between 1kg and 10kg')
        , ('between 10kg and 25kg', 'between 10kg and 25kg')
        , ('between 25kg and 50kg', 'between 25kg and 50kg')
        , ('more than 50kgs', 'more than 50kgs')], validators=[DataRequired()])
    source = SelectField('Source', choices=[('', 'Select from below---'), ('Mysore', 'Mysore')
        , ('Kodagu', 'Kodagu')
        , ('Mandya', 'Mandya')
        , ('Hassan', 'Hassan')
        , ('Tumakuru', 'Tumakuru')], validators=[DataRequired()])
    destination = SelectField('Destination', choices=[('', 'Select from below---'), ('Mysore', 'Mysore')
        , ('Kodagu', 'Kodagu')
        , ('Mandya', 'Mandya')
        , ('Hassan', 'Hassan')
        , ('Tumakuru', 'Tumakuru')], validators=[DataRequired()])
    s_address = TextAreaField("Pickup Address", validators=[DataRequired()])
    d_address = TextAreaField("Destination Address", validators=[DataRequired()])
    s_pincode = StringField("Source Pincode", validators=[validators.DataRequired(), validators.Length(min=6, max=6)])
    d_pincode = StringField("Destination Pincode", validators=[validators.DataRequired(), validators.Length(min=6, max=6)])
    submit = SubmitField("Book my Parcel")


class ReviewForm(FlaskForm):
    review = TextAreaField("Review", validators=[DataRequired()])
    submit = SubmitField("Post")


class CustomerSupportForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    complaint = TextAreaField("Review", validators=[DataRequired()])
    submit = SubmitField("Register your complaint")


class UpdateStatusForm(FlaskForm):
    order_id = SelectField('Order ID', choices=[])
    currentLocation = SelectField('Current Location', choices=[('', 'Select from below---'), ('Mysore', 'Mysore')
        , ('Kodagu', 'Kodagu')
        , ('Mandya', 'Mandya')
        , ('Hassan', 'Hassan')
        , ('Tumakuru', 'Tumakuru')], default='', validators=[DataRequired()])
    currentStatus = SelectField('Current Status', choices=[('', 'Select from below---'), ('Booked', 'Booked')
        , ('Dispatched', 'Dispatched')
        , ('InTransit', 'InTransit')
        , ('Out For Delivery', 'Out For Delivery')
        , ('Delivered', 'Delivered')], default='', validators=[DataRequired()])
    submit = SubmitField('Update Status')


@app.route('/')
@app.route('/home')
def home():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM review_view")
    review = cursor.fetchall()
    cursor.close()
    return render_template('home.html', review=review)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM user_login_details where email=%s", (email,))
        user = cursor.fetchone()
        cursor.close()
        if user and bcrypt.checkpw(password.encode('utf-8'), user[3].encode('utf-8')):
            session['user_id'] = user[0]
            session['user_name'] = user[1]
            return redirect(url_for('dashboard'))
        else:
            flash("Login Failed. Please check you email and password")
            return redirect(url_for('login'))

    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        phone = form.phone.data
        address = form.address.data

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO user_login_details(name,email,password,phone,address) values (%s,%s,%s,%s,%s)",
                       (name, email, hashed_password, phone, address))
        mysql.connection.commit()
        cursor.close()

        flash("Account created Successfully. Please Login.")
        return redirect(url_for('login'))

    return render_template('register.html', form=form)


@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        user_id = session['user_id']

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM user_login_details where id=%s", (user_id,))
        user = cursor.fetchone()
        cursor.close()

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT order_id FROM order_details where user_id=%s", (user_id,))
        order = cursor.fetchall()
        cursor.close()

        if user:
            return render_template('dashboard.html', user=user, order=order)
    else:
        flash("Please login before you proceed")
        return redirect(url_for('login'))


@app.route('/admin_dashboard')
def admin_dashboard():
    if 'admin_id' in session:
        admin_id = session['admin_id']

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM admin_login_details where id=%s", (admin_id,))
        user = cursor.fetchone()
        cursor.close()

        if user:
            return render_template('admin_dashboard.html', user=user)
    else:
        flash("Please login before you proceed")
        return redirect(url_for('admin'))


'''@app.route('/adminregister', methods=['GET', 'POST'])
def admin_register():
    form = AdminRegisterForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO admin_login_details(name,email,password) values (%s,%s,%s)",
                       (name, email, hashed_password))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('admin_register'))

    return render_template('admin_register.html', form=form)'''


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM admin_login_details where email=%s", (email,))
        user = cursor.fetchone()
        cursor.close()
        if user and bcrypt.checkpw(password.encode('utf-8'), user[3].encode('utf-8')):
            session['admin_id'] = user[0]
            return redirect(url_for('admin_dashboard'))
        else:
            flash("Login Failed. Please check you email and password")
            return redirect(url_for('admin'))

    return render_template('admin.html', form=form)


@app.route('/pricing')
def pricing():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * from pricing_table_view;")
    item = cursor.fetchall()
    cursor.close()
    return render_template('pricing.html', item=item)


@app.route('/bookings', methods=['GET', 'POST'])
def bookings():
    if 'user_id' in session:
        user_id = session['user_id']
        form = BookingForm()

        if form.validate_on_submit():
            weight = form.weight.data
            source = form.source.data
            s_address = form.s_address.data
            d_address = form.d_address.data
            destination = form.destination.data
            s_pincode = form.s_pincode.data
            d_pincode = form.d_pincode.data
            order_id = generate_order_id()
            x = datetime.now()
            dt = x.strftime("%Y-%m-%d %H:%M:%S")
            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO order_details(order_id,user_id,weight,date_time,source,s_address,s_pin,"
                           "destination,"
                           "d_address,d_pin,current,status) values ("
                           "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                           (order_id, user_id, weight, dt, source, s_address, s_pincode, destination, d_address,
                            d_pincode, source, 'Booked'))
            mysql.connection.commit()
            cursor.close()
            flash("You have successfully booked your package. Please refer to pricing section for more details and "
                  "we'll collect you package from your doorstep. Thank You for Choosing Us.--TEC")
            return redirect(url_for('dashboard'))

    else:
        flash("Please login before you proceed")
        return redirect(url_for('login'))

    return render_template('bookings.html', form=form)


@app.route('/status')
def status():
    if 'user_id' in session:
        user_id = session['user_id']
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT order_id,source,destination,current,status,package_type FROM order_details where "
                       "user_id=%s", (user_id,))
        order = cursor.fetchall()
        cursor.close()
    else:
        flash("Please login before you proceed")
        return redirect(url_for('login'))

    return render_template('status.html', order=order)


@app.route('/customer_details')
def customer_details():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM user_login_details")
    user = cursor.fetchall()
    cursor.close()
    return render_template('customer_details.html', user=user)


@app.route('/reviews', methods=['GET', 'POST'])
def reviews():
    form = ReviewForm()
    if 'user_id' in session:
        user_id = session['user_id']
        user_name = session['user_name']
        if form.validate_on_submit():
            review = form.review.data
            cursor = mysql.connection.cursor()
            cursor.execute("INSERT into reviews(user_id,name,reviews) values(%s,%s,%s)", (user_id, user_name, review))
            mysql.connection.commit()
            cursor.close()
            flash("Your review was posted Successfully.")
            return redirect(url_for('reviews'))
    else:
        flash("Please login before you proceed")
        return redirect(url_for('login'))

    return render_template('reviews.html', form=form)


@app.route('/admin_reviews')
def admin_reviews():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * from reviews")
    user = cursor.fetchall()
    cursor.close()
    return render_template('admin_reviews.html', user=user)


@app.route('/delete_review/<id>', methods=['POST', 'GET'])
def delete_review(id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM reviews WHERE user_id=%s", (id,))
    mysql.connection.commit()
    cursor.close()
    flash("Review deleted successfully.")
    return redirect(url_for('admin_reviews'))


@app.route('/customer_support', methods=['POST', 'GET'])
def customer_support():
    form = CustomerSupportForm()
    if 'user_id' in session:
        user_id = session['user_id']
        user_name = session['user_name']

        email = form.email.data
        complaint = form.complaint.data

        if form.validate_on_submit():
            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO customer_support(user_id,name,email,complaint,reply) values(%s,%s,%s,%s,%s)",
                           (user_id, user_name, email, complaint, 'Reply Awaited'))
            mysql.connection.commit()
            cursor.close()
            flash("Your complaint is registered. We will get to back soon on your mail")
            return redirect(url_for('customer_support'))
    else:
        flash("Please login before you proceed")
        return redirect(url_for('login'))

    return render_template('customer_support.html', form=form)


@app.route('/admin_support')
def admin_support():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * from customer_support")
    complaint = cursor.fetchall()
    cursor.close()
    return render_template('admin_support.html', complaint=complaint)


@app.route('/package_status', methods=['GET', 'POST'])
def package_status():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM order_details")
    user = cursor.fetchall()
    cursor.close()
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT order_id FROM order_details")
    order = cursor.fetchall()
    cursor.close()
    choices = [(str(orders[0]), str(orders[0])) for orders in order]
    form = UpdateStatusForm()
    form.order_id.choices = choices

    if form.validate_on_submit():
        orderID = form.order_id.data
        cl = form.currentLocation.data
        cs = form.currentStatus.data
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE order_details set current=%s,status=%s where order_id=%s", (cl, cs, orderID))
        mysql.connection.commit()
        cursor.close()
        flash("The package status was successfully updated.")
        return redirect(url_for('package_status'))

    return render_template('package_status.html', user=user, form=form)

@app.route('/generate_pdf/<id>', methods=['POST', 'GET'])
def generate_pdf(id):
    now = datetime.now()
    if 'user_id' in session:
        user_id = session['user_id']
        pdf = FPDF()
        pdf.add_page()
        pdf.ln(0)
        image_width = 150
        x = (210 - image_width) / 2
        pdf.image('static/img/TEC_nb.jpg', x=x, y=20, w=image_width, h=40)
        pdf.set_font("Courier", 'B', 30)
        pdf.ln(60)
        pdf.cell(0, 10, txt="TEC COURIERS", ln=True, align='C')

        pdf.set_font("Courier", 'U', size=22)
        pdf.ln(20)
        pdf.cell(0, 10, txt="Order Details", ln=True, align='C')

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT order_id,weight,date_time,source,s_address,s_pin,destination,d_address,d_pin,"
                       "package_type FROM order_details where order_id=%s", (id,))
        orders = cursor.fetchall()

        pdf.set_font("Courier", size=12)
        for i, order in enumerate(orders):
            pdf.ln(10)
            pdf.cell(200, 10, txt=f"Order ID: {order[0]}", ln=i + 1, align='L')
            pdf.cell(200, 10, txt=f"Weight: {order[1]}", ln=i + 1, align='L')
            pdf.cell(200, 10, txt=f"Date and Time: {order[2]}", ln=i + 1, align='L')
            pdf.cell(200, 10, txt=f"Pickup(source) City: {order[3]}", ln=i + 1, align='L')
            pdf.cell(200, 10, txt=f"Pickup(source) Address: {order[4]}", ln=i + 1, align='L')
            pdf.cell(200, 10, txt=f"Pickup(source) Pincode: {order[5]}", ln=i + 1, align='L')
            pdf.cell(200, 10, txt=f"Destination City: {order[6]}", ln=i + 1, align='L')
            pdf.cell(200, 10, txt=f"Destination Address: {order[7]}", ln=i + 1, align='L')
            pdf.cell(200, 10, txt=f"Destination Pincode: {order[8]}", ln=i + 1, align='L')
            pdf.cell(200, 10, txt=f"Package Type: {order[9]}", ln=i + 1, align='L')
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d_%H%M%S")
        pdf.output(f"C:\\Users\\ADMIN\\Downloads\\order_details_{timestamp}.pdf")
        cursor.close()
        flash("PDF has been downloaded successfully.")
        return redirect(url_for('dashboard'))
    else:
        flash("Please login before you proceed")
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash("You have logged out successfully")
    return redirect(url_for('login'))


@app.route('/admin_logout')
def admin_logout():
    session.pop('user_id', None)
    flash("You have logged out successfully")
    return redirect(url_for('admin'))


def generate_order_id():
    timestamp = int(time.time())
    random_number = random.randint(10000, 99999)
    order_id = f"{timestamp}{random_number}"
    return order_id


if __name__ == '__main__':
    app.run(debug=True)
