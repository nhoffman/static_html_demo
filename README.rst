=================================================================
a demo for building static html reports with Jinja2 and Bootstrap
=================================================================

installation
============

This is just a demo, most easily run locally::

  git clone ...
  cd static_html_demo
  virtualenv shd-env
  source shd-env/bin/activate
  pip install -r requirements.txt
  ./shd.py -h


architecture
============

This project has the following subdirectories:

* ``dev`` - development tools not essential for the primary functionality of the application.
* ``doc`` - files related to project documentation.
* ``static_html_demo`` - the Python package implementing most of the project functionality.
* ``testfiles`` - files and data used for testing.
* ``tests`` - subpackage implementing unit tests.

execution
=========

The ``shd.py`` script provides the user interface, and uses standard
UNIX command line syntax. Note that for development, it is convenient
to run this script from within the project directory by specifying the
relative path to the script::

    % ./shd.py --help


versions
========

The package version is defined using ``git describe --tags --dirty``
(see http://git-scm.com/docs/git-describe for details).  The version
information is updated and saved in the file ``/data/ver/static_html_demo``
when ``setup.py`` is run (on installation, or even by executing
``python setup.py -h``). Run ``python setup.py check_version`` to make
sure that the stored version matches the output of ``git
describe --tags --dirty``.

Add a tag like this::

  git tag -a -m 'version 0.1.0' 0.1.0


unit tests
==========

Unit tests are implemented using the ``unittest`` module in the Python
standard library. The ``tests`` subdirectory is itself a Python
package that implements the tests. All unit tests can be run like this::

    % python setup.py test

A single unit test can be run by referring to a specific module,
class, or method within the ``tests`` package using dot notation::

    % python setup.py test --test-suite tests.test_utils

license
=======

Copyright (c) 2016 Noah Hoffman

Released under the MIT License:

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
