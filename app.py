from flask import Flask, render_template, request, redirect, url_for, session, flash ,make_response
import pickle
import numpy as np
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from reportlab.pdfgen import canvas
from io import BytesIO
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
import os


app = Flask(__name__)
app.secret_key = "realestate_secret_key"

model = pickle.load(
open("model.pkl","rb")
)

def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        fullname = request.form["fullname"]
        email = request.form["email"]
        phone = request.form["phone"]
        password = generate_password_hash(request.form["password"])

        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("""
            INSERT INTO users(fullname,email,phone,password)
            VALUES(?,?,?,?)
            """,
                           (fullname, email, phone, password))

            conn.commit()
            flash("Registration Successful", "success")
            return redirect(url_for("login"))

        except:
            flash("Email Already Exists", "danger")

        finally:
            conn.close()

    return render_template("register.html")

@app.route("/")
def index():
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        conn = get_db_connection()

        user = conn.execute(
            "SELECT * FROM users WHERE email=?",
            (email,)
        ).fetchone()

        conn.close()

        if user and check_password_hash(
                user["password"], password):

            session["user_id"] = user["id"]
            session["fullname"] = user["fullname"]

            return redirect(url_for("profile"))

        flash("Invalid Credentials", "danger")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/profile")
def profile():

    if "user_id" not in session:
        return redirect(url_for("login"))

    conn = get_db_connection()

    user = conn.execute(
        "SELECT * FROM users WHERE id=?",
        (session["user_id"],)
    ).fetchone()

    conn.close()

    return render_template("profile.html",
                           user=user)


@app.route('/prediction', methods=['GET', 'POST'])
def prediction():

    if request.method == 'GET':
        return render_template('prediction.html')

    area = float(request.form['area'])
    bedrooms = int(request.form['bedrooms'])
    bathrooms = int(request.form['bathrooms'])
    stories = int(request.form['stories'])
    mainroad = int(request.form['mainroad'])
    guestroom = int(request.form['guestroom'])
    basement = int(request.form['basement'])
    hotwaterheating = int(request.form['hotwaterheating'])
    airconditioning = int(request.form['airconditioning'])
    parking = int(request.form['parking'])
    prefarea = int(request.form['prefarea'])
    furnishingstatus = int(request.form['furnishingstatus'])

    features = np.array([[
        area,
        bedrooms,
        bathrooms,
        stories,
        mainroad,
        guestroom,
        basement,
        hotwaterheating,
        airconditioning,
        parking,
        prefarea,
        furnishingstatus
    ]])

    prediction = round(model.predict(features)[0], 2)

    if 'user_id' in session:

        conn = get_db_connection()

        conn.execute("""
            INSERT INTO predictions(
                user_id,
                area,
                bedrooms,
                bathrooms,
                stories,
                parking,
                predicted_price
            )
            VALUES(?,?,?,?,?,?,?)
        """, (
            session['user_id'],
            area,
            bedrooms,
            bathrooms,
            stories,
            parking,
            prediction
        ))

        conn.commit()
        conn.close()

    return render_template(
        'prediction_result.html',
        prediction=prediction,
        area=area,
        bedrooms=bedrooms,
        bathrooms=bathrooms,
        stories=stories,
        parking=parking
    )

@app.route('/dashboard')
def dashboard():

    conn = sqlite3.connect(
        'database.db'
    )

    conn.row_factory = sqlite3.Row

    total_predictions = conn.execute(

        """
        SELECT COUNT(*)
        FROM predictions
        """

    ).fetchone()[0]

    avg_price = conn.execute(

        """
        SELECT AVG(predicted_price)
        FROM predictions
        """

    ).fetchone()[0]

    recent_predictions = conn.execute(

        """
        SELECT *
        FROM predictions
        ORDER BY id DESC
        LIMIT 10
        """

    ).fetchall()

    total_reviews = conn.execute("""

                                 SELECT COUNT(*)
                                 FROM feedback

                                 """).fetchone()[0]

    avg_rating = conn.execute("""

                              SELECT AVG(rating)
                              FROM feedback

                              """).fetchone()[0]

    total_reviews = total_reviews

    conn.close()

    return render_template(
        'dashboard.html',
        total_predictions=total_predictions,
        avg_price=round(avg_price or 0, 2),
        recent_predictions=recent_predictions,
        total_reviews=total_reviews,
        avg_rating=round(avg_rating or 0, 1)
    )

