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
    SelectMultipleField,
    StringField,
    SubmitField,
    TelField,
    TextAreaField,
    TimeField,
    URLField,
)
from wtforms.fields.choices import SelectFieldBase
from wtforms.widgets import html_params

import wtforms_css
from wtforms_css import ColorField, DateTimeLocalField, Form


class TableWidget(wtforms_css.TableWidget):
    def __init__(self):
        super().__init__("table table-borderless table-sm")


class RadioWidget:
    def __init__(self, container_css: str = "form-check") -> None:
        self.container_css = container_css

    def __call__(self, field, **kwargs):
        # kwargs.setdefault("id", field.id)
        extra = ""
        if "class" in kwargs:
            extra = kwargs["class"]
        html = []
        for subfield in field:
            html.append(f'<div class="{self.container_css} {extra}">')
            html.append(
                f"{subfield(class_=f'form-check-input {extra}')}{subfield.label(class_='form-check-label')}"
            )
            html.append("</div>")
        return Markup("".join(html))


Field.valid_css = "is-valid"
Field.invalid_css = "is-invalid"
Field.css = "form-control"
Field.label_css = "form-label"
IntegerRangeField.css = "form-range"
DecimalRangeField.css = "form-range"
BooleanField.css = "form-check-input"
BooleanField.label_css = "form-check-label"

RadioField.css = ""
SelectFieldBase._Option.css = ""
RadioField.widget = RadioWidget()

SelectField.css = "form-select"
SubmitField.css = "btn"
ColorField.css = "form-control form-control-color"
HiddenField.css = ""
