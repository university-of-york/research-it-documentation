# research-it-documentation
A static website hosting Research IT related documentation.

## Technical

### Infrastructure

The website is hosted in S3 (behind a CloudFront distribution coming soon).
It is defined in `cloudformation.yaml` and deployed via GitHub Actions.

### Content

The content is generated using `sphinx` with the `rtd` theme.
The source markdown files are stored in `docs` and the content is deployed via GitHub Actions.

## Development

Clone the repo, install `sphinx` through `pip install sphinx sphinx-rtd-theme` and run `sphinx-build -b html docs/source site/` to compile the web pages and open `site/index.html` in a web browser.
There isn't a development server that auto-builds bundled with Sphinx.
When your changes are ready to be deployed, submit a PR and request approval.

Check links are valid with the following `sphinx-build -b linkcheck docs/source site/`

## Reference

[Sphinx Docs](https://www.sphinx-doc.org/en/master/index.html)

[RST Specs](https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html)
