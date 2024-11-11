from dataclasses import dataclass
import os
import pymongo
from sensor.constant.env_variable import MONGODB_URL_KEY
from sensor.logger import logging
@dataclass


class EnvironmentVariable:
    mongo_db_url:str = os.getenv("MONGO_DB_URL")
    logging.info(f"Loaded MongoDB URL from environment: {mongo_db_url}")


env_var = EnvironmentVariable()

mongo_client = pymongo.MongoClient(env_var.mongo_db_url)