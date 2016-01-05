"""
Create the index page.
"""

import os
from os import path
import subprocess
import csv

from jinja2 import Environment, PackageLoader

from static_html_demo.utils import (make_local_copy, timestamp_now,
                                    mkdir, Opener, include_file)


def get_versions():
    output = subprocess.check_output(['pip', 'freeze'])
    return dict([line.strip().split('==')
                 for line in output.splitlines() if line.strip()])


def build_parser(parser):
    parser.add_argument('-d', '--outdir', default='./report',
                        help='output directory for html [%(default)s]')
    parser.add_argument('--title',
                        help=('Title string for index.html '
                              '(default: name of cwd)'))
    parser.add_argument('--text', type=Opener(), default='testfiles/lorem.txt',
                        help='Some text to display [%(default)s]')
    parser.add_argument('--table', type=Opener(),
                        default='testfiles/western_states.csv',
                        help='A table in csv format [%(default)s]')
    parser.add_argument('--img', nargs='*', help='path to one or more images')
    parser.add_argument('--ncol', type=int, default=4,
                        help='number of columns for arranging images [%(default)s]')


def action(args):

    timestamp = timestamp_now()
    title = args.title or os.getcwd()
    outdir = args.outdir
    mkdir(outdir)

    # make a local copies of css and js files
    bootstrap_css = make_local_copy(outdir, 'css', 'bootstrap.css')
    jquery_js = make_local_copy(outdir, 'js', 'jquery-1.11.2.min.js')
    bootstrap_js = make_local_copy(outdir, 'js', 'bootstrap.js')
    js_files = [jquery_js, bootstrap_js]

    versions = get_versions()
    text = args.text.read()
    table = csv.reader(args.table)
    # has the side effect of copying files into place
    images = [include_file(path.join(outdir, 'img'), img)
              for img in args.img] if args.img else None

    env = Environment(loader=PackageLoader('static_html_demo', 'templates'))
    # env.globals = globals()

    with open(path.join(outdir, 'index.html'), 'w') as f:
        f.write(env.get_template('index.html').render(
            title=title,
            bootstrap_css=bootstrap_css,
            js_files=js_files,
            footers=versions,
            timestamp=timestamp,
            text=text,
            table=table,
            images=images,
            ncol=args.ncol,
            navigation=[('index.html', 'home')],
        ))
