from setuptools import setup, find_packages

setup(
    name='mch_api',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        "aniso8601==8.0.0",
        "click==7.1.2",
        "Flask==1.1.2",
        "Flask-RESTful==0.3.8",
        "Jinja2==2.11.2",
        "flask-mysqldb==0.2.0",
        "pandas>=1.2.2",
        "markdown==2.6.11"
    ]
)