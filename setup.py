from setuptools import setup

setup(
    name='jarv',
    packages=['jarv'],
    include_package_data=True,
    install_requires=[
        'flask', 'flask-security', 'flask-sqlalchemy', 'bcrypt', 'psycopg2'
    ],
)
