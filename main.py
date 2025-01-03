from ETLpipeline.core.extraction  import  ExtractData
from ETLpipeline.core.transform import TransformData
from ETLpipeline.core.load import LoadData
from ETLpipeline.config import config

def main():
    path_config = config.get_paths()
    db_config = config.get_database_config()
    
    file_path = f"{path_config['data_dir']}/employee_data.csv"
    table_name  = db_config['table']

    extracted_data = ExtractData(file_path)
    transformed_data = TransformData(extracted_data.data)
    
    if transformed_data is not None:
        print("Data extraction and transformstion successful")

        loader = LoadData()
        try:
            loader.load_to_db(table_name, transformed_data.transformed_data)
        finally:
            loader.close_connection()
    else:
        print("ETLpipeline failure")

if __name__ == "__main__":
    main()
