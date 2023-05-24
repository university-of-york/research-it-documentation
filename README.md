# research-it-documentation
A static website hosting Research IT related documentation.

## Technical

### Infrastructure

The website is hosted in S3 (behind a CloudFront distribution coming soon).
It is defined in `cloudformation.yaml` and deployed via GitHub Actions.

### Content

The content is generated using `mkdocs` with the `material` theme.
The source markdown files are stored in `docs` and the content is deployed via GitHub Actions.

## Development

Clone the repo, install `mkdocs` through `pip install mkdocs-material` and run `mkdocs serve` to deploy a development web server that watches for changes made to the `docs` folder.
When your changes are ready to be deployed, submit a PR and request approval.
