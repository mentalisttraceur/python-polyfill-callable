Python ``callable`` polyfill
============================

Attempts to ensure the ``callable`` builtin is available.

Most Python versions have a native builtin function called ``callable``
which checks if the argument is a callable object.

This applies to all modern supported versions of CPython (including
stackless), PyPy, Jython, IronPython, MicroPython, PyPy.js, Brython,
and probably others, but there is a small handful of Python versions
where ``callable`` isn't implemented.

The concept behind this module is that it attempts to ensure that the
``callable`` builtin is available:

* On versions of Python where ``callable`` is already available,
  importing this doesn't break anything and leaves ``callable`` alone.

* On versions without a ``callable`` builtin, on import this will
  attempt to inject an equivalent implementation, so that code invoking
  ``callable`` continues to work.

* If your Python runtime has no ``callable`` builtin and this code is
  unable to polyfill it, it will raise a ``NotImplementedError``.


Versioning
----------

This library's version numbers follow the `SemVer 2.0.0 specification
<https://semver.org/spec/v2.0.0.html>`_.

The current version number is available in the variable ``__version__``
as is normal for Python modules.


Installation
------------

::

    pip install polyfill-callable


Usage
-----

Just make sure you run this before you run any other code that uses
``callable``:

.. code:: python

    import polyfill_callable

You can also catch ``NotImplementedError`` if you'd like to gracefully
handle the lack of ``callable``.

.. code:: python

    try:
        import polyfill_callable
    except NotImplementedError as error:
        # .. do something ..


Limitations
-----------

As of this writing on 2018-02-17, this module only has a ``callable``
polyfill for:

* The early CPython 3 versions that shipped without ``callable`` before
  it was added back in in CPython 3.2. There we can reimplement it using
  ``ctypes``, and polyfill it into the global namespace by using
  ``builtins`` (this, by the way, is a perfect example of why having the
  flexibility to inject names into the language environment in a truly
  global way is a good thing).

If there are other Python implementation versions where it would be
possible to support a polyfill, they might eventually be added here.
