from pyreact import useState, render, createElement as el


def ListItems(props):
    items = props['items']
    return [el('li', {'key': item}, item) for item in items]


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

    return el('form', {'onSubmit': handleSubmit},
              el('label', {'htmlFor': 'newItem'}, "New Item: "),
              el('input', {'id': 'newItem',
                           'onChange': handleChange,
                           'value': newItem
                           }
                 ),
              el('input', {'type': 'submit'}),
              el('ol', None,
                 el(ListItems, {'items': items})
                 )
              )


render(App, None, 'root')
