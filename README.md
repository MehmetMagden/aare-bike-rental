Aare Bike Rental — The Infinity Pipeline
A Flask REST API for Bern's bike rental system, fully containerized with Docker and automated with a CI/CD pipeline powered by GitHub Actions.

Overview
This project modernizes Bern's bike rental infrastructure by:

Preventing faulty code from reaching production (automated testing)
Ensuring consistent behavior across all environments (Docker)
Automating the build and delivery process (GitHub Actions)
Tech Stack
Layer	Technology
Backend	Python / Flask 3.0.0
Testing	pytest 7.4.0
Container	Docker (Multi-stage build)
CI/CD	GitHub Actions
Registry	Docker Hub
Project Structure
aare-bike-rental/
├── app/
│   ├── app.py              # Flask REST API
│   └── requirements.txt    # Python dependencies
├── tests/
│   └── test_app.py         # pytest test suite
├── .github/
│   └── workflows/
│       └── docker.yml      # The Infinity Pipeline
├── Dockerfile              # Multi-stage build
├── .dockerignore
├── .gitignore
└── README.md
API Endpoints
Method	Endpoint	Description	Response
GET	/health	Health check	{"status": "healthy", "service": "Aare Bike Rental"}
GET	/bikes	List all bikes	JSON array of bike objects
Example Responses
# Health check
curl http://localhost:5000/health
# {"status": "healthy", "service": "Aare Bike Rental"}

# List bikes
curl http://localhost:5000/bikes
# [{"id": 1, "model": "Scott Sub Active", "status": "available"}, ...]
CI/CD Pipeline — The Infinity Pipeline
Every git push to master triggers the full pipeline:

git push
    |
    +-- test-stage
    |       Checkout code
    |       Setup Python 3.11
    |       pip install dependencies
    |       Run pytest (2 tests)
    |
    +-- docker-stage (only if test-stage passes)
            Login to Docker Hub
            Build Docker image (multi-stage)
            Push to Docker Hub
Pipeline File
.github/workflows/docker.yml

Docker
Multi-Stage Build
Stage 1 (builder): Install Python dependencies
Stage 2 (final):   Copy only what's needed — smaller image
Run Locally
# Pull from Docker Hub
docker pull wowmaker/aare-bike-rental:latest

# Run
docker run -p 5000:5000 wowmaker/aare-bike-rental:latest

# Test
curl http://localhost:5000/health
Local Development
Requirements
Python 3.11+
Docker
Setup
# Clone the repository
git clone https://github.com/MehmetMagden/aare-bike-rental.git
cd aare-bike-rental

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r app/requirements.txt
Run Tests
pytest tests/ -v
Expected output:

tests/test_app.py::test_health_check    PASSED
tests/test_app.py::test_get_bikes       PASSED
2 passed
Run Application
python app/app.py
# Serving on http://0.0.0.0:5000
Security
Docker Hub credentials are stored as GitHub Secrets (DOCKER_USERNAME, DOCKER_PASSWORD)
Credentials are never hardcoded in any file
.gitignore prevents sensitive files from being committed
Key Achievements
Faulty code is blocked automatically — pipeline stops on test failure
Portable — runs identically on any machine with Docker
Secure — credentials managed via GitHub Secrets
Fast — full pipeline completes in under 60 seconds
Author
Mehmet Magden — DevOps Engineer in Training
GitHub: github.com/MehmetMagden
Docker Hub: hub.docker.com/u/wowmaker