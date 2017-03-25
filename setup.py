import json
from pkg_resources import resource_string
from setuptools import setup


VERSION = json.loads(resource_string(__name__, "package.json"))["version"]

setup(
    name="cht",
    version=VERSION,
    data_files=[("", ["package.json"])],

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
