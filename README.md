# CSV to Database ETL Pipeline Demo
![Architecture Diagram](/architecture_diagram.png)

## Overview  
This project demonstrates a simple ETL (Extract, Transform, Load) pipeline that reads data from a CSV file, processes it, and loads it into a database. The pipeline is designed to showcase the fundamental principles of data engineering while being easy to set up and use. The pipeline is also containerized using docker to ensure portability and consistency across environments.

---

## Features
- Fully containerized for seamless deployment.
- Extracts data from CSV files.
- Performs basic data validation and transformation.
- Loads processed data into a relational database.
- Built with modularity and reusability in mind.
- YAML-based configuration management
- Comprehensive logging system
- Type-hinted codebase
- Includes error handling for common issues.

---

## Table of Contents  
- [CSV to Database ETL Pipeline Demo](#csv-to-database-etl-pipeline-demo)
  - [Overview](#overview)
  - [Features](#features)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Project Structure](#project-structure)
  - [Setup and Installation](#setup-and-installation)
  - [Usage](#usage)
  - [Pipeline Workflow](#pipeline-workflow)
  - [Technologies Used](#technologies-used)
  - [Further Improvements](#further-improvements)

---

## Prerequisites
- A PostgreSQL Database
- Docker installed on your system.

---

## Project Structure  
```
ETLpipeline/
├── core/
│   ├── extraction.py         # Handles CSV data extraction
│   ├── transform.py          # Data transformation logic
│   └── load.py               # Database loading operations
├── utils/
│   └── db.py                 # Database connection utilities
├── config/
│   ├── config.py             # Configuration management
│   └── config.example.yaml   # Example Configuration file
|   └── config.yaml           # Main Configuration file, you will need to create this
├── tests/                    # Unit tests for the ETL components
└── main.py                   # Main ETL pipeline executor
├── requirements.txt          # Python dependencies
├── Dockerfile                # Dockerfile for the ETL pipeline
└── README.md                 # Project documentation
```

---

## Setup and Installation  
1. Clone the repository:  
   ```bash
   git clone https://github.com/Data-Bishop/csv-to-db-etl.git
   cd csv-to-db-etl
   ```

2. Set up your configurations (`config/config.yaml`).
   
3. Build the Docker Image
   Build the Docker image using the provided Dockerfile:
   ```bash
   docker build -t csv-to-db-etl .
   ```

4. Run the Container
   Run the container with the following command:
   ```bash
   docker run --network host -v ${pwd}/ETLpipeline/data:/app/ETLpipeline/data -v ${pwd}/ETLpipeline/config:/app/ETLpipeline/config csv-to-db-etl
   ```

   This mounts the `data/` and the `config/` directories from your host machine to the container, allowing the pipeline to process your CSV files.

---

## Usage  
1. Place your CSV file(s) in the `data/` directory.
   By default, the pipeline is configured to process files in this directory.

2. Run the pipeline:  
   After placing the CSV files, simply run the Docker container (as shown above) to start the ETL process.

3. Check the database to verify the data was successfully loaded.
   Use Docker logs for debugging, if necessary:
   ```bash
   docker logs <container_id>
   ```

---

## Pipeline Workflow  
1. **Extract:**  
   - Reads data from the CSV file(s).  
   <!-- - Handles issues like missing files or unsupported formats. -->

2. **Transform:**  
   <!-- - Validates and cleans data (e.g., removing duplicates, handling nulls).   -->
   - Converts data to the appropriate schema for the database.

3. **Load:**  
   - Inserts the processed data into a database table.  
   <!-- - Uses bulk inserts for performance efficiency.   -->

---

## Technologies Used  
- **Docker**: Containerization of the application.
- **Python**: Core programming language for the pipeline.
- **pandas**: Data processing and manipulation.
- **Psycopg2**: Database connection.
- **PostgreSQL**: Database system for storing transformed data.

---

## Further Improvements
- Add support for multiple file formats (e.g., JSON, Excel).  
- Implement advanced transformations (e.g., deduplication, type casting).  
- Add monitoring capabilities. 
- Support more databases (e.g., MongoDB, Snowflake).

---
