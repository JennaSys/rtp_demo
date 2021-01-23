from pyreact import useState, render, createElement as el


def App():
    newItem, setNewItem = useState("")
    editItem, setEditItem = useState("")
    items, setItems = useState([])

    def handleSubmit(event):
        event.preventDefault()
        if len(editItem) > 0:  # In edit mode
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

    def ListItem(props):
        item = props['item']

        return el('li', None,
                  props['item'] + " ",
                  el('button', {'type': 'button',
                                'onClick': lambda: handleDelete(item)
                                }, "Delete"
                     ),
                  el('button', {'type': 'button',
                                'onClick': lambda: handleEdit(item)
                                }, "Edit"
                     ),
                  )

    def ListItems():
        return [el(ListItem, {'key': item, 'item': item}) for item in items]

    return el('form', {'onSubmit': handleSubmit},
              el('label', {'htmlFor': 'newItem'},
                 "Add Item: " if len(editItem) == 0 else "Edit Item: "
                 ),
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
