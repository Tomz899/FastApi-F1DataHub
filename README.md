# FastAPI Project

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)

## Overview

The FastAPI Project is a web application built using FastAPI, a modern Python web framework. It provides users with access to Formula 1 (F1) race information, including current schedules and recent race results. The application is designed to be a simple and efficient way to keep track of F1 events.

## Project Structure

The project is structured as follows:

- `main.py`: The FastAPI application.
- `templates`: HTML templates used for rendering pages.
- `static`: CSS and other static files.
- `tests`: Test cases for the application.

## Features

- Display the current F1 race schedule.
- Show the most recent F1 race results.
- API endpoints for accessing race information programmatically.
- Use of FastAPI and Jinja2 templates.
- Poetry

## Getting Started

To run this project locally, follow these steps:

### Prerequisites

- Python 3.11
- Poetry 1.6.1
- Fastapi 0.68.1
- Uvicorn 0.15.0
- Requests 2.31.0
- Jinja2 3.0.3
- Aiofiles 23.2.1
- Httpx 0.25.0

### Installation

1. Clone the repository:
   git clone https://github.com/Tomz899/FastApi-F1DataHub.git
2. Change to the project directory:
   cd FastApi-F1DataHub
3. Run poetry:

### API Endpoints

The following API endpoints are available:

/current_schedule: Returns the current F1 race schedule.
/current_results: Displays the most recent F1 race results.

### Testing

To run tests for the project, use the following command:
pytest

### Deployment

This section is currently under development.

### Contributing

Contributions are welcome! If you want to contribute to this project, please follow the guidelines in CONTRIBUTING.md.

### License

This project is licensed under the MIT License. See the LICENSE file for details.
