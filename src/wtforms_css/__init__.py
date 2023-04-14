import wtforms
from markupsafe import Markup
from wtforms.widgets import html_params


class ColorInput(wtforms.widgets.Input):
    input_type = "color"


class ColorField(wtforms.StringField):
    widget = ColorInput()


class Label(wtforms.Label):
    def __init__(self, field_id: str, text: str, css: str):
        self.css = css
        super().__init__(field_id, text)

    def __call__(self, text=None, **kwargs):
        kwargs["class_"] = " ".join(filter(None, [self.css, kwargs.get("class_")]))
        return super().__call__(text, **kwargs)

    @staticmethod
    def from_(field: wtforms.Field):
        return Label(field.label.field_id, field.label.text, field.label_css)


class Form(wtforms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validated = False
        self.meta.form = self

    def validate(self, extra_validators=None):
        self.validated = True
        return super().validate(extra_validators)

    class Meta:
        def bind_field(self, form, unbound_field, options):
            field = super().bind_field(form, unbound_field, options)
            field.label = Label.from_(field)
            return field

        def render_field(self, field, render_kw):
            if field.type == "_Option":
                field.label = Label.from_(field)
                field.parent = self.form[field.name]

            validation_css = render_css = ""
            if field.render_kw:
                render_css = field.render_kw.get("class")
            # override field.render_kw w __call__ kwargs:
            render_css = render_kw.get("class_", render_css)

            errors = field.errors if field.type != "_Option" else field.parent.errors
            if self.form.validated and field.validators:
                validation_css = field.invalid_css if errors else field.valid_css

            render_kw["class"] = " ".join(
                filter(None, [field.css, render_css, validation_css])
            )

            return super().render_field(field, render_kw)


class GridWidget:
    def __init__(self, table_css: str = ""):
        self.table_css = table_css

    def __call__(self, field, **kwargs):
        if not len(field):
            return ""

        html = [f'<table class="{self.table_css}">\n']
        html.append("<thead>\n<tr>")
        for column in field[0]:
            html.append(
                f"<td>{column.label.text if column.type != 'SubmitField' else ''}</td>"
            )
        html.append("</tr>\n</thead>\n<tbody>\n")
        for row in field:
            html.append("<tr>")
            for cell in row:
                html.append(f"<td>{str(cell)}</td>")
            html.append("</tr>\n")
        html.append("</tbody>\n</table>\n")
        return Markup("".join(html))


class TableWidget(wtforms.widgets.TableWidget):
    def __init__(self, with_table_tag=True, table_css=""):
        super().__init__(with_table_tag)
        self.table_css = table_css

    def __call__(self, field, **kwargs):
        kwargs["class"] = " ".join(filter(None, [self.table_css, kwargs.get("class_")]))
        return super().__call__(field, **kwargs)


class DateTimeLocalField(wtforms.DateTimeLocalField):
    def __init__(self, *args, **kwargs):
        super().__init__(format="%Y-%m-%dT%H:%M", *args, **kwargs)
