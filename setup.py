from setuptools import setup, find_packages
setup(
    name="shellify",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'click',
        'spotipy',
        'python-dotenv',
    ],
    entry_points={
        'console_scripts': [
            'shellify=src.main:cli',  # command=package.module:function
        ],
    },
)
