from pyreact import useState, render, react_component
from pyreact import Form, Label, Input, Ol, Li, Button


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

    @react_component
    def ListItem(props):
        item = props['item']

        return Li(None,
                  item + " ",
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
        return [ListItem({'key': item, 'item': item}) for item in items]

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
                   ListItems(None)
                   )
                )


render(App, None, 'root')
