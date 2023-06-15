import os
import psycopg2
from dotenv import load_dotenv

class PgClient:
    def __init__(self, database="spatial_dwh"):
        load_dotenv(override=True)

        self.config = {
            "host": os.environ.get("POSTGRES_HOST", None),
            "port": os.environ.get("POSTGRES_PORT", None),
            "user": os.environ.get("POSTGRES_USERNAME", None),
            "password": os.environ.get("POSTGRES_PASSWORD", None),
            "database": database,
        }
        
        try: 
            self.conn = psycopg2.connect(**self.config)
            self.cur = self.conn.cursor()
            print(f"Connected to PostgreSQL database '{self.config['database']}'")
        except(Exception, psycopg2.DatabaseError) as error:
            raise Exception(error)

    # Getters
    def connection(self):
        return self.conn

    def cursor(self):
        return self.cur
    
    # Execution
    def execute(self, query, commit=True):
        if commit:
            self.cur.execute(query)
            self.conn.commit()
        else:
            self.cur.execute(query)

    def fetchall(self, query):
        self.cur.execute(query)
        return self.cur.fetchall()

    def close(self):
        self.cur.close()
        self.conn.close()
