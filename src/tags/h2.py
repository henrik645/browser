def replace(text, special_info):
    return text.upper() + '\n' + '=' * len(text) + '\n'

def add_call(content, special_info):
    return ({}, special_info)

function = {
    'replace': replace,
    'add_call': add_call
}
