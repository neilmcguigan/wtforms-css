from flask import Flask, render_template, request
from wtforms import FormField

from wtforms_css.uikit import (
    BooleanField,
    ColorField,
    DateField,
    DateTimeField,
    DateTimeLocalField,
    DecimalField,
    DecimalRangeField,
    EmailField,
    FieldList,
    FileField,
    FloatField,
    Form,
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


class MyFormField(Form):
    name = StringField("Name")
    age = IntegerField("Age")
    registered = BooleanField("Registered")
    another = SelectField("State", choices=choices)


class MySubform(Form):
    name = StringField("Name")


class KitchenSink(Form):
    boolean = BooleanField("Boolean")
    color = ColorField("Color")
    date = DateField("Date")
    datetime = DateTimeField("Date Time")
    datetimelocal = DateTimeLocalField("Date Time Local")
    decimal = DecimalField("Decimal")
    decimal_range = DecimalRangeField("Decimal Range")
    email = EmailField("Email")
    file = FileField("File")
    floatfield = FloatField("Float")
    hidden = HiddenField("Hidden")
    integer = IntegerField("Integer")
    integer_range = IntegerRangeField("Integer Range")
    month = MonthField("Month")
    multiple_file = MultipleFileField("Multiple File")
    password = PasswordField("Password")
    radio = RadioField("Radio", choices=choices)
    search = SearchField("Search")
    select = SelectField("Select", choices=choices)
    select_multiple = SelectMultipleField("Select Multiple", choices=choices)
    submit = SubmitField("Submit", render_kw={"class": "btn-primary"})
    string = StringField("String")
    tel = TelField("Tel")
    textarea = TextAreaField("Text Area")
    time = TimeField("Time")
    url = URLField("URL")
    # subform = FormField(MySubform)
    tabular = FieldList(FormField(MyFormField), min_entries=3, widget=TableWidget())


@app.get("/")
def index():
    return render_template("index.html", form=KitchenSink())


@app.post("/")
def index_post():
    form = KitchenSink(request.form)
    form.validate()
    return render_template("index.html", form=form)
