from setuptools import setup

requirements = [
    'requests',
    'slackclient'
]

setup(
    name='burpa',
    packages=['burpa'],
    scripts=['burpa/burpa.py'],
    console=(['burpa']),
    version=1.0,
    python_requires='>=2.7.10',
    install_requires=requirements
)