<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<div align="center">

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

</div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/university-of-york/research-it-documentation">
    <img src="images/logo.png" alt="Logo" width="200" height="200">
  </a>

<h3 align="center">Viking Documentation</h3>

  <p align="center">
    A static website hosting Viking and Research IT related documentation.
    <br />
    <a href="https://vikingdocs.york.ac.uk/"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/university-of-york/research-it-documentation/issues">Report Bug</a>
    ·
    <a href="https://github.com/university-of-york/research-it-documentation/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#technical">Technical</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#windows-installation">Windows Installation</a></li>
        <li><a href="#manual-dependency-install">Manual Dependency Install</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#reference">Reference</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://vikingdocs.york.ac.uk/)

### Technical

#### Infrastructure

The website is hosted in S3 and delivered from a CloudFront distribution.
It is defined in `cloudformation.yaml` and deployed via GitHub Actions, although the SSL certificate is manually created and added to CloudFront through the AWS website.
The certificate is validated through DNS by adding the CNAMEs it provides, this can be done via a ticket to Systems.

#### Content

The content is generated using `sphinx` with the `rtd` theme.
The source markdown files are stored in `docs` and the content is deployed via GitHub Actions.

#### Development

There isn't a development server that auto-builds bundled with Sphinx. Create a new branch and make your changes.
When your changes are ready to be deployed, submit a PR and request approval. Upon a merge the site is built and deployed to an S3 bucket and the CloudFlare cache is invalidated through GitHub actions.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python]][Python-url]
* [![Read the Docs][Read-the-docs]][Read-the-docs-url]
* [![Sphinx][Sphinx]][Sphinx-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Below is a step by step guide to getting up and running on Linux followed by an example on Windows. The built pages are static so once built the site is easily viewable in any web browser.

### Prerequisites

Python 3 and git.

### Installation

1. Clone the repo

    ```
    git clone git@github.com:university-of-york/research-it-documentation.git
    cd research-it-documentation/
    ```

2. Create a Python virtual environment and activate it

    ```
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. Install the required packages

    ```
    python3 -m pip install -r requirements.txt
    ```

4.  Build the site

    ```
    sphinx-build -b html docs/source site/ -a
    ```

5. To view the site simply open the newly built `site/index.html` in your browser

### Windows Installation

Python can be installed via Anaconda3 from the Software Center on a managed Windows PC (Git should already be installed), then from a PowerShell:

    git clone https://github.com/university-of-york/research-it-documentation.git
    cd research-it-documentation/
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
    python -m pip install -r requirements.txt
    sphinx-build -b html docs/source site/ -a

To view the site simply open the newly built `site/index.html` in your browser

### Manual dependency install

If needed, you can manually install the two required Python packages `sphinx-rtd-theme` and `sphinx` with:

    python3 -m pip install sphinx-rtd-theme sphinx

<!-- USAGE EXAMPLES -->
## Usage

### Replacements

The `docs/source/replacements.py` file contains a dictionary of replacement words to use throughout the docs. For exmaple, all the module versions to load in the jobscript examples. This makes it simple to update that part of the docs in the future.

### Substitutions

The `global.rst` file contains an [RST substitution](https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#substitution-definitions) so you can use `|br|` to create a raw html `</br>`. Useful in some formatting for example in the table headers. To use this substitution in a page  you must include the following at the top of the page: `.. include:: /global.rst`

### Custom CSS

Found in the `docs/source/_static/css/custom.css` file. Only a minimal set of CSS tweaks are there as we keep close to the default theme.

### Images and Tables

Located in the `assets/img` and `assets/data` folders. The `csv` files in the `data` folder are useful for displaying tables with better formatting.

### Example template

To help quickly make a new page, `docs/source/template.rst` can be used as a base.

### Application guides

Any `.rst` files dropped into the `docs/source/applications` folder will automatically be `globbed` and added to that section by the `toctree` directive in the `docs/source/applications/index.rst` page.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [x] Infrastructure
    - [x] Move site to AWS
    - [x] Fix issue with CloudFront cache invalidation
- [x] Get ready for Pull Requests:
    - [x] Update README.md to new format
    - [x] Use public actions for workflow
- [ ] New pages:
    - [x] Create 'Data Management' section
    - [x] Add X11 Forwarding page
    - [ ] Slurm common commands page
- [ ] Update pages:
    - [x] Update Virtual desktops page
    - [x] Move all application specific pages to one section
      - [x] Split up into separate pages
    - [ ] FAQ page with common issues
    - [ ] RELION jobscript

See the [open issues](https://github.com/university-of-york/research-it-documentation/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a [Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork)

> [!NOTE]
> You may need to [keep your pull request in sync with the base branch](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/keeping-your-pull-request-in-sync-with-the-base-branch) if other updates are also being added around the same time.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Research IT - itsupport@york.ac.uk

Project Link: [https://github.com/university-of-york/research-it-documentation](https://github.com/university-of-york/research-it-documentation)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- REFERENCE -->
## Reference

* [Sphinx Documentation](https://www.sphinx-doc.org/en/master/index.html)
* [Re Structured Text Specs](https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [othneildrew](https://github.com/othneildrew/Best-README-Template) for the README.md template

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/badge/contributors-🤝-0f5323?style=for-the-badge
[contributors-url]: https://github.com/university-of-york/research-it-documentation/graphs/contributors
[forks-shield]: https://img.shields.io/badge/forks-🍴-bb8009?style=for-the-badge
[forks-url]: https://github.com/university-of-york/research-it-documentation/network/members
[stars-shield]: https://img.shields.io/badge/stars-⭐-553098?style=for-the-badge
[stars-url]: https://github.com/university-of-york/research-it-documentation/stargazers
[issues-shield]: https://img.shields.io/badge/issues-🐛-0d419d?style=for-the-badge
[issues-url]: https://github.com/university-of-york/research-it-documentation/issues
[product-screenshot]: images/screenshot.png
[Python]: https://img.shields.io/badge/Python-3776ab?style=for-the-badge&logo=Python&logoColor=white
[Python-url]: https://www.python.org/
[Read-the-docs]: https://img.shields.io/badge/Read_the_Docs-2980b9?style=for-the-badge&logo=read%20the%20docs&logoColor=white
[Read-the-docs-url]: https://docs.readthedocs.io/en/stable/index.html
[Sphinx]: https://img.shields.io/badge/Sphinx-0A507A?style=for-the-badge&logo=Sphinx&logoColor=white
[Sphinx-url]: https://www.sphinx-doc.org/

