import psycopg2.pool
from ETLpipeline.config import config
import psycopg2
from psycopg2 import OperationalError
from psycopg2.extensions import connection

def get_db_connection() -> connection | None:
    db_config = config.get_database_config()
    try:
        # Create a connection pool
        connection_pool = psycopg2.pool.SimpleConnectionPool(
            minconn=1,
            maxconn=db_config['pool_size'],
            host=db_config['host'],
            port=db_config['port'],
            user=db_config['user'],
            password=db_config['password'],
            database=db_config['database'],
            connect_timeout=db_config['timeout']
        )
        
        # Get a connection from the pool
        conn = connection_pool.getconn()
        
        if conn:
            print("Successfully connected to the PostgreSQL database.")
            return conn
    except OperationalError as e:
        print(f"Error while connecting to PostgreSQL: {e}")
        return None