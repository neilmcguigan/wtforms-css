import wtforms
from flask import Flask, render_template, request
from wtforms import FormField, validators

from wtforms_css.bootstrap import (
    BooleanField,
    ColorField,
    DateField,
    DateTimeLocalField,
    DecimalField,
    DecimalRangeField,
    EmailField,
    FieldList,
    FileField,
    FloatField,
    Form,
    GridWidget,
    HiddenField,
    IntegerField,
    IntegerRangeField,
    MonthField,
    MultipleFileField,
    PasswordField,
    RadioField,
    SearchField,
    SelectField,
    SelectMultipleField,
    StringField,
    SubmitField,
    TableWidget,
    TelField,
    TextAreaField,
    TimeField,
    URLField,
)

app = Flask(__name__)

choices = ["a", "b", "c"]
select_choices = ["", "a", "b", "c"]

validators = [validators.InputRequired()]


class MyFormField(Form):
    name = StringField("Name", validators=validators)
    age = IntegerField("Age", validators=validators)
    registered = BooleanField("Registered", validators=validators)
    another = SelectField("State", choices=select_choices, validators=validators)


class KitchenSink(Form):
    boolean = BooleanField("Boolean", validators=validators)
    color = ColorField("Color", validators=validators)
    date = DateField("Date", validators=validators)
    datetimelocal = DateTimeLocalField("Date Time Local", validators=validators)
    decimal = DecimalField("Decimal", validators=validators)
    decimal_range = DecimalRangeField("Decimal Range", validators=validators)
    email = EmailField("Email", validators=validators)
    file = FileField("File", validators=validators)
    floatfield = FloatField("Float", validators=validators)
    hidden = HiddenField("Hidden")
    integer = IntegerField("Integer", validators=validators)
    integer_range = IntegerRangeField("Integer Range", validators=validators)
    month = MonthField("Month", validators=validators)
    multiple_file = MultipleFileField("Multiple File", validators=validators)
    password = PasswordField(
        "Password",
        validators=validators,
        widget=wtforms.widgets.PasswordInput(hide_value=False),
    )
    radio = RadioField("Radio", choices=choices, validators=validators)
    search = SearchField("Search", validators=validators)
    select = SelectField("Select", choices=select_choices, validators=validators)
    select_multiple = SelectMultipleField(
        "Select Multiple", choices=choices, validators=validators
    )
    submit = SubmitField("Submit", render_kw={"class": "btn-primary"})
    string = StringField("String", validators=validators)
    tel = TelField("Tel", validators=validators)
    textarea = TextAreaField("Text Area", validators=validators)
    time = TimeField("Time", validators=validators)
    url = URLField("URL", validators=validators)
    field_list = FieldList(FormField(MyFormField), min_entries=3, widget=GridWidget())
    form_field = FormField(MyFormField, widget=TableWidget())


css = "bootstrap"


@app.get("/")
def index():
    form = KitchenSink()
    return render_template("index.html", form=form, css=css)


@app.post("/")
def index_post():
    form = KitchenSink(request.form)
    form.validate()

    return render_template("index.html", form=form, css=css)
