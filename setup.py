from setuptools import setup, find_packages

setup(
    name='Guilded_Rose',
    version='1.0',
    description='Proyecto API del negocio de la tienda Guilded Rose de Ollivanders',
    author='Sergio Gonzalez Barde y Antoni Pizarro Gayá',
    url='https://github.com/AntoniPizarro/API_PY_Ollivanders.git',
    packages=find_packages(exclude=('test', '.pytest_cache', '__pycache__')),
    python_requires='>=3.6',
    install_requires=[
        'astroid==2.4.2', 'atomicwrites==1.4.0', 'attrs==20.3.0', 'certifi==2020.11.8', 'chardet==3.0.4', 'click==7.1.2', 'colorama==0.4.4', 'curl==0.0.1', 'dnspython==1.16.0', 'email-validator==1.1.2', 'Flask==1.1.2', 'Flask-Cors==3.0.10', 'Flask-RESTful==0.3.8', 'Flask-WTF==0.14.3', 'idna==2.10', 'iniconfig==1.1.1', 'isort==5.6.4', 'itsdangerous==1.1.0', 'Jinja2==2.11.3', 'lazy-object-proxy==1.4.3', 'MarkupSafe==1.1.1', 'mccabe==0.6.1', 'mongoengine==0.23.0', 'MouseInfo==0.1.3', 'packaging==20.4', 'pluggy==0.13.1', 'py==1.9.0', 'PyAutoGUI==0.9.52', 'PyGetWindow==0.0.9', 'pylint==2.6.0', 'PyMsgBox==1.0.9', 'PyMySQL==1.0.2', 'pynput==1.7.2', 'pyparsing==2.4.7', 'pyperclip==1.8.1', 'PyRect==0.1.4', 'PyScreeze==0.1.26', 'PySimpleGUI==4.32.1', 'pytest==6.1.2', 'PyTweening==1.0.3', 'requests==2.25.0', 'six==1.15.0', 'urllib3==1.26.2', 'Werkzeug==1.0.1', 'wrapt==1.12.1', 'WTForms==2.3.3'
    ]
)