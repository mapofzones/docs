# Map of Zones docs

Status of Last Deployment:<br>
<img src="https://github.com/mapofzones/docs/workflows/CI/badge.svg"><br>

Map of Zones docs is a project documentation static site. Used static site generator MkDocs, and some extensions.

## Requirements

* Python (3.8, 3.9 or later) - [python.org/downloads](https://www.python.org/downloads/)
* Pip [via python] (20.0.2 or later) - `python get-pip.py`
* MkDocs [via pip] (1.1.2 or later) - `pip install mkdocs`
* MkDocs-diagrams [via pip] (v1.0.0 or later) - `pip install mkdocs-diagrams`
* Graphviz dot (2.44.1 or later) - [graphviz.org/download](https://www.graphviz.org/download/)

## Usage

* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

1) **Pages** - project documentation with Markdown. User guides: [mkdocs.org/user-guide](https://www.mkdocs.org/user-guide/writing-your-docs/)

2) **Diagram as Code** - diagrams lets you draw the cloud system architecture in Python code. Examples: [diagrams.mingrammer.com](https://diagrams.mingrammer.com/docs/getting-started/examples)



## Deploy

Just push your changes to github. On changes in the master branch, github actions will automatically prepare the build. If the build is successful, the new version of the static site will be deployed.