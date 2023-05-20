import os
from itertools import product

from constants import ( 
    DISTRO_LIST,
    POETRY_VERSION_LIST,
    PYTHON_VERSION_LIST,
    WARNING_HEADER
)

def dockerfile_template(poetry_version, python_version, distro):
    template = f"""# {WARNING_HEADER}

FROM python:{python_version}-{distro}

ENV POETRY_VERSION={poetry_version} \\
    POETRY_NO_INTERACTION=1 \\
    POETRY_VIRTUALENVS_CREATE=false

RUN pip install "poetry==$POETRY_VERSION"

CMD ["python3"]
"""

    return template

for POETRY_VERSION, PYTHON_VERSION, DISTRO in product(POETRY_VERSION_LIST, PYTHON_VERSION_LIST, DISTRO_LIST):

    filename = f'{POETRY_VERSION}/python{PYTHON_VERSION}/{DISTRO}/Dockerfile'

    os.makedirs(os.path.dirname(filename), exist_ok=True)

    file = open(filename, "wt")
    file.write(dockerfile_template(
        POETRY_VERSION_LIST[POETRY_VERSION], 
        PYTHON_VERSION_LIST[PYTHON_VERSION], 
        DISTRO)
    )
    file.close()
