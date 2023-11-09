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

There isn't a development server that auto-builds bundled with Sphinx. Create a new branch and make your changes.
When your changes are ready to be deployed, submit a PR and request approval. Upon a merge the site is built and deployed to an S3 bucket and the CloudFlare cache is invalidated through GitHub actions.

### Quickstart

To clone the repo, create a Python virtual environment and activate it. Install the required packages and build the site.

    git clone git@github.com:university-of-york/research-it-documentation.git
    cd research-it-documentation/
    python3 -m venv .venv
    source .venv/bin/activate
    python3 -m pip install sphinx-rtd-theme sphinx
    sphinx-build -b html docs/source site/ -a

Then simply open the built `site/index.html` in your browser.

**Compile all the web pages**

`sphinx-build -b html docs/source site/ -a`

Remove the `-a` option to only compile changes.

**Check links are valid**

`sphinx-build -b linkcheck docs/source site/`

**View the website**

Open `site/index.html` in a web browser.

**Replacements**

The `docs/source/replacements.py` file contains a dictionary of replacement words to use throughout the docs. For exmaple, all the module versions to load in the jobscript examples. This makes it simple to update that part of the docs in the future.

**Substitutions**

The `global.rst` file contains an [RST substitution](https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#substitution-definitions) so you can use `|br|` to create a raw html `</br>`. Useful in some formatting for example in the table headers. To use this substitution in a page  you must include the following at the top of the page: `.. include:: /global.rst`

**Custom CSS**

Found in the `docs/source/_static/css/custom.css` file. Only a minimal set of CSS tweaks are there as we keep close to the default theme.

**Images and Tables**

Located in the `assets/img` and `assets/data` folders. The `csv` files in the `data` folder are useful for displaying tables with better formatting.

**Example template**

To help quickly make a new page, `docs/source/template.rst` can be used as a base.

## Reference

For `Re Structured Text` help:

[Sphinx Docs](https://www.sphinx-doc.org/en/master/index.html)

[RST Specs](https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html)

The site has a *cheatsheet* page to showcase example syntax, it's built from `docs/source/cheatsheet.rst` and not linked in the website but accessible as [https://vikingdocs.york.ac.uk/cheatsheet.html](https://vikingdocs.york.ac.uk/cheatsheet.html).


