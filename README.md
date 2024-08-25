# Syft Documentation Guide

To build the documentation the easiest thing to do is to use `tox`.
This will automatically install the environment needed for the documentation each time you build it.

## Build the documentation

Install `tox` with:

```
pip install tox
```

then navigate to `meta/` and run the following:

```
tox -e docs-update
```

this will install the necessary environment the first time, then build the documentation for you.

## Preview live documentation

```
tox -e docs-live
```
