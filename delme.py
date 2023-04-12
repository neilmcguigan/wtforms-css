from wtforms_css import Form, StringField, SubmitField


class MyForm(Form):
    name = StringField("Name")


form = MyForm()

print(form.name(), form.name.label())
