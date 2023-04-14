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


class GridWidget(wtforms_css.GridWidget):
    def __init__(self):
        super().__init__("uk-table uk-table-small")


class TableWidget(wtforms_css.TableWidget):
    def __init__(self, with_table_tag=True, table_css="uk-table uk-table-small"):
        super().__init__(with_table_tag, table_css)


class RadioWidget:
    def __init__(self, extra_css: str = "") -> None:
        self.extra_css = extra_css

    def __call__(self, field, **kwargs):
        css = " ".join(
            filter(None, ["uk-form-controls", self.extra_css, kwargs.get("class")])
        )
        html = []
        html.append(f'<div class="{css}">')
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
