# Copyright 2018 Alexander Kozhevnikov <mentalisttraceur@gmail.com>
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.


"""Attempts to ensure the ``callable`` builtin is available.

If your Python runtime has a ``callable`` builtin natively (almost
all implementation of Python do), importing this does nothing.

If your Python runtime has no ``callable`` builtin, on import this
will attempt to inject an equivalent implementation, so that code
invoking ``callable`` continues to work.

If your Python runtime has no ``callable`` builtin and this code
is unable to polyfill it, it will raise a ``NotImplementedError``.
"""


try:
    # Python 3 (and hopefully all future versions, indefinitely)
    import builtins
except ImportError:
    # Pre-Python 3
    try:
        import __builtin__ as builtins
    except ImportError:
        # Some implementations of Python don't expose builtins. On
        # those, we can just fall through to the final check.
        class _FakeBuiltins(object):
            # pylint: disable=too-few-public-methods
            callable = None
        builtins = _FakeBuiltins()

try:
    from ctypes import py_object as _py_object
    from ctypes import pythonapi as _pythonapi
    # pylint: disable=invalid-name
    _PyCallable_Check = _pythonapi.PyCallable_Check
except (ImportError, AttributeError):
    pass
else:
    def ctypes_callable(obj):
        """Return whether the object is callable (i.e., some kind of function).

        Note that classes are callable, as are instances of classes with a
        __call__() method.
        """
        return bool(_PyCallable_Check(_py_object(obj)))
    if not hasattr(builtins, 'callable'):
        builtins.callable = ctypes_callable


__all__ = ()
__version__ = '1.0.1'


try:
    # Calling `callable` on itself is the most compact sanity check.
    # It also handles implementations that define `callable` but
    # have it raise `NotImplementedError` when called.
    if not callable(callable):
        raise NotImplementedError('"callable" returns wrong result')
except NameError:
    raise NotImplementedError('"callable" polyfill not available')
except TypeError:
    raise NotImplementedError('"callable" defined but not callable')

# It might be worthwhile to have tests checking that `callable` behaves
# as expected more specifically, when called on other types of objects,
# and raise exceptions to indicate any bugs with enough granularity that
# a person importing it could easily decide whether to proceed or not.
#
# Such exceptions should inherit from `NotImplementedError` because this
# module is about assuring that `callable` is *available*, which implies
# *implemented correctly*.
#
# If you know of any Python implementation that successfully passes the
# above but has incorrect `callable` behavior, please let me know.
