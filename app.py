from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'b3f9d053519ee03f222043b69afb7fb0'  # Replace with a random secret key

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'eriugochisom6@gmail.com'  # your Gmail
app.config['MAIL_PASSWORD'] = 'dqihmsylvdezdjhl'         # app password

mail = Mail(app)

# Homepage route
@app.route('/')
def home():
    return render_template("index.html")

# Send message form submission
@app.route('/send-message', methods=['POST'])
def send_message():
    name = request.form['name']
    email = request.form['email']
    message_body = request.form['message']

    # --- Basic validation ---
    if not name or not email or not message_body:
        flash("All fields are required.", "danger")
        return redirect(url_for('home'))

    if "@" not in email or "." not in email:
        flash("Invalid email address.", "danger")
        return redirect(url_for('home'))

    # --- Sending email ---
    msg = Message(subject=f"Message from {name}",
                  sender=email,
                  recipients=['eriugochisom6@gmail.com'],  # your Gmail
                  body=message_body)
    try:
        mail.send(msg)
        flash("✅ Message sent successfully!", "success")
    except Exception as e:
        print(f"Error: {e}")  # helpful for debugging
        flash("❌ Failed to send message. Try again.", "danger")

    return redirect(url_for('home'))

# Menu page route
@app.route('/menu')
def menu():
    return render_template("menu.html")

if __name__ == "__main__":
    app.run(debug=True)





