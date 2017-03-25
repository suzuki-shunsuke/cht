import json
from setuptools import setup


with open("package.json") as r:
    VERSION = json.load(r)["version"]

setup(
    name="cht",
    version=VERSION,

    zip_safe=True,
    entry_points={
        "console_scripts": ["cht=main.main"],
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
