import re
import os


def download(url, output):
    file_name = generate_name(url, output)
    return file_name


def generate_name(url, output):
    url = re.sub(r'\W', '-', re.sub(r'^([a-zA-Z]+):\/\/', '', url))
    return os.path.join(output, url + '.html')
