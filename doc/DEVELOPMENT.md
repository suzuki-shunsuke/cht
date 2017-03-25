# Development

## Requirement

* python 2

## Recommeded (Optional)

* [pyenv](https://github.com/pyenv/pyenv)
* [direnv](https://github.com/direnv/direnv)

https://github.com/direnv/direnv/wiki/Python#-pyenv

* [pip-tools](https://github.com/jazzband/pip-tools)

## Setup

### 1. Install python

If you use pyenv,

```
$ pyenv install 2.7.13
```

### 2. Install dependencies

```
$ pip install -r requirements.dev.txt
```

If you use pip-tools,

```
$ pip-sync requirements.dev.txt
```
