# wtforms-css
WTForms but with base CSS classes

Usage:

```
from wtforms_css.bootstrap import Form, StringField

class MyForm(Form):
    name = StringField("Name")

form = MyForm()

print(form.name(), form.label())
```

Result:

```
<input class="form-control" id="name" name="name" type="text" value="">
<label class="form-label" for="name">Name</label>
```

UIKit coming soon!

![screenshot](screenshot.png?raw=true "Screenshot")