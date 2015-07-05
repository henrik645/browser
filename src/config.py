import json
import sys
import os

from exit import exit

class Config:
    def __init__(self, contents):
        self.contents = contents

    def get_parameter(self, name):
        if name in self.contents:
            return self.contents[name]
        else:
            error("get_parameter: no such parameter in config: " + name)
 
def error(message):
    print("config: " + message, file=sys.stderr)
    exit(code=1)

def get_config():
    config = search_for_config()
    if config is not None:
        return config
    else:
        error("get_config: no valid config file found")

def search_for_config():
    config = None
    for location in os.curdir, os.path.expanduser("~"), "/etc/pybrowser", os.environ.get("PYBROWSER_CONF"):
        if location is None:
            break
        try: 
            with open(os.path.join(location, "config.json")) as source:
                try:
                    config_contents = json.loads(source.read())
                    config = Config(config_contents)
                except ValueError:
                    pass
        except (IOError, OSError, IsADirectoryError):
            pass

    return config
