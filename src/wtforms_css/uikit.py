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
        super().__init__("uk-table")


class RadioWidget:
    def __call__(self, field, **kwargs):
        kwargs.setdefault("id", field.id)
        html = []
        html.append(f'<div class="{field.container_css}">')
        for subfield in field:
            html.append(
                f"<label>{subfield(class_=field.css)} {subfield.label.text}</label><br>"
            )
        html.append("</div>")
        return Markup("".join(html))


Field.valid_css = "uk-form-success"
Field.invalid_css = "uk-form-danger"
Field.css = "uk-input"
Field.label_css = "uk-form-label"
TextAreaField.css = "uk-textarea"
IntegerRangeField.css = "uk-range"
DecimalRangeField.css = "uk-range"
BooleanField.css = "uk-checkbox"
RadioField.css = "uk-radio"
RadioField.container_css = "uk-form-controls"
RadioField.widget = RadioWidget()
SelectField.css = "uk-select"
SubmitField.css = "uk-button uk-button-default"
FileField.css = ""
ColorField.css = ""
