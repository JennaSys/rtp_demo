from pyreact import useState, render, react_component
from pyreact import Form, Label, Input, Ol, Li


@react_component
def ListItems(props):
    items = props['items']
    return [Li({'key': item}, item) for item in items]


def App():
    newItem, setNewItem = useState("")
    items, setItems = useState([])

    def handleSubmit(event):
        event.preventDefault()
        # setItems(items.__add__(newItem))
        setItems(items + [newItem])  # __:opov
        setNewItem("")

    def handleChange(event):
        target = event['target']
        setNewItem(target['value'])

    return Form({'onSubmit': handleSubmit},
              Label({'htmlFor': 'newItem'}, "New Item: "),
              Input({'id': 'newItem',
                           'onChange': handleChange,
                           'value': newItem
                           }
                 ),
              Input({'type': 'submit'}),
              Ol(None,
                 ListItems({'items': items})
                 )
              )


render(App, None, 'root')
