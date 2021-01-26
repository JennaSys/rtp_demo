from pyreact import useState, render, createElement as el


def ListItem(props):
    item = props['item']
    handleDelete = props['handleDelete']
    handleEdit = props['handleEdit']

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


def ListItems(props):
    items = props['items']
    handleDelete = props['handleDelete']
    handleEdit = props['handleEdit']

    return [
        el(ListItem, {'key': item,
                      'item': item,
                      'handleDelete': handleDelete,
                      'handleEdit': handleEdit}
           ) for item in items]


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

    return el('form', {'onSubmit': handleSubmit},
              el('label', {'htmlFor': 'newItem'},
                 "Edit Item: " if editItem else "Add Item: "
                 ),
              el('input', {'id': 'newItem',
                           'onChange': handleChange,
                           'value': newItem
                           }
                 ),
              el('input', {'type': 'submit'}),
              el('ol', None,
                 el(ListItems, {'items': items,
                                'handleDelete': handleDelete,
                                'handleEdit': handleEdit}
                    )
                 )
              )


render(App, None, 'root')
