===========
Usage
===========

.. extensions:: sphinx_packaging


Directives
--------------


.. rst:directive:: .. tconf:: name

	Used to document a TOML configuration field, for example in :pep:`621` metadata.

	.. rst:directive:option:: type
		:type: string

		Indicates the field's type.

	.. rst:directive:option:: required
		:type: flag

		Indicates the whether a value is required for the field.

	.. rst:directive:option:: default
		:type: string

		Indicates the default value for the field.

	.. rst:directive:option:: noindex
		:type: flag

		Disables the index entry and cross-referencing for this field.


	:bold-title:`Examples:`

	.. rest-example::

		.. tconf:: project.name
			:type: :toml:`String`
			:required: True

			The name of the project.

		.. tconf:: project.version
			:type: :toml:`String`
			:required: True

			The version of the project as supported by :pep:`440`.

		.. tconf:: description
			:type: :toml:`String`
			:default: ``'This is the description'``
			:required: False

			A short summary description of the project.


Roles
--------

:mod:`sphinx_packaging` provides the following roles:


.. rst:role:: pep

	Creates a cross-reference to a `Python Enhancement Proposal`_.

	The text "PEP NNN" is inserted into the document,
	and with supported builders is a hyperlink to the online copy of the specified PEP.
	This role also generates an appropriate index entry.

	You can link to a specific section by writing :samp:`:pep:\`number#anchor\``.

	A custom title can also be added to the link by writing :samp:`:pep:\`title <number#anchor>\``.
	Unlike the version of this directive which ships with Sphinx,
	the link is not shown in bold when there is a custom title.

	:bold-title:`Examples:`

	.. rest-example::

		:pep:`621`

		:pep:`503#normalized-names`

		.. seealso:: The :pep:`specification <427>` for wheels.


.. rst:role:: pep621

	Creates a cross-reference to a section in :pep:`621`,
	typically the name of a field in ``pyproject.toml``.

	The title of the directive (either implicit, :samp:`:pep621:\`title\``,
	or explicit :samp:`:pep621:\`title <target>\``) is inserted into the document.
	With supported builders is a hyperlink to the specified heading in the online copy of the PEP.
	This role also generates an appropriate index entry.

	:bold-title:`Examples:`

	.. rest-example::

		The :pep621:`name` field must be provided and cannot be :pep621:`dynamic`.

		:pep621:`Version <version>` may be required by some backend,
		but can be determined dynamically by others.

		:pep621:`authors` and :pep621:`maintainers` both point to the same section.


.. rst:role:: core-meta

	Creates a cross-reference to a field in the Python `core metadata`_.

	The title of the directive (either implicit, :samp:`:core-meta:\`title\``,
	or explicit :samp:`:core-meta:\`title <target>\``) is inserted into the document.
	With supported builders is a hyperlink to the specified field in the specification
	on `packaging.python.org`_.
	This role also generates an appropriate index entry.

	:bold-title:`Examples:`

	.. rest-example::

		:core-meta:`Supported-Platform (Multiple Use) <Supported-Platform>` specifies the OS and CPU
		for which the binary distribution was compiled.

		The project's :core-meta:`description` may have multiple lines.

		:pep621:`requires-python` in ``pyproject.toml`` maps to :core-meta:`Requires-Python`


.. rst:role:: toml

	Creates a cross-reference to a section in the `TOML specification`_.

	The title of the directive (either implicit, :samp:`:toml:\`title\``,
	or explicit :samp:`:toml:\`title <target>\``) is inserted into the document.
	With supported builders is a hyperlink to section in the web version of the specification.
	This role also generates an appropriate index entry.

	:bold-title:`Examples:`

	.. rest-example::

		TOML's :toml:`string` type accepts either single or double quotes.

		:toml:`Inline Tables <Inline Table>` must be on a single line.

		There are four date/time types in TOML:

		* :toml:`Offset Date-Time`
		* :toml:`Local Date-Time`
		* :toml:`Local Date`
		* :toml:`!Local Time`


	The last xref will not appear in the index because the target is prefixed with a ``!``.
	This also works when there is an explicit title:

	.. rest-example::

		The following xrefs are not indexed: :toml:`!Float`, :toml:`array <!Array>`.

	.. only:: html

		:ref:`Click here <genindex>` to see the index.


.. rst:role:: tconf

	Role which provides a cross-reference to a :rst:dir:`tconf` directive.


	:bold-title:`Examples:`

	.. rest-example::

		:tconf:`project.name` and :tconf:`~project.version` are required.
		Some backends may be able to determine a value for :tconf:`version` dynamically.

		:tconf:`description` will be displayed this towards the top of the project page on PyPI.

		Links can also be written with a shorter name: :tconf:`~.name`.


.. latex:clearpage::


Configuration
----------------

.. confval:: toml_spec_version
	:type: string
	:required: False
	:default: 1.0.0

	The version of the `TOML specification`_ to link to.

	For example, this documentation links to ``v0.5.0`` with the following setting:

	.. code-block:: python

		# conf.py
		toml_spec_version = "0.5.0"


.. confval:: tconf_show_full_name
	:type: :py:class:`bool`
	:required: False
	:default: True

	Whether to show the full name for field.

	For example, with ``tconf_show_full_name = True``:

	.. tconf:: project.description
		:type: :toml:`String`
		:noindex:

	And with ``tconf_show_full_name = False``:

	.. tconf:: description
		:type: :toml:`String`
		:noindex:


.. _Python Enhancement Proposal: https://www.python.org/dev/peps/
.. _core metadata: https://packaging.python.org/specifications/core-metadata/
.. _packaging.python.org: https://packaging.python.org
.. _TOML specification: https://toml.io/en/v1.0.0
