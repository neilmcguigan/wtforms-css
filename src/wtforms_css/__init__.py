import wtforms
from markupsafe import Markup


class ColorInput(wtforms.widgets.Input):
    input_type = "color"


class ColorField(wtforms.StringField):
    widget = ColorInput()


class Label(wtforms.Label):
    def __init__(self, field_id: str, text: str, css: str):
        self.css = css
        super().__init__(field_id, text)

    def __call__(self, text=None, **kwargs):
        render_css = kwargs["class_"] if "class_" in kwargs else ""
        kwargs["class_"] = " ".join([self.css, render_css]).strip()
        return super().__call__(text, **kwargs)

    @staticmethod
    def from_(field: wtforms.Field):
        return Label(field.label.field_id, field.label.text, field.label_css)


class Form(wtforms.Form):
    def validate(self, extra_validators=None):
        self.meta.validated = True
        return super().validate(extra_validators)

    class Meta:
        validated = False

        def bind_field(self, form, unbound_field, options):
            field = super().bind_field(form, unbound_field, options)
            field.label = Label.from_(field)
            return field

        def render_field(self, field, render_kw):
            base_css = render_css = validation_css = ""
            if field.css:
                base_css = field.css
            if field.render_kw and "class" in field.render_kw:
                render_css = field.render_kw["class"]
            if "class_" in render_kw:
                render_css = render_kw["class_"]
            if self.validated and field.validators and field.type != "_Option":
                # _Options never have errors even if RadioField does...
                validation_css = "is-invalid" if field.errors else "is-valid"

            render_kw["class"] = " ".join(
                [base_css, render_css, validation_css]
            ).strip()

            return super().render_field(field, render_kw)


class TableWidget:
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


class DateTimeLocalField(wtforms.DateTimeLocalField):
    def __init__(self, *args, **kwargs):
        super().__init__(format="%Y-%m-%dT%H:%M", *args, **kwargs)
