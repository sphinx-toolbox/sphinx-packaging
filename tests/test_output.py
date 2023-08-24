# stdlib
import re
import shutil

# 3rd party
import bs4.element  # type: ignore[import]
import pytest
from bs4 import BeautifulSoup
from domdf_python_tools.paths import PathPlus
from domdf_python_tools.stringlist import StringList
from sphinx.application import Sphinx
from sphinx_toolbox.testing import HTMLRegressionFixture, LaTeXRegressionFixture


@pytest.fixture()
def doc_root(tmp_pathplus: PathPlus) -> None:
	doc_root = tmp_pathplus.parent / "test-packaging"
	doc_root.maybe_make()
	(doc_root / "conf.py").write_lines([
			"extensions = ['sphinx_packaging']",
			"toml_spec_version = '0.5.0'",
			])

	shutil.copy2(PathPlus(__file__).parent / "index.rst", doc_root / "index.rst")


@pytest.mark.usefixtures("doc_root")
@pytest.mark.sphinx("html", testroot="test-packaging")
def test_build_example(app: Sphinx) -> None:
	app.build()
	app.build()


@pytest.mark.usefixtures("doc_root")
@pytest.mark.sphinx("html", testroot="test-packaging")
def test_html_output(app: Sphinx, html_regression: HTMLRegressionFixture) -> None:
	app.build()

	# capout = app._warning.getvalue()
	#
	# for string in {
	# 		"WARNING: invalid PEP number abc",
	# 		"WARNING: more than one target found for cross-reference 'name': project.name, tool.something.name"
	# 		}:
	# 	assert string in capout

	output_file = PathPlus(app.outdir) / "index.html"

	page = BeautifulSoup(output_file.read_text(), "html5lib")

	# Make sure the page title is what you expect
	title = page.find("h1").contents[0].strip()
	assert "sphinx-packaging demo" == title

	code: bs4.element.Tag
	for code in page.find_all("code", attrs={"class": "sig-prename descclassname"}):
		first_child = code.contents[0]
		if isinstance(first_child, bs4.element.Tag):
			code.contents = [first_child.contents[0]]

	for code in page.find_all("code", attrs={"class": "sig-name descname"}):
		first_child = code.contents[0]
		if isinstance(first_child, bs4.element.Tag):
			code.contents = [first_child.contents[0]]

	for div in page.findAll("script"):
		if div.get("src"):
			div["src"] = div["src"].split("?v=")[0]
			print(div["src"])

	html_regression.check(page, jinja2=True)


@pytest.mark.usefixtures("doc_root")
@pytest.mark.sphinx("latex", testroot="test-packaging")
def test_latex_output(app: Sphinx, latex_regression: LaTeXRegressionFixture) -> None:

	assert app.builder.name.lower() == "latex"

	app.build()

	output_file = PathPlus(app.outdir) / "python.tex"
	content = StringList(output_file.read_lines())
	latex_regression.check(
			str(content).replace("\\sphinxAtStartPar\n", ''),
			jinja2=True,
			)
