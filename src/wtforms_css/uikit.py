import wtforms


class DefaultMixin:
    css = "uk-input"
    label_css = "uk-form-label"


class StringField(DefaultMixin, wtforms.StringField):
    ...
