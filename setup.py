import os
from setuptools import setup

import cht


with open("README.rst") as r:
    LONG_DESCRIPTION = r.read()

setup(
    name="cht",
    version=cht.VERSION,

    py_modules=["cht"],
    zip_safe=True,
    entry_points={
        "console_scripts": ["cht=cht:main"],
    },

    keywords="slack",
    description=(
        "Notify to the slack channel using the incoming webhook "
        "when the previous command has ended."),
    long_description=LONG_DESCRIPTION,
    url="https://github.com/suzuki-shunsuke/cht",
    license="MIT",
    author="Suzuki Shunsuke",
    author_email="suzuki.shunsuke.1989@gmail.com"
)
