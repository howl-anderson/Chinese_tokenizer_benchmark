#!/usr/bin/env python

import os

from jinja2 import Template

from config import corpus_registry

current_dir = os.path.dirname(os.path.abspath(__file__))

input_file = os.path.join(current_dir, 'README.tpl.md')
output_file = os.path.join(current_dir, 'README.md')

with open(input_file, encoding='utf_8') as input_fd, open(output_file, mode='w', encoding='utf_8') as output_fd:
    template = Template(input_fd.read())

    test_result = []

    for k, v in corpus_registry.items():
        markdown_table_file = os.path.join(current_dir, 'results', v + '.md')
        item = {
            'title': k,
            'markdown_table': open(markdown_table_file).read()
        }

        test_result.append(item)

    rendered_string = template.render(test_result=test_result)

    output_fd.write(rendered_string)
