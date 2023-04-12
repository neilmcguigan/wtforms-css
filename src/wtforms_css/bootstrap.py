import wtforms

import wtforms_css


class Form(wtforms_css.Form):
    ...


class DefaultMixin:
    css = "form-control"
    label_css = "form-label"


class BooleanField(wtforms.BooleanField):
    css = "form-check-input"
    label_css = "form-check-label"


class ColorInput(wtforms.widgets.Input):
    input_type = "color"


class ColorField(DefaultMixin, wtforms.StringField):
    css = "form-control form-control-color"
    widget = ColorInput()


class DateField(DefaultMixin, wtforms.DateField):
    ...


class DateTimeField(DefaultMixin, wtforms.DateTimeField):
    ...


class DateTimeLocalField(DefaultMixin, wtforms.DateTimeLocalField):
    ...


class DecimalField(DefaultMixin, wtforms.DecimalField):
    ...


class DecimalRangeField(DefaultMixin, wtforms.DecimalRangeField):
    css = "form-range"


class EmailField(DefaultMixin, wtforms.EmailField):
    ...


class FileField(DefaultMixin, wtforms.FileField):
    ...


class FloatField(DefaultMixin, wtforms.FloatField):
    ...


class HiddenField(wtforms.HiddenField):
    css = ""
    label_css = ""


class IntegerField(DefaultMixin, wtforms.IntegerField):
    ...


class IntegerRangeField(DefaultMixin, wtforms.IntegerRangeField):
    css = "form-range"


class MonthField(DefaultMixin, wtforms.MonthField):
    ...


class MultipleFileField(DefaultMixin, wtforms.MultipleFileField):
    ...


class PasswordField(DefaultMixin, wtforms.PasswordField):
    ...


class RadioField(wtforms.RadioField):
    css = "form-check-input"
    label_css = "form-check-label"
    container_css = "form-check"
    widget = wtforms_css.RadioWidget()


class SearchField(DefaultMixin, wtforms.SearchField):
    ...


class SelectField(DefaultMixin, wtforms.SelectField):
    css = "form-select"


class SelectMultipleField(DefaultMixin, wtforms.SelectMultipleField):
    css = "form-select"


class SubmitField(wtforms.SubmitField):
    css = "btn"  # make so can append class at instantiation time
    label_css = ""


class StringField(DefaultMixin, wtforms.StringField):
    ...


class TelField(DefaultMixin, wtforms.TelField):
    ...


class TextAreaField(DefaultMixin, wtforms.TextAreaField):
    ...


class TimeField(DefaultMixin, wtforms.TimeField):
    ...


class URLField(DefaultMixin, wtforms.URLField):
    ...
