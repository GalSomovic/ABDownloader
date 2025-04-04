from fasthtml.common import *

app,rt = fast_app()

def mk_input(): return Input(id='command', placeholder="type a command here", value="", hx_swap_oob="true")

def create_chat_message(role, content, msg_num):
    text_color = '#1F2937'
    match role:
        case 'system': color = '#8B5CF6'
        case 'user': color = "#F000B8"
        case _: color = "#37CDBE"

    # msg 0 = left, msg 1 = right, msg 2 = left, etc.
    alignment = 'flex-end' if msg_num % 2 == 1 else 'flex-start'

    message = Div(Div(
            Div(# Shows the Role
                Strong(role.capitalize()),
                style=f"color: {text_color}; font-size: 0.9em; letter-spacing: 0.05em;"),
            Div(# Shows content and applies font color to stuff other than syntax highlighting
                Style(f".marked *:not(code):not([class^='hljs']) {{ color: {text_color} !important; }}"),
                Div(content),
                style=f"margin-top: 0.5em; color: {text_color} !important;"),
            # extra styling to make things look better
            style=f"""
                margin-bottom: 1em; padding: 1em; border-radius: 24px; background-color: {color};
                max-width: 70%; position: relative; color: {text_color} !important; """),
        style=f"display: flex; justify-content: {alignment};")

    return message


@rt('/')
def get(): return Div(P('Hello World!'), hx_get="/change")

serve()