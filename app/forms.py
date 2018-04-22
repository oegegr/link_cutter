from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL


class URLConverterForm(FlaskForm):
    url = StringField('URL', validators=[URL(), DataRequired()], render_kw={"placeholder": "Please enter URL"})
    submit = SubmitField('Get Short Url')