@app.route(
'/feedback',
methods=['GET','POST']
)
def feedback():

    if 'user_id' not in session:
        return redirect('/login')

    conn = sqlite3.connect(
        'database.db'
    )

    conn.row_factory = sqlite3.Row

    if request.method == 'POST':

        rating = int(
            request.form['rating']
        )

        review = request.form['review']

        conn.execute("""

        INSERT INTO feedback(

        user_id,
        rating,
        review

        )

        VALUES(?,?,?)

        """,

        (

        session['user_id'],
        rating,
        review

        ))

        conn.commit()

    reviews = conn.execute("""

    SELECT

    feedback.*,
    users.fullname

    FROM feedback

    JOIN users

    ON feedback.user_id =
    users.id

    ORDER BY feedback.id DESC

    """).fetchall()

    avg_rating = conn.execute("""

    SELECT AVG(rating)
    FROM feedback

    """).fetchone()[0]

    total_reviews = conn.execute("""

    SELECT COUNT(*)
    FROM feedback

    """).fetchone()[0]

    conn.close()

    return render_template(

        'feedback.html',

        reviews=reviews,

        avg_rating=
        round(avg_rating or 0,1),

        total_reviews=
        total_reviews

    )

sender_email = os.getenv("EMAIL_USER")
sender_password = os.getenv("EMAIL_PASS")

@app.route(
'/admin-login',
methods=['GET','POST']
)
def admin_login():

    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']

        conn = sqlite3.connect(
            'database.db'
        )

        conn.row_factory = sqlite3.Row

        admin = conn.execute("""

        SELECT *
        FROM admin

        WHERE email=?
        AND password=?

        """,

        (email,password)

        ).fetchone()

        conn.close()

        if admin:

            session['admin'] = True

            return redirect(
                '/admin-dashboard'
            )

    return render_template(
        'admin_login.html'
    )

@app.route('/admin-dashboard')
def admin_dashboard():

    if 'admin' not in session:
        return redirect('/admin-login')

    conn = sqlite3.connect(
        'database.db'
    )

    conn.row_factory = sqlite3.Row

    total_users = conn.execute("""

    SELECT COUNT(*)
    FROM users

    """).fetchone()[0]

    total_predictions = conn.execute("""

    SELECT COUNT(*)
    FROM predictions

    """).fetchone()[0]

    total_feedback = conn.execute("""

    SELECT COUNT(*)
    FROM feedback

    """).fetchone()[0]

    avg_price = conn.execute("""

    SELECT AVG(predicted_price)
    FROM predictions

    """).fetchone()[0]

    recent_users = conn.execute("""

    SELECT *
    FROM users

    ORDER BY id DESC

    LIMIT 5

    """).fetchall()

    conn.close()

    return render_template(

        'admin_dashboard.html',

        total_users=
        total_users,

        total_predictions=
        total_predictions,

        total_feedback=
        total_feedback,

        avg_price=
        round(avg_price or 0,2),

        recent_users=
        recent_users

    )

@app.route('/manage-users')
def manage_users():

    if 'admin' not in session:
        return redirect('/admin-login')

    conn = sqlite3.connect(
        'database.db'
    )

    conn.row_factory = sqlite3.Row

    users = conn.execute("""

    SELECT *
    FROM users

    ORDER BY id DESC

    """).fetchall()

    conn.close()

    return render_template(
        'manage_users.html',
        users=users
    )


