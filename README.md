# Weather Data API

This project provides a RESTful API for fetching, storing, and retrieving temperature data for cities around the world. It uses Django with PostgreSQL, containerized with Docker for easy deployment and development.

## Features

- Fetch current temperature data from OpenWeather API for any valid city name (Only ADMIN users should have access)
- City names must be provided in English and must exist in the OpenWeather database
- Automatically store temperature data in PostgreSQL database
- RESTful API to access stored temperature information (Any user should have access)
- Interactive API documentation with Swagger/ReDoc
- Docker containerization for consistent development and deployment

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/)
- [Make](https://www.gnu.org/software/make/) (optional, for using Makefile commands)
- OpenWeather API key (I will send it to gntech via e-mail)

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/rodfarah/gntech.git>
cd gntech
```

### 2. Configure environment variables

Create a .env file in the root directory with the same variables deffined in .env-example file

### 3. Build and start the application

Using Make:
```bash
make up
```

Or using Docker Compose directly:
```bash
docker compose up --build
```

The application will be available at http://localhost:8000

## Project Structure

```
gntech/
├── docker-scripts/       # Scripts for Docker container
│   └── commands.sh       # Container startup script
├── src/                  # Django project source code
│   ├── apps/             # Django applications
│   │   ├── weather/      # Weather data collection
│   │   └── weather_api/  # API endpoints
│   └── project/          # Django project settings
├── .env                  # Environment variables (create this file)
├── docker-compose.yml    # Docker Compose configuration
├── Dockerfile            # Docker container definition
├── Makefile              # Make commands for common operations
├── poetry.lock           # Poetry lock file
├── pyproject.toml        # Poetry project definition
└── pytest.ini           # pytest configuration
```

## Django Applications Structure

The project is divided into two Django applications, each with a specific responsibility following the single responsibility principle:

### 1. Weather Data Collection (`apps.weather`)

This application is responsible for fetching data from the OpenWeather API and storing it in the database.
Only a ADMIN user should have access to this features.

#### Key Components:

- **Models**: Defines the `WeatherData` model that stores city, temperature, and timestamp information
- **Services**: Contains the `WeatherService` class that handles API communication with OpenWeather
- **Views**: Provides admin-only endpoints for triggering data collection for specific cities
- **URLs**: Routes for admin operations (`/api/admin/v1/get-temperature/{city}/`)

#### Features:

- Fetches real-time temperature data from OpenWeather API
- Validates and processes the incoming data
- Stores temperature records in the PostgreSQL database
- Handles API connection errors gracefully
- Admin-only access for data collection operations

### 2. Weather API (`apps.weather_api`)

This application exposes REST endpoints to retrieve the weather data stored in the database.
Any user should have access to this features.

#### Key Components:

- **Views**: Defines views for listing and filtering temperature data
- **Serializers**: Handles the conversion of database objects to JSON responses
- **URLs**: Defines public API endpoints (`/api/v1/temperatures/all-records/`, `/api/v1/temperatures/by-city/{city_name}/`)
- **Tests**: Includes test cases for the API endpoints

#### Features:

- Browsable REST API with filtering capabilities
- Pagination support for large datasets
- Properly formatted JSON responses
- API documentation via Swagger/ReDoc
- Public access for data retrieval

### Interaction Between Apps

The applications work together as follows:

1. `weather` app collects data from OpenWeather and populates the database
2. `weather_api` app provides read-only access to this data through RESTful endpoints
3. Both apps share the same database models but have different responsibilities

This separation of concerns makes the codebase more maintainable, testable, and allows for independent scaling of the data collection and API serving components.


## Available Commands

The project includes a Makefile with the following commands:

```bash
# Start the containers (build if needed)
make up

# Stop the containers
make down

# Build Docker images
make build
```

## Running Tests

To run the tests:

```bash
# Execute tests inside the Django container
docker exec -it djangoapp poetry run pytest
```

For specific test files:

```bash
docker exec -it djangoapp poetry run python /app/src/manage.py test apps.weather_api
```

## Container Architecture

The project uses two Docker containers:

1. **djangoapp**: Python 3.10 with Django application
   - Uses Poetry for dependency management
   - Runs as non-root user for security
   - Waits for PostgreSQL to be available before starting

2. **psql**: PostgreSQL 13 database
   - Uses persistent volume for data storage
   - Configured with environment variables from .env file

## Development Flow

1. Make changes to the source code in the src directory
2. Changes are automatically reflected due to volume mounting
3. For dependency changes, rebuild the container with `make build`
4. Access the admin interface at http://localhost:8000/admin/
5. View API documentation at http://localhost:8000/api/docs/

## MIT License

```
Copyright (c) 2025 Rodrigo Lagrotta Silva Farah

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
