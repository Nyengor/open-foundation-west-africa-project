# Galamsay Data Analysis & REST API

This project analyzes illegal small-scale mining (Galamsay) activities in Ghana using structured CSV data.  
The system performs data cleaning, statistical analysis, persistent storage, and exposes results via a RESTful API.

The project simulates a real-world workflow involving data analysis, backend processing, and API development.

---

## Problem Statement

OFWA provided a dataset containing records of illegal small-scale mining sites across Ghanaian cities and regions.

The objectives of this project are to:

- Clean and validate the dataset
- Perform analytical calculations
- Persist analysis results for auditing and reuse
- Expose results programmatically via an API
- Ensure correctness through automated testing

---

## System Workflow

Raw CSV Data
│
▼
Data Cleaning & Validation
│
▼
Analytical Computation
│
▼
SQLite Database (Persistent Log)
│
▼
REST API (JSON Output)



## Project Structure

Galamsey analysis/
├── analysis.py # Data loading, cleaning, analysis, database logging
├── api.py # REST API for accessing analysis results
├── galamsay_data.csv # Input dataset
├── galamsay_analysis.db # SQLite database (generated at runtime)
└── README.md # Project documentation



## Technologies Used

- **Python 3**
- **SQLite** (file-based database)
- **Flask** (REST API framework)


## Database Design

A SQLite database (`galamsay_analysis.db`) is used to log analysis runs.

Stored fields include:

- Total site count
- Highest region and its count
- Threshold used
- Cities exceeding the threshold
- Timestamp of analysis execution

Each analysis run is stored as a separate record.


## Running the Analysis

1. Ensure Python is installed:


2. Run the analysis script:

python analysis.py


## Running the REST API

1. Install Flask:

python -m pip install flask

2. Start the API server:

python api.py

3. Access results via browser or API client:

http://127.0.0.1:5000/results

The API returns analysis records in JSON format.



## Version Control

Git was used for version control with meaningful commit messages.  


## Author

Janet Dede-Nyengor Odonkor