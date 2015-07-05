import os
import json

from tags import paragraph
from tags import link
from tags import linebreak
from tags import text

tags = {
    'pg': paragraph.function,
    'a': link.function,
    'br': linebreak.function,
    'text': text.function
}

class Page:
    def __init__(self, url="", content=[]):
        self.content = content
        self.render = ""
        self.url = url
        self.special_calls = {}
        
    def append_text(self, content):
        self.content.append(content)
        
    def error(self, message):
        self.render += 'Error: ' + message + '\n'
        
    def load_page(self, config):
        if not os.path.isdir(config.get_parameter('net_dir')):
            self.error('No net directory')
        else:
            abs_url = os.path.join(config.get_parameter('net_dir'), self.url)
            try:
                file = open(abs_url, "r")
            except (OSError, IOError, IsADirectoryError):
                self.error('404 - File not found')
                self.content = None
                return
                
            try:
                self.content = json.loads(file.read())
            except ValueError:
                self.error('Wrongly formatted JSON')
                self.content = None
                return
            
        
    def display_page(self, screen):
        special_info = { #Special info needed for correctly rendering page
            'number_of_links': 1
        }
        if self.content is not None: #no errors parsing
            for tag in self.content:
                self.render += tags[tag['tag']]['replace'](tag['content'], special_info)
                
                (special_call, special_info_bit) = tags[tag['tag']]['add_call'](tag['content'], special_info)
                special_info.update(special_info_bit)
                self.special_calls.update(special_call)
        screen.addstr(self.render)
        
    def get_special_calls(self):
        return self.special_calls
