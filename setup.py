import re
from setuptools import setup


with open('ipapp/__init__.py') as ver_file:
    ver = re.compile(r".*__version__ = '(.*?)'", re.S).match(ver_file.read())
    if ver is not None:
        version = ver.group(1)
    else:
        version = '0.0.0'

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.read()
with open('requirements_postgres.txt') as requirements_file:
    requirements_postgres = requirements_file.read()
with open('requirements_rabbitmq.txt') as requirements_file:
    requirements_rabbit = requirements_file.read()


setup(
    name='ipapp',
    version=str(version),
    description='InPlan application framework',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Operating System :: Unix',
        'Operating System :: POSIX :: Linux',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
    ],
    author='InPlat',
    url='https://gitlab.app.ipl/inplat/ipapp',
    packages=['ipapp'],
    python_requires='>=3.7',
    install_requires=requirements.split('\n'),
    extras_require={
        'postgres': requirements_postgres.split('\n'),
        'rabbitmq': requirements_rabbit.split('\n'),
    },
)
