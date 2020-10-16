Python ``callable`` polyfill
============================

Attempts to ensure the ``callable`` builtin is available.

* On versions of Python where ``callable`` is already available,
  importing this doesn't break anything and leaves ``callable`` alone.

* On versions without a ``callable`` builtin, on import this will
  attempt to inject an equivalent implementation, so that code
  invoking ``callable`` continues to work.

* If your Python runtime has no ``callable`` builtin and this module
  is unable to polyfill it, it will raise a ``NotImplementedError``.


Versioning
----------

This library's version numbers follow the `SemVer 2.0.0
specification <https://semver.org/spec/v2.0.0.html>`_.


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

You can also catch ``NotImplementedError`` if you'd like to
gracefully handle the lack of ``callable``:

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
  it was added back in in CPython 3.2. There we can reimplement it
  using ``ctypes``, and polyfill it into the global namespace by using
  ``builtins``.

If there are other Python implementation versions where it would be
possible to support a polyfill, they might eventually be added here.
