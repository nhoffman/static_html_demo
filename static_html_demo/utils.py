import os
import gzip
import logging
import shutil
import sys
from datetime import datetime

try:
    from bz2 import BZ2File
except ImportError, err:
    BZ2File = lambda x, *args, **kwargs: sys.exit(err)

from os import path

from static_html_demo import package_data

log = logging.getLogger(__name__)


def cast(val):
    """Attempt to coerce `val` into a numeric type, or a string stripped
    of whitespace.

    """

    for func in [int, float, lambda x: x.strip(), lambda x: x]:
        try:
            return func(val)
        except ValueError:
            pass


def mkdir(dirpath, clobber=False):
    """
    Create a (potentially existing) directory without errors. Raise
    OSError if directory can't be created. If clobber is True, remove
    dirpath if it exists.
    """

    if clobber:
        shutil.rmtree(dirpath, ignore_errors=True)

    try:
        os.mkdir(dirpath)
    except OSError:
        pass

    if not path.exists(dirpath):
        raise OSError('Failed to create %s' % dirpath)

    return dirpath


class Opener(object):
    """Factory for creating file objects. Transparenty opens compressed
    files for reading or writing based on suffix (.gz and .bz2 only).

    Example::

        with Opener()('in.txt') as infile, Opener('w')('out.gz') as outfile:
            outfile.write(infile.read())
    """

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.writable = 'w' in kwargs.get('mode', args[0] if args else 'r')

    def __call__(self, obj):
        if obj is sys.stdout or obj is sys.stdin:
            return obj
        elif obj == '-':
            return sys.stdout if self.writable else sys.stdin
        else:
            __, suffix = obj.rsplit('.', 1)
            opener = {'bz2': BZ2File,
                      'gz': gzip.open}.get(suffix, open)
            return opener(obj, *self.args, **self.kwargs)


def make_local_copy(outdir, subdir, fname):
    """Copy fname from package data to outdir/subdir (creating dir if
    necessary), and return the path to the copy of fname relative to
    outdir.

    """

    destdir = path.join(outdir, subdir)
    mkdir(destdir)
    shutil.copyfile(package_data(fname), path.join(destdir, fname))
    return path.join(subdir, fname)


def include_file(outdir, fname):
    mkdir(outdir)
    dest = path.join(outdir, path.basename(fname))
    shutil.copyfile(fname, dest)
    return path.join(path.basename(outdir), path.basename(fname))


def timestamp_now():
    """
    Produce a string with date and time information for a report
    """
    return datetime.now().strftime("%A, %B %d, %Y, %I:%M %p")
