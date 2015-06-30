def replace(msg, special_info):
    return msg + '\n\n'

def add_call(content, special_info):
    return ({}, special_info)

function = {
    'replace': replace,
    'add_call': add_call
}
