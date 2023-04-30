# Toybox API

Toybox API is a centralized Flask API that serves as the back-end for multiple toy projects. The API is organized into different blueprints, each corresponding to a specific project. This repository was created to provide a single location to host and manage the back-end code for these projects, which are primarily accessed through the [Portfolio](https://github.com/yourusername/portfolio) React app.

## Features

- Centralized API for multiple toy projects
- Flask Blueprints to separate and manage endpoints for each project
- Easy integration with the Portfolio React app

## Table of Contents

1. [Getting Started](#getting-started)
2. [Usage](#usage)
3. [Creating a New Project Blueprint](#creating-a-new-project-blueprint)
4. [API Documentation](#api-documentation)
5. [Contributing](#contributing)
6. [License](#license)

## Getting Started

To set up the API locally, follow these steps:

### Prerequisites

- Conda
- Python 3.8 or higher

### Installation

1. Clone the repository: 
```bash
git clone https://github.com/pashbylogan/toybox-api.git

2. Create and activate a Conda environment using the provided `conda.yml` file:
```bash
conda env create -f conda.yml
conda activate toybox-api

3. Start the development server using gunicorn
```bash
gunicorn wsgi:app


Now, the API should be running at `http://localhost:8000`.

## Usage

To access a specific project's API endpoints, use the project's blueprint prefix. For example, if you have a project called "project1" with a blueprint prefix of `/project1`, you would access its endpoints at `http://localhost:8000/project1/endpoint`.

## Creating a New Project Blueprint

To create a new project blueprint, follow these steps:

1. In the `blueprints` folder, create a new folder for your project, e.g., `project2`.

2. Inside the new folder, create a `__init__.py` file and a `routes.py` file.

3. In the `__init__.py` file, define your blueprint with a prefix:

```python
from flask import Blueprint

project2_blueprint = Blueprint('project2', __name__, url_prefix='/project2')

In the routes.py file, define your project's endpoints:
```python
from . import project2_blueprint

@project2_blueprint.route('/endpoint', methods=['GET'])
def your_function():
    # Your code here

5. Import the blueprint in the app.py file and register it:
```python
from blueprints.project2 import project2_blueprint

app.register_blueprint(project2_blueprint)

Now, your project's endpoints are accessible at http://localhost:8000/project2/endpoint.

## API Documentation
The API documentation is available at API_DOCS.md. This file contains information about the available endpoints for each project, including request parameters, response formats, and examples.

## Contributing
To contribute to this repository, please submit an issue or create a pull request with a clear description of the changes you propose. All contributions are welcome, and we appreciate your help in improving the Toybox API.

## License
This project is licensed under the MIT License.

