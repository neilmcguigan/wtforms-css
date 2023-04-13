# wtforms-css
WTForms but with base CSS classes

Usage:

```
from wtforms_css.bootstrap import Form, StringField

class MyForm(Form):
    name = StringField("Name")

form = MyForm()

print(form.name(), form.name.label())
```

Result:

```
<input class="form-control" id="name" name="name" type="text" value="">
<label class="form-label" for="name">Name</label>
```

or

```
from wtforms_css.uikit import Form, StringField

class MyForm(Form):
    name = StringField("Name")

form = MyForm()

print(form.name(), form.name.label())
```

Result:

```
<input class="uk-input" id="name" name="name" type="text" value="">
<label class="uk-form-label" for="name">Name</label>
```

![screenshot-bootstrap](screenshot-bootstrap.png?raw=true "Bootstrap")

![screenshot-uikit](screenshot-uikit.png?raw=true "UIKit")
