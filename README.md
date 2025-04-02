# Weather API Project

## Overview
This project provides weather data through a REST API, fetching information from the OpenWeather API and storing it in a PostgreSQL database. The application is containerized using Docker for easy deployment and setup.

## Features
- Real-time temperature queries by city name
- API endpoints for retrieving stored weather data
- Data storage in PostgreSQL database
- Fully containerized setup with Docker
- API documentation using drf-spectacular
- Admin interface for manual data management

## Tech Stack
- Django 5.1
- Django REST Framework
- PostgreSQL
- Docker & Docker Compose
- drf-spectacular for API documentation

## Project Structure
```
src/
├── apps/
│   ├── weather/              # App for collecting weather data (Admin only)
│   │   ├── models.py         # WeatherData model
│   │   ├── services.py       # Service to interact with OpenWeather API
│   │   ├── urls.py           # URLs for admin operations
│   │   └── views.py          # Views for admin operations
│   │
│   └── weather_api/          # App for REST API endpoints to retrieve data from Postgres Database
│       ├── urls.py           # API endpoints
│       └── views.py          # API views for data retrieval
│
├── project/                  # Django project settings
└── manage.py                 # Django management script
```

## Installation and Setup

### Prerequisites
- Docker and Docker Compose
- OpenWeather API key

### Setup Steps

1. Clone the repository
   ```bash
   git clone https://github.com/rodfarah/gntech.git
   cd weather-api
   ```

2. Create a .env file based on .env-example file:

3. Run the following command in order to build containers and install the application:
   ```bash
   # First, make the script executable
   chmod +x start.sh
   
   # Then run it
   ./start.sh 
   # you will need to insert sudo password in order to execute operations. 


4. The application should now be running at:
   - API: http://localhost:8000/api/
   - API Documentation: http://localhost:8000/api/docs/
   - Admin interface: http://localhost:8000/admin/

## API Endpoints

### Weather Data Retrieval
- **GET /api/temperatures/all-records/**  
  Retrieve all temperature records in the database

- **GET /api/temperatures/by-city/{city_name}/**  
  Retrieve all temperature records for a specific city

### Weather Data Collection (Admin Only)
- **GET /api/admin/temperature/{city}/**  
  Fetch current temperature for a city from OpenWeather and store it in the database

## Development

### Running Tests
```bash
python manage.py test
```

## License
MIT License

Copyright (c) 2025 Rodrigo Farah

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

## Author
Rodrigo Farah (digofarah@gmail.com)