from flask_wtf import FlaskForm
from wtforms import img
from wtforms.validators import InputRequired

class UploadForm(FlaskForm):
   file_upload = img('File', validators=[InputRequired()])