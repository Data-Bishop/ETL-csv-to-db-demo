# ETL Pipeline

A data pipeline for processing employee data.

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Create a `config.yaml` in the `config` subdirectory
3. Use the `config.example.yaml` as a refernce to configure your `config.yaml`
4. Run the pipeline: `python main.py`

## Project Structure
- ETLpipeline/
  - core/ : Core ETL components
  - config/ : Configuration files
  - utils/ : Utility functions
  - data/ : Data files