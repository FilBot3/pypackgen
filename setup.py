""" setuptools setup.py
"""

import setuptools


with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()


setuptools.setup(
    name="pypackgen",
    version="0.0.1",
    author="Phillip Dudley",
    author_email="Predatorian3@gmail.com",
    description="A Python Package to generate Python Packages like I want \
    them.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/Predatorian3/pypackgen",
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    test_suite='test.pypackgen',
    tests_require=[
        "autopep8",
        "pycodestyle",
        "pylint",
        "pytest",
        "pytest-codestyle",
        "pytest-pylint",
        "pytest-runner",
    ],
    install_requires=[
        "click",
        "jinja2",
    ],
    entry_points={
        'console_scripts': [
            'pypackgener = pypackgen_scripts.scripts.executable:cli'
        ],
    },
)
