import wtforms
from markupsafe import Markup


class Label(wtforms.Label):
    def __init__(self, field_id, text, css=None):
        self.css = css
        super().__init__(field_id, text)

    def __call__(self, text=None, **kwargs):
        if self.css:
            kwargs.setdefault("class", self.css)
        return super().__call__(text, **kwargs)


class Form(wtforms.Form):
    class Meta:
        def bind_field(self, form, unbound_field, options):
            result = super().bind_field(form, unbound_field, options)
            if hasattr(result, "label_css"):
                result.label = Label(
                    result.label.field_id, result.label.text, result.label_css
                )
            return result

        def render_field(self, field, render_kw):
            if hasattr(field, "css") and field.css:
                render_kw.setdefault("class_", field.css)
            return super().render_field(field, render_kw)


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


class RadioWidget:
    def __call__(self, field, **kwargs):
        kwargs.setdefault("id", field.id)
        html = []
        for subfield in field:
            html.append(f'<div class="{field.container_css}">')
            html.append(
                f"{subfield(class_=field.css)} {subfield.label(class_=field.label_css)}"
            )
            html.append("</div>")
        return Markup("".join(html))


class RadioField(wtforms.RadioField):
    css = "form-check-input"
    label_css = "form-check-label"
    container_css = "form-check"
    widget = RadioWidget()


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
