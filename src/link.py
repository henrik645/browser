def replace(msg, special_info):
    return '[' + str(special_info['number_of_links']) + ']'
    
def add_call(content, special_info):
    special_call = {str(special_info['number_of_links']): content}
    special_info['number_of_links'] += 1
    return (special_call, special_info)
    
function = {
    'add_call': add_call,
    'replace': replace
}
