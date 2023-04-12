from flask import Flask, render_template

from wtforms_css.bootstrap import (
    BooleanField,
    ColorField,
    DateField,
    DateTimeField,
    DateTimeLocalField,
    DecimalField,
    DecimalRangeField,
    EmailField,
    FileField,
    FloatField,
    Form,
    HiddenField,
    InlineRadioField,
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
    TelField,
    TextAreaField,
    TimeField,
    URLField,
)

app = Flask(__name__)

choices = ["a", "b", "c"]


class KitchenSink(Form):
    boolean = BooleanField("Boolean")
    color = ColorField("Color", render_kw={"value": "#0400ff"})
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
    # radio2 = InlineRadioField("Inline Radio", choices=choices)
    search = SearchField("Search")
    select = SelectField("Select", choices=choices)
    select_multiple = SelectMultipleField("Select Multiple", choices=choices)
    submit = SubmitField("Submit")
    string = StringField("String")
    tel = TelField("Tel")
    textarea = TextAreaField("Text Area")
    time = TimeField("Time")
    url = URLField("URL")


@app.get("/")
def index():
    return render_template("index.html", form=KitchenSink())
