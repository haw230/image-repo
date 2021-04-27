from setuptools import setup

setup(
    name="my_project",
    version="0.1.0",
    packages=["my_project"],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        image_repo=image_repo.main:main
    ''',
)