# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# This main remove previous versions of the docs, and then put the source files
# in one place so sphinx can find them
%: Makefile
	# Cleanup
	rm -rf source/{{ package_name }}*
	rm -rf source/modules.rst
	rm -rf build/$@

	# Generate sources from docstrings
	sphinx-apidoc -l -o source/ ../{{ package_name }} -M

	# Build documentation
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

	rm -rf source/*_deps*


