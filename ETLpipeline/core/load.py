from ETLpipeline.utils.db import get_db_connection
import psycopg2
import pandas as pd

class LoadData:
    def __init__(self):
        # Establish connection to the database
        self.conn = get_db_connection()
        self.cursor = self.conn.cursor() if self.conn else None

    def load_to_db(self, table_name: str, data: pd.DataFrame) -> None:
        if not self.conn:
            print("Database connection is not established")
            return None
        try:
            for index, row in data.iterrows():
                # Prepare placeholders for data values
                placeholders = ", ".join(["%s"] * len(row))
                columns = ", ".join(data.columns)
                query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
                
                # Execute the insert query
                self.cursor.execute(query, tuple(row))
            
            # Commit the transaction
            self.conn.commit()
            print(f"Inserted {len(data)} rows into {table_name}.")
        except psycopg2.Error as e:
            print(f"Error inserting data: {e}")
            self.conn.rollback()  # Rollback if error occurs
        except Exception as e:
            print(f"Unexpected error: {e}")
            self.conn.rollback()

    def close_connection(self) -> None:
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
            print("Database connection closed.")
