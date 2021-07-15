========================
sphinx-packaging demo
========================

:pep:`503` is the specification for PyPI's ``/simple`` repository API, used by tools such as pip.

:pep:`503#normalized-names`

The :pep621:`name` is :pep:`normalized <503#normalized-names>` per :pep:`503`

:pep621:`version` must be a valid per :pep:`440`

:pep621:`requires-python` maps to :core-meta:`Requires-Python`

The project's :core-meta:`description` may have multiple lines.

A wheel's :core-meta:`supported platforms <Supported-Platform>` specify the OS and CPU for which the binary distribution was compiled.


Values in TOML must be one of the following types:

* :toml:`String`
* :toml:`Integer`
* :toml:`Float`
* :toml:`Boolean`
* :toml:`Offset Date-Time`
* :toml:`Local Date-Time`
* :toml:`Local Date`
* :toml:`Local Time`
* :toml:`Array`
* :toml:`Inline Table`

:toml:`Inline Tables <Inline Table>` must be on a single line.

Unlike in YAML, a :toml:`string` must be surrounded by quotation marks.

You can place multiple objects in an :toml:`array`.

The following xrefs are not indexed: :toml:`!Float` :toml:`array <!Array>`.

:pep:`621` defines the following fields in the ``[project]`` table:

* :pep621:`name`
* :pep621:`version`
* :pep621:`description`
* :pep621:`readme`
* :pep621:`requires-python`
* :pep621:`license`
* :pep621:`authors`
* :pep621:`maintainers`
* :pep621:`keywords`
* :pep621:`classifiers`
* :pep621:`urls`
* :pep621:`scripts`
* :pep621:`gui-scripts`
* :pep621:`entry-points`
* :pep621:`dependencies`
* :pep621:`optional-dependencies`
* :pep621:`dynamic`

:pep621:`authors and maintainers <authors/maintainers>` function the same; the difference is left up to the backend.

This PEP is invalid: :pep:`abc`
