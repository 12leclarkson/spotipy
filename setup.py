from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

test_reqs = [
    'mock==2.0.0'
]

doc_reqs = [
    'Sphinx>=1.5.2'
]

extra_reqs = {
    'doc': doc_reqs,
    'test': test_reqs
}

setup(
    name='spotipy',
    version='2.18.0',
    description='A light weight Python library for the Spotify Web API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="lc3817",
    author_email="lc3817@ic.ac.uk",
    url='https://spotipy.readthedocs.org/',
    install_requires=[
        'requests>=2.25.0',
        'six>=1.15.0',
        'urllib3>=1.26.0'
    ],
    tests_require=test_reqs,
    extras_require=extra_reqs,
    license='LICENSE',
    packages=['spotipy'])
