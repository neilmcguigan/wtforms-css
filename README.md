# wtforms-css
WTForms but with base CSS classes

Usage:

```
from wtforms.validators import InputRequired, Optional

from wtforms_css.bootstrap import Form, RadioField, StringField, SubmitField
# or from wtforms_css.uikit ...

class MyForm(Form):
    name = StringField("Name", validators=[Optional()])
    radio = RadioField("Radio", choices=["a", "b"], validators=[InputRequired()])
    submit = SubmitField("Submit", render_kw={"class": "btn-primary"})

form = MyForm()
form.validate()

print(form.name(), form.name.label())
print(form.radio())
print(form.submit())
```

Result:

```
<input class="form-control is-valid" id="name" name="name" type="text" value="">
<label class="form-label" for="name">Name</label>

<div class="form-check is-invalid">
    <input class="form-check-input is-invalid" id="radio-0" name="radio" required type="radio" value="a">
    <label class="form-check-label" for="radio-0">a</label>
</div>
<div class="form-check is-invalid">
    <input class="form-check-input is-invalid" id="radio-1" name="radio" required type="radio" value="b">
    <label class="form-check-label" for="radio-1">b</label>
</div>

<input class="btn btn-primary" id="submit" name="submit" type="submit" value="Submit">
```

Want to integrate your own framework?

```
import wtforms_css

from wtforms import Field, StringField

Field.css = "class-applied-to-all-fields"
Field.label_css = "class-applied-to-all-labels"
Field.valid_css = "class-applied-to-fields-when-valid"
Field.invalid_css = "class-applied-to-fields-when-invalid"
StringField.css = "class-applied-to-StringField-and-subclasses"

class MyForm(wtforms_css.Form):
    foo = StringField("foo")

```

Bootstrap:
![screenshot-bootstrap](screenshot-bootstrap.png?raw=true "Bootstrap")

UIKit:
![screenshot-uikit](screenshot-uikit.png?raw=true "UIKit")
