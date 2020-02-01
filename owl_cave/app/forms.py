from flask_wtf import FlaskForm
from wtforms import SubmitField

class SelectNodeForm(FlaskForm):
	submit = SubmitField('next_node')