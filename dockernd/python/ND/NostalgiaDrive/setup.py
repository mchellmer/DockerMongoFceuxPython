from setuptools import setup

setup(
    name='nd',
    py_modules=['nd'],
    version='1.0.0',
    description='user friendly emulation game selection',
    license="MIT",
    author='Mark Hellmer',
    author_email='mchellmer@gmail.com',
    install_requires=['tkinter', 'nltk', 'pymongo'],
    scripts=[]
)
