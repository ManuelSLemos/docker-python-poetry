from itertools import product

from constants import ( 
    DISTRO_LIST,
    DOCKER_REGISTRY_NAME,
    POETRY_VERSION_LIST,
    PYTHON_VERSION_LIST
)

for POETRY_VERSION, PYTHON_VERSION, DISTRO in product(POETRY_VERSION_LIST, PYTHON_VERSION_LIST, DISTRO_LIST):
    tags = []

    POETRY_FULL_VERSION = POETRY_VERSION_LIST[POETRY_VERSION]
    PYTHON_FULL_VERSION = PYTHON_VERSION_LIST[PYTHON_VERSION]

    filename = f'{POETRY_VERSION}/python{PYTHON_VERSION}/{DISTRO}/Dockerfile'

    tags.append( f'{POETRY_FULL_VERSION}-python{PYTHON_FULL_VERSION}-{DISTRO}' )
    tags.append( f'{POETRY_FULL_VERSION}-python{PYTHON_VERSION}-{DISTRO}' )
    tags.append( f'{POETRY_FULL_VERSION}-python3-{DISTRO}' )
    tags.append( f'{POETRY_FULL_VERSION}-{DISTRO}' )
    tags.append( f'{POETRY_FULL_VERSION}-python{PYTHON_FULL_VERSION}' )
    tags.append( f'{POETRY_FULL_VERSION}-python{PYTHON_VERSION}' )
    tags.append( f'{POETRY_FULL_VERSION}-python3' )

    tags.append( f'{POETRY_VERSION}-python{PYTHON_FULL_VERSION}-{DISTRO}' )
    tags.append( f'{POETRY_VERSION}-python{PYTHON_VERSION}-{DISTRO}' )
    tags.append( f'{POETRY_VERSION}-python3-{DISTRO}' )
    tags.append( f'{POETRY_VERSION}-{DISTRO}' )
    tags.append( f'{POETRY_VERSION}-python{PYTHON_FULL_VERSION}' )
    tags.append( f'{POETRY_VERSION}-python{PYTHON_VERSION}' )
    tags.append( f'{POETRY_VERSION}-python3' )

    if POETRY_VERSION == '1.5' and PYTHON_VERSION == '3.11':
        if DISTRO == 'alpine3.18':
            tags.append( f'{POETRY_FULL_VERSION}-python{PYTHON_FULL_VERSION}-alpine' )
            tags.append( f'{POETRY_FULL_VERSION}-python{PYTHON_VERSION}-alpine' )
            tags.append( f'{POETRY_FULL_VERSION}-python3-alpine' )
            tags.append( f'{POETRY_FULL_VERSION}-alpine' )
            tags.append( f'{POETRY_VERSION}-python{PYTHON_FULL_VERSION}-alpine' )
            tags.append( f'{POETRY_VERSION}-python{PYTHON_VERSION}-alpine' )
            tags.append( f'{POETRY_VERSION}-python3-alpine' )
            tags.append( f'{POETRY_VERSION}-alpine' )

        if DISTRO == 'slim-bullseye':
            tags.append( f'{POETRY_FULL_VERSION}-python{PYTHON_FULL_VERSION}-slim' )
            tags.append( f'{POETRY_FULL_VERSION}-python{PYTHON_VERSION}-slim' )
            tags.append( f'{POETRY_FULL_VERSION}-python3-slim' )
            tags.append( f'{POETRY_FULL_VERSION}-slim' )
            tags.append( f'{POETRY_VERSION}-python{PYTHON_FULL_VERSION}-slim' )
            tags.append( f'{POETRY_VERSION}-python{PYTHON_VERSION}-slim' )
            tags.append( f'{POETRY_VERSION}-python3-slim' )
            tags.append( f'{POETRY_VERSION}-slim' )

        if DISTRO == 'bullseye':
            tags.append(f'{POETRY_VERSION}')
            tags.append(f'{POETRY_FULL_VERSION}')
            tags.append('latest')
    

    for tag in tags: 
        build = f'docker build . -t {DOCKER_REGISTRY_NAME}:{tag} -f {filename}'
        push = f'docker push {DOCKER_REGISTRY_NAME}:{tag}'

        file = open('push.sh', "a")
        file.write(f'{build}\n{push}\n')
        file.close()

        




