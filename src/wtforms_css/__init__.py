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
            if hasattr(result, "label_css") and result.label_css:
                result.label = Label(
                    result.label.field_id, result.label.text, result.label_css
                )
            return result

        def render_field(self, field, render_kw):
            if hasattr(field, "css") and field.css:
                render_kw.setdefault("class_", field.css)
            return super().render_field(field, render_kw)


class RadioWidget:
    def __call__(self, field, **kwargs):
        kwargs.setdefault("id", field.id)
        html = []
        html.append("<div>")
        for subfield in field:
            setattr(subfield, "css", field.css)
            html.append(f'<div class="{field.container_css}">')
            html.append(f"{subfield()} {subfield.label(class_=field.label_css)}")
            html.append("</div>")
        html.append("</div>")
        return Markup("".join(html))
