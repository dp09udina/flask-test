from flask_wtf import CSRFProtect, FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

WTF_CSRF_ENABLED = False


class QueryForm(FlaskForm):
    query = StringField("Type your query here:", validators=[DataRequired()])
    submit = SubmitField("Submit")
