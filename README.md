# Swagger JSON Parser

## Overview

This project is a simple Python script that fetches Swagger JSON from a given URL and extracts and lists all the endpoints present in the Swagger documentation. It's designed to help you understand the API endpoints quickly.

## Prerequisites

Before you get started, ensure that you have the following prerequisites:

- Python 3.x installed
- `requests` library (You can install it using `pip install requests`)

## Getting Started

1. Clone this repository to your local machine if you haven't already:

   ```bash
   git clone git@github.com:PiyushChakerwarty/exploring-swagger-endpoints.git

2. **Navigate to the project directory:**

   ```bash
   cd swagger-json-parser

3. Run the Python script to parse Swagger JSON and list endpoints:

    ```python swagger_endpoints.py


## Usage:

Modify the swagger_url variable in the Python script (swagger_endpoints.py) to use a different Swagger JSON URL if needed.
Run the script to get a list of endpoints from the Swagger documentation.

## Example Output:

Here is an example of what the script output might look like:
    
    Endpoints:
    /pet
    /store/inventory
    /user
    /pet/{petId}