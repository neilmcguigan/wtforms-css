from markupsafe import Markup
from wtforms import (
    BooleanField,
    DateField,
    DateTimeField,
    DateTimeLocalField,
    DecimalField,
    DecimalRangeField,
    EmailField,
    Field,
    FieldList,
    FileField,
    FloatField,
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
    TelField,
    TextAreaField,
    TimeField,
    URLField,
)

import wtforms_css
from wtforms_css import ColorField, Form


class TableWidget(wtforms_css.TableWidget):
    def __init__(self):
        super().__init__("table table-borderless table-sm")


class RadioWidget:
    def __call__(self, field, **kwargs):
        kwargs.setdefault("id", field.id)
        html = []
        # html.append("<div>")
        for subfield in field:
            html.append(f'<div class="{field.container_css}">')
            html.append(
                f"{subfield(class_=field.css)} {subfield.label(class_=field.label_css)}"
            )
            html.append("</div>")
        # html.append("</div>")
        return Markup("".join(html))


Field.valid_css = "is-valid"
Field.invalid_css = "is-invalid"
Field.css = "form-control"
Field.label_css = "form-label"
IntegerRangeField.css = "form-range"
DecimalRangeField.css = "form-range"
BooleanField.css = "form-check-input"
BooleanField.label_css = "form-check-label"
RadioField.css = "form-check-input"
RadioField.label_css = "form-check-label"
RadioField.container_css = "form-check"
RadioField.widget = RadioWidget()
SelectField.css = "form-select"
SubmitField.css = "btn btn-primary"
ColorField.css = "form-control form-control-color"
HiddenField.css = ""
HiddenField.label_css = ""
