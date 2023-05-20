import json

from urllib.request import urlopen

from constants import ( 
    POETRY_VERSION_LIST,
    URL_FORKED_VERSION
)

raw_forked_version = urlopen( URL_FORKED_VERSION )
json_forked_version = json.loads( raw_forked_version.read() )

version = {}

for POETRY_VERSION in POETRY_VERSION_LIST.keys():

    POETRY_FULL_VERSION = POETRY_VERSION_LIST[POETRY_VERSION]

    version[POETRY_VERSION] = {
        'python': json_forked_version,
        'version': POETRY_FULL_VERSION
    }

if __name__ == "__main__":
    
    file = open('version.json', "wt")
    file.write(json.dumps(version, indent = 4))
    file.close()