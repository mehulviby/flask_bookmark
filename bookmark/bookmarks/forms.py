from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, BooleanField, SubmitField
from wtforms.fields.html5 import URLField
from wtforms.validators import *
import sys
# import bookmark
# from bookmark import app


class BoolmarkForm(FlaskForm):
    url = URLField('The URL for your bookmark',
                   validators=[DataRequired(), url()])
    description = StringField('Add an optional description')
    tags = StringField('Tags', validators=[Regexp(
        r'^[a-zA-Z0-9, ]*$', message="Tags can contain only letters and numbers")])

    def validate(self):
        if not self.url.data.startswith("http://") and not self.url.data.startswith("https://"):
            self.url.data = "https://" + self.url.data

        # print(self.url.data)
        # sys.stdout.flush()
        if not FlaskForm.validate(self):
            return False

        if not self.description.data:
            self.description.data = self.url.data

        stripped = [t.strip() for t in self.tags.data.split(',')]
        not_empty = [tag for tag in stripped if tag]
        tagset = set(not_empty)
        self.tags.data = ",".join(tagset)

        return True

