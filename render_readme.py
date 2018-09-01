#!/usr/bin/env python

import os

from jinja2 import Template

from config import corpus_registry

current_dir = os.path.dirname(os.path.abspath(__file__))

input_file = os.path.join(current_dir, 'README.tpl.md')
output_file = os.path.join(current_dir, 'README.md')


def get_file_content(input_file):
    with open(input_file) as fd:
        return fd.read()


with open(input_file, encoding='utf_8') as input_fd, open(output_file, mode='w', encoding='utf_8') as output_fd:
    template = Template(input_fd.read())

    test_result = []

    for k, v in corpus_registry.items():
        markdown_table_file = os.path.join(current_dir, 'results', 'performance', v + '.md')
        item = {
            'title': k,
            'markdown_table': get_file_content(markdown_table_file)
        }

        test_result.append(item)

    # read other files
    other_template_variable = {}
    other_files_dir = os.path.join(current_dir, 'results', 'others')
    for info_file in os.listdir(other_files_dir):
        variable_name = os.path.splitext(info_file)[0]
        info_file_path = os.path.join(other_files_dir, info_file)
        if os.path.isfile(info_file_path):
            other_template_variable[variable_name] = get_file_content(info_file_path)

    rendered_string = template.render(test_result=test_result, **other_template_variable)

    output_fd.write(rendered_string)
