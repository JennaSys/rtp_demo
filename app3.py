from pyreact import useState, render, react_component
from pyreact import Form, Label, Input, Ol, Li, Button


@react_component
def ListItem(props):
    item = props['item']
    handleDelete = props['handleDelete']
    handleEdit = props['handleEdit']

    return Li(None,
              props['item'] + " ",
              Button({'type': 'button',
                      'onClick': lambda: handleDelete(item)
                      }, "Delete"
                     ),
              Button({'type': 'button',
                      'onClick': lambda: handleEdit(item)
                      }, "Edit"
                     ),
              )


@react_component
def ListItems(props):
    items = props['items']
    handleDelete = props['handleDelete']
    handleEdit = props['handleEdit']

    return [
        ListItem({'key': item,
                  'item': item,
                  'handleDelete': handleDelete,
                  'handleEdit': handleEdit}
                 ) for item in items]


@react_component
def App():
    newItem, setNewItem = useState("")
    editItem, setEditItem = useState("")
    items, setItems = useState([])

    def handleSubmit(event):
        event.preventDefault()
        if editItem:  # In edit mode
            new_list = list(items)  # Make a copy
            new_list[new_list.index(editItem)] = newItem
            setItems(new_list)  # Update our state
        else:  # In add mode
            # setItems(items.__add__(newItem))
            setItems(items + [newItem])  # __:opov
        setEditItem("")
        setNewItem("")

    def handleChange(event):
        target = event['target']
        setNewItem(target['value'])

    def handleDelete(item):
        new_list = list(items)  # Make a copy
        new_list.remove(item)  # Remove the specified item
        setItems(new_list)  # Update our state

    def handleEdit(item):
        setNewItem(item)  # Set the new item value
        setEditItem(item)  # Set the edit item value

    return Form({'onSubmit': handleSubmit},
                Label({'htmlFor': 'newItem'},
                      "Edit Item: " if editItem else "Add Item: "
                      ),
                Input({'id': 'newItem',
                       'onChange': handleChange,
                       'value': newItem
                       }
                      ),
                Input({'type': 'submit'}),
                Ol(None,
                   ListItems({'items': items,
                              'handleDelete': handleDelete,
                              'handleEdit': handleEdit}
                             )
                   )
                )


render(App, None, 'root')
