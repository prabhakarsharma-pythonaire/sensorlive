from sensor.exception import SensorException
import sys
from sensor.logger import logging
from sensor.utils import dump_csv_file_mongodb_collection

# def test_exception():
#     try:
#         logging.info("intentionally causing error to check if it's working")
#         b = 1/0
#
#     except Exception as e:
#         raise SensorException(e,sys)


if __name__ == "__main__":
    file_path = "aps_failure_training_set1.csv"
    database_name = "mldb"
    collection_name = "col"

    dump_csv_file_mongodb_collection(file_path, database_name, collection_name)

