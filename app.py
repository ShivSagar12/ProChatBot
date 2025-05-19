from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import secrets
import cohere

# Define the app first
app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # Required for CSRF protection

# Define the form
class Form(FlaskForm):
    text = StringField('Enter text to search', validators=[DataRequired()])
    submit = SubmitField('Submit')

# Now use @app.route
@app.route('/', methods=['GET', 'POST'])
def home():
    form = Form()
    co = cohere.Client('zy1RnsNJtznl02N75QvwngY8LKz6yzRmelKoTp9x')  # Replace with your valid key (API)

    if form.validate_on_submit():
        text = form.text.data
        response = co.chat(
            model='command-nightly',
            message=text,
            temperature=0.9,
            max_tokens=300
        )
        output = response.text
        return render_template('home.html', form=form, output=output)

    return render_template('home.html', form=form, output=None)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
