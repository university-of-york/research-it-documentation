# research-it-documentation
A static website hosting Research IT related documentation.

## [https://vikingdocs.york.ac.uk/](https://vikingdocs.york.ac.uk/)

## Technical

### Infrastructure

The website is hosted in S3 and delivered from a CloudFront distribution.
It is defined in `cloudformation.yaml` and deployed via GitHub Actions, although the SSL certificate is manually created and added to CloudFront through the AWS website.
The certificate is validated through DNS by adding the CNAMEs it provides, this can be done via a ticket to Systems.

### Content

The content is generated using `sphinx` with the `rtd` theme.
The source markdown files are stored in `docs` and the content is deployed via GitHub Actions.

## Development

Clone the repo, install `sphinx` through

`pip install sphinx sphinx-rtd-theme`

**Compile the web pages**

`sphinx-build -b html docs/source site/`

**View the website**

Open `site/index.html` in a web browser.

**Check links are valid**

`sphinx-build -b linkcheck docs/source site/`

There isn't a development server that auto-builds bundled with Sphinx.
When your changes are ready to be deployed, submit a PR and request approval.

**Replacement**

The `docs/source/replacements.py` file contains a dictionary of replacement words to use throughout the docs. For exmaple, all the module versions to load in the jobscript examples. This makes it simple to update that part of the docs in the future.

## Reference

For `Re Structured Text` help:

[Sphinx Docs](https://www.sphinx-doc.org/en/master/index.html)

[RST Specs](https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html)

The site has a cheatsheet page which is built from `docs/source/cheatsheet.rst` and not linked in the website but accessible as [https://vikingdocs.york.ac.uk/cheatsheet.html](https://vikingdocs.york.ac.uk/cheatsheet.html).


