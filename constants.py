DISTRO_LIST = [
    'bullseye',
    'slim-bullseye',
    'buster',
    'slim-buster',
    'alpine3.18',
    'alpine3.17',
]

DOCKER_REGISTRY_NAME = 'manuelslemos/docker-python-poetry'

POETRY_VERSION_LIST = {
    '1.4': '1.4.2',
    '1.5': '1.5.0'
}

PYTHON_VERSION_LIST = {
    '3.7': '3.7.16',
    '3.8': '3.8.16',
    '3.9': '3.9.16',
    '3.10': '3.10.11',
    '3.11': '3.11.3',
    '3.12-rc': '3.12.0a7'  
}

URL_FORKED_VERSION = 'https://raw.githubusercontent.com/docker-library/python/090760cb09d6061d973a68d7fa148cbbde100cb9/versions.json'

WARNING_HEADER = f'''#
# NOTE: THIS DOCKERFILE IS GENERATED VIA "apply-templates.py"
#
# PLEASE DO NOT EDIT IT DIRECTLY.
#
'''