@app.route('/manage-predictions')
def manage_predictions():

    if 'admin' not in session:
        return redirect('/admin-login')

    conn = sqlite3.connect(
        'database.db'
    )

    conn.row_factory = sqlite3.Row

    predictions = conn.execute("""

    SELECT predictions.*,
    users.fullname

    FROM predictions

    JOIN users

    ON predictions.user_id =
    users.id

    ORDER BY predictions.id DESC

    """).fetchall()

    conn.close()

    return render_template(

        'manage_predictions.html',

        predictions=predictions

    )

@app.route(
'/delete-prediction/<int:id>'
)
def delete_prediction(id):

    conn = sqlite3.connect(
        'database.db'
    )

    conn.execute("""

    DELETE FROM predictions

    WHERE id=?

    """,

    (id,))

    conn.commit()

    conn.close()

    return redirect(
        '/manage-predictions'
    )

@app.route('/manage-feedback')
def manage_feedback():

    if 'admin' not in session:
        return redirect('/admin-login')

    conn = sqlite3.connect(
        'database.db'
    )

    conn.row_factory = sqlite3.Row

    feedbacks = conn.execute("""

    SELECT feedback.*,
    users.fullname

    FROM feedback

    JOIN users

    ON feedback.user_id =
    users.id

    ORDER BY feedback.id DESC

    """).fetchall()

    conn.close()

    return render_template(

        'manage_feedback.html',

        feedbacks=feedbacks

    )


