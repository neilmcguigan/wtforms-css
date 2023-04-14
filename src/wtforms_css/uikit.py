from markupsafe import Markup
from wtforms import (
    BooleanField,
    DateField,
    DateTimeField,
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
    SelectFieldBase,
    SelectMultipleField,
    StringField,
    SubmitField,
    TelField,
    TextAreaField,
    TimeField,
    URLField,
)

import wtforms_css
from wtforms_css import ColorField, DateTimeLocalField, Form


class TableWidget(wtforms_css.TableWidget):
    def __init__(self):
        super().__init__("uk-table")


class RadioWidget:
    def __init__(self, container_css: str = "uk-form-controls") -> None:
        self.container_css = container_css

    def __call__(self, field, **kwargs):
        validation_css = kwargs.get("class")
        html = []
        html.append(f'<div class="{self.container_css} {validation_css}">')
        for subfield in field:
            html.append(f"<label>{subfield()} {subfield.label.text}</label><br>")
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

RadioField.css = ""
SelectFieldBase._Option.css = ""
RadioField.widget = RadioWidget()

RadioField.css = ""
SelectFieldBase._Option.css = "uk-radio"
SelectFieldBase._Option.label_css = ""
RadioField.widget = RadioWidget()

SelectField.css = "uk-select"
SubmitField.css = "uk-button uk-button-default"
FileField.css = ""
ColorField.css = ""
