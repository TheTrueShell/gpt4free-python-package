#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    "websocket-client",
    "requests",
    "tls-client",
    "pypasser",
    "names",
    "colorama",
    "curl_cffi",
    "streamlit==1.21.0",
    "selenium",
    "fake-useragent",
    "twocaptcha",
]

test_requirements = ['pytest>=3', ]

setup(
    author="Reza Shakeri",
    author_email='rzashakeri@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description=" decentralising the Ai Industry, free gpt-4/3.5 scripts through several reverse engineered api's ( poe.com, phind.com, chat.openai.com, writesonic.com, sqlchat.ai, t3nsor.com, you.com etc...)",
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='gpt4free',
    name='gpt4free',
    packages=find_packages(include=['gpt4free', 'gpt4free.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/rzashakeri/gpt4free',
    version='0.1.0',
    zip_safe=False,
)
