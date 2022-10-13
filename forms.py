from wtforms import Form
from wtforms import StringField

class CommentForm(Form):
    valor=StringField('valor')