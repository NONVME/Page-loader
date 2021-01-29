![Python CI](https://github.com/NONVME/python-project-lvl3/workflows/Python%20CI/badge.svg?branch=main)
[![Maintainability](https://api.codeclimate.com/v1/badges/3aef99c8389e3c89abf9/maintainability)](https://codeclimate.com/github/NONVME/python-project-lvl3/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/3aef99c8389e3c89abf9/test_coverage)](https://codeclimate.com/github/NONVME/python-project-lvl3/test_coverage)
[![Actions Status](https://github.com/NONVME/python-project-lvl3/workflows/hexlet-check/badge.svg)](https://github.com/NONVME/python-project-lvl3/actions)

# Page-loader
A page-loader is a cli tool that downloads the requested web page with local resources.

This is a third level project. created as part of the [Hexlet](https://ru.hexlet.io/) training course to prepare a Python Web developer.

## Features

- Enter the web address and the page-loader will download it.
- The tool downloads all the resources listed on the page and changes the page so that it starts referencing local versions.
- Usage as CLI util or library function
- Supports logging

## Installation

```bash
git clone https://github.com/NONVME/python-project-lvl3.git

cd python-project-lvl3

make package-install
```


## Usage

### As library function

```python
from page-loader import download

download(url, path_to_save)
```

### As CLI util

```bash
usage: page-loader [-h] [-o OUTPUT] url

Web scrapper

positional arguments:
  url

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        set output full-path
```

### Usage examples

#### Installation


## License

[MIT](https://choosealicense.com/licenses/mit/)
