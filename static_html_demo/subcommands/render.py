"""
Create an html report of classification results.
"""

import os

from operator import itemgetter
from collections import defaultdict
from os import path
from ConfigParser import SafeConfigParser

from jinja2 import Environment, PackageLoader, Markup

from pipeline.utils import (make_local_copy, timestamp_now)


def build_parser(parser):
    parser.add_argument('-d', '--outdir', default='./report',
                        help='output directory for html')
    parser.add_argument('--title',
                        help=('Title string for index.html '
                              '(default: name of cwd)'))


def action(args):

    timestamp = timestamp_now()
    title = args.title or os.getcwd()
    outdir = args.outdir

    # make a local copies of css and js files
    bootstrap_css = make_local_copy(outdir, 'css', 'bootstrap.css')
    jquery_js = make_local_copy(outdir, 'js', 'jquery-1.11.2.min.js')
    bootstrap_js = make_local_copy(outdir, 'js', 'bootstrap.js')
    js_files = [jquery_js, bootstrap_js]

    env = Environment(loader=PackageLoader('pipeline', 'templates'))
    # env.globals = globals()

    with open(path.join(outdir, 'index.html'), 'w') as f:
        f.write(env.get_template('specimen.html').render(
            title=title,
            bootstrap_css=bootstrap_css,
            js_files=js_files,
            # footers=versions,
            # timestamp=timestamp,
            # groups=specimen_groups,
            # accordian_threshold=args.hide_threshold,
            # limits=dict(limits.items('analysis_qa')),
            # max_num=max_num,
            # navigation=[('index.html', titlestr)],
            # img_tag=img_tag,
            # ann=ann,
        ))
