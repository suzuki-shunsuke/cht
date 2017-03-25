from setuptools import setup

import cht


setup(
    name="cht",
    version=cht.VERSION,

    py_modules=["cht"],
    zip_safe=True,
    entry_points={
        "console_scripts": ["cht=cht:main"],
    },

    author="Suzuki Shunsuke",
    author_email="suzuki.shunsuke.1989@gmail.com",
    description=(
        "Notify to the slack channel using the incoming webhook "
        "when the previous command has ended."),
    license="MIT",
    keywords="slack",
    url="https://github.com/suzuki-shunsuke/cht"
)