@app.route('/delete-user/<int:id>')
def delete_user(id):

    if 'admin' not in session:
        return redirect('/admin-login')

    conn = get_db_connection()

    conn.execute(
        "DELETE FROM users WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect('/manage-users')


@app.route('/delete-feedback/<int:id>')
def delete_feedback(id):

    if 'admin' not in session:
        return redirect('/admin-login')

    conn = get_db_connection()

    conn.execute(
        "DELETE FROM feedback WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect('/manage-feedback')

@app.route('/download-report/<float:price>')
def download_report(price):

    buffer = BytesIO()

    pdf = canvas.Canvas(buffer)

    pdf.setTitle("Property Valuation Report")

    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawString(100, 800, "EstateAI Property Report")

    pdf.setFont("Helvetica", 14)
    pdf.drawString(100, 750, f"Predicted Property Value: ₹ {price:,.2f}")

    pdf.drawString(100, 720, "Generated by AI Property Valuation System")

    pdf.save()

    buffer.seek(0)

    response = make_response(buffer.read())

    response.headers['Content-Type'] = 'application/pdf'

    response.headers['Content-Disposition'] = \
        'attachment; filename=Property_Report.pdf'

    return response

# ---------------------------
# FORGOT PASSWORD
# ---------------------------

@app.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():

    if request.method == "POST":

        email = request.form["email"]

        conn = get_db_connection()

        user = conn.execute(
            "SELECT * FROM users WHERE email=?",
            (email,)
        ).fetchone()

        conn.close()

        if not user:
            flash("Email not registered", "danger")
            return redirect(url_for("forgot_password"))

        otp = str(random.randint(100000, 999999))

        session["otp"] = otp
        session["email"] = email
        session["otp_expiry"] = (
            datetime.now() + timedelta(minutes=10)
        ).strftime("%Y-%m-%d %H:%M:%S")

        sender_email = "rprogramming21@gmail.com"
        sender_password = "fmto kpoo sffc veqy"

        try:

            msg = MIMEMultipart("alternative")

            msg["Subject"] = "🔐 EstateAI Password Reset OTP"
            msg["From"] = sender_email
            msg["To"] = email

            html = f"""
            <html>
            <body style="font-family:Arial;background:#f4f6f9;padding:20px;">

            <div style="
                max-width:650px;
                margin:auto;
                background:white;
                border-radius:15px;
                overflow:hidden;
                box-shadow:0 10px 25px rgba(0,0,0,.15);
            ">

                <div style="
                    background:linear-gradient(135deg,#0f172a,#2563eb);
                    color:white;
                    padding:35px;
                    text-align:center;
                ">

                    <h1>🏡 EstateAI</h1>

                    <p>
                    AI Powered Property Valuation System
                    </p>

                </div>

                <div style="padding:35px;">

                    <h2>
                    Password Reset Request
                    </h2>

                    <p>
                    Hello {user['fullname']},
                    </p>

                    <p>
                    We received a request to reset the password
                    for your EstateAI account.
                    </p>

                    <p>
                    Please use the OTP below to continue.
                    </p>

                    <div style="
                        text-align:center;
                        margin:30px 0;
                    ">

                        <span style="
                            display:inline-block;
                            font-size:40px;
                            font-weight:bold;
                            letter-spacing:8px;
                            color:#2563eb;
                            background:#eff6ff;
                            padding:18px 35px;
                            border-radius:12px;
                            border:2px dashed #2563eb;
                        ">
                            {otp}
                        </span>

                    </div>

                    <p>
                    ⏳ OTP Validity: <b>10 Minutes</b>
                    </p>

                    <p>
                    🔒 Never share this OTP with anyone.
                    </p>

                    <p>
                    EstateAI support team will never ask
                    for your OTP.
                    </p>

                    <div style="
                        background:#f8fafc;
                        padding:15px;
                        border-left:4px solid #2563eb;
                        margin-top:20px;
                    ">

                        <b>Security Notice</b>

                        <p>
                        If you didn't request a password reset,
                        simply ignore this email.
                        Your account remains secure.
                        </p>

                    </div>

                </div>

                <div style="
                    background:#0f172a;
                    color:white;
                    text-align:center;
                    padding:20px;
                ">

                    <p>
                    © 2026 EstateAI
                    </p>

                    <p>
                    Smart Real Estate Intelligence Platform
                    </p>

                </div>

            </div>

            </body>
            </html>
            """

            msg.attach(MIMEText(html, "html"))

            server = smtplib.SMTP(
                "smtp.gmail.com",
                587
            )

            server.starttls()

            server.login(
                sender_email,
                sender_password
            )

            server.sendmail(
                sender_email,
                email,
                msg.as_string()
            )

            server.quit()

            flash(
                "OTP sent successfully to your Gmail account.",
                "success"
            )

            return redirect(
                url_for("verify_otp")
            )

        except Exception as e:

            flash(
                f"Email Error: {str(e)}",
                "danger"
            )

            return redirect(
                url_for("forgot_password")
            )

    return render_template(
        "forgot_password.html"
    )

@app.route("/verify-otp", methods=["GET", "POST"])
def verify_otp():

    if request.method == "POST":

        entered_otp = request.form["otp"]

        expiry = datetime.strptime(
            session["otp_expiry"],
            "%Y-%m-%d %H:%M:%S"
        )

        if datetime.now() > expiry:

            flash(
                "OTP Expired",
                "danger"
            )

            return redirect(
                url_for("forgot_password")
            )

        if entered_otp == session.get("otp"):

            flash(
                "OTP Verified",
                "success"
            )

            return redirect(
                url_for("reset_password")
            )

        flash(
            "Invalid OTP",
            "danger"
        )

    return render_template(
        "verify_otp.html"
    )


@app.route(
    "/reset-password",
    methods=["GET", "POST"]
)
def reset_password():

    if request.method == "POST":

        new_password = request.form["password"]

        email = session.get("email")

        if not email:

            return redirect(
                url_for("forgot_password")
            )

        hashed_password = generate_password_hash(
            new_password
        )

        conn = get_db_connection()

        conn.execute(
            """
            UPDATE users
            SET password=?
            WHERE email=?
            """,
            (
                hashed_password,
                email
            )
        )

        conn.commit()

        conn.close()

        session.pop("otp", None)
        session.pop("email", None)

        flash(
            "Password Updated Successfully",
            "success"
        )

        return redirect(
            url_for("login")
        )

    return render_template(
        "reset_password.html"
    )




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)