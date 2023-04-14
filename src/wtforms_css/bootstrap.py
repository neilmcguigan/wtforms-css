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
        super().__init__("table table-borderless table-sm")


class TableWidget(wtforms_css.TableWidget):
    def __init__(
        self, with_table_tag=True, table_css="table table-borderless table-sm"
    ):
        super().__init__(with_table_tag, table_css)


class RadioWidget:
    """
    can use extra_cls=form-check-inline|form-check-reverse,form-switch
    """

    def __init__(self, extra_css: str = "") -> None:
        self.extra_css = extra_css

    def __call__(self, field, **kwargs):
        # kwargs should contain {"class":""|"is-valid"|"is-invalid"}
        css = " ".join(
            filter(None, ["form-check", self.extra_css, kwargs.get("class")])
        )
        html = []
        for subfield in field:
            html.append(f'<div class="{css}">')
            html.append(f"{subfield()}{subfield.label}")
            html.append("</div>")
        return Markup("".join(html))


Field.valid_css = "is-valid"
Field.invalid_css = "is-invalid"
Field.css = "form-control form-control-sm"
Field.label_css = "form-label"
IntegerRangeField.css = "form-range"
DecimalRangeField.css = "form-range"
BooleanField.css = "form-check-input"
BooleanField.label_css = "form-check-label"

RadioField.css = ""
SelectFieldBase._Option.css = "form-check-input"
SelectFieldBase._Option.label_css = "form-check-label"
RadioField.widget = RadioWidget()

SelectField.css = "form-select form-select-sm"
SubmitField.css = "btn btn-sm"
ColorField.css = "form-control form-control-color form-control-sm"
HiddenField.css = ""
