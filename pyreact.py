# __pragma__ ('skip')
def require(lib):
    return lib

class document:
    getElementById = None
    addEventListener = None
# __pragma__ ('noskip')


# Load React and ReactDOM JavaScript libraries into local namespace
React = require('react')
ReactDOM = require('react-dom')

# Map React javaScript objects to Python identifiers
createElement = React.createElement
useState = React.useState


def react_component(component):
    def react_element(props, *children):
        return createElement(component, props, *children)

    return react_element


Form = react_component('form')
Label = react_component('label')
Input = react_component('input')
Ol = react_component('ol')
Li = react_component('li')
Button = react_component('button')
Div = react_component('div')
Span = react_component('span')


def render(root_component, props, container):
    """Loads main react component into DOM"""

    def main():
        ReactDOM.render(
            React.createElement(root_component, props),
            document.getElementById(container)
        )

    document.addEventListener('DOMContentLoaded', main)
