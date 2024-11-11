import sys
from typing import Optional
import numpy as np
import pandas as pd
import json
from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.constant.database import DATABASE_NAME
from sensor.exception import SensorException
from sensor.logger import logging


class SensorData:
    """
    This class helps to export the entire MongoDB record as a pandas DataFrame.
    """

    def __init__(self):
        try:
            # Initialize MongoDB client with explicit database context
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
            self.mongo_client.database = self.mongo_client.client[DATABASE_NAME]
            logging.info(f"Initialized MongoDB Client for database: {DATABASE_NAME}")
            print("Connection established. Client started.")

        except Exception as e:
            logging.error(f"Error initializing MongoDB Client: {e}")
            raise SensorException(e, sys)

    def save_csv_file(self, file_path, collection_name: str, database_name: Optional[str] = None):
        try:
            data_frame = pd.read_csv(file_path)
            data_frame.reset_index(drop=True, inplace=True)
            records = list(json.loads(data_frame.T.to_json()).values())

            # Select collection based on the provided database context
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]

            collection.insert_many(records)
            logging.info(f"Inserted {len(records)} records into collection: {collection_name}")
            return len(records)
        except Exception as e:
            logging.error(f"Error saving CSV to MongoDB: {e}")
            raise SensorException(e, sys)

    def export_collection_as_dataframe(self, collection_name: str, database_name: Optional[str] = None) -> pd.DataFrame:
        try:
            """
            Export the entire collection as a DataFrame.
            Returns:
                pd.DataFrame: DataFrame of the collection data
            """
            # Log the database and collection names
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
                logging.info(f"Fetching data from database: {DATABASE_NAME}, collection: {collection_name}")
            else:
                collection = self.mongo_client[database_name][collection_name]
                logging.info(f"Fetching data from database: {database_name}, collection: {collection_name}")

            # Fetch data and convert to DataFrame
            df = pd.DataFrame(list(collection.find()))
            logging.info(f"Number of documents fetched: {len(df)}")

            # Drop the '_id' column if present
            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis=1)

            # Replace 'na' with NaN
            df.replace({"na": np.nan}, inplace=True)
            return df

        except Exception as e:
            logging.error(f"Error exporting collection as DataFrame: {e}")
            raise SensorException(e, sys)
