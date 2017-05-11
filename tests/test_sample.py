#!/usr/bin/python3
"""Demonstrate high quality docstrings.

Module-level docstrings appear as the first "statement" in a module. Remember,
that while strings are regular Python statements, comments are not, so an
inline comment may precede the module-level docstring.

After importing a module, you can access this special string object through the
``__doc__`` attribute; yes, it's actually available as a runtime attribute,
despite not being given an explicit name! The ``__doc__`` attribute is also
what is rendered when you call ``help()`` on a module, or really any other
object in Python.

You can also document a package using the module-level docstring in the
package's ``__init__.py`` file.

"""


def inc(param):
    """A template for unit testing.

    Remove me when adding the first test.
    """
    return param + 1


def test_answer():
    """A template for unit testing.

    Remove me when adding the first test.
    """
    assert inc(3) == 4
