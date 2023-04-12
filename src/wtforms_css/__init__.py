import wtforms
from markupsafe import Markup


class ColorInput(wtforms.widgets.Input):
    input_type = "color"


class ColorField(wtforms.StringField):
    widget = ColorInput()


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
            field = super().bind_field(form, unbound_field, options)
            if hasattr(field, "label_css") and field.label_css:
                field.label = Label(
                    field.label.field_id,
                    field.label.text,
                    field.label_css,
                )
            return field

        def render_field(self, field, render_kw):
            if hasattr(field, "css") and field.css:
                render_kw.setdefault("class_", field.css)
                if field.raw_data is not None:
                    if field.errors:
                        render_kw["class_"] = f"{field.css} {field.invalid_css}"
                    else:
                        render_kw["class_"] = f"{field.css} {field.valid_css}"
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
