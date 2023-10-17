import logging
import os
from datetime import datetime

import names

from secrets import API_KEY
from swagger_client import Configuration, ApiClient, ApiApi, Customer

HOST = "http://localhost:8000/"
BASE_DIR = os.path.dirname(__file__)
DOWNLOADS_DIRECTORY = os.path.join(BASE_DIR, "downloads")
CONSOLE_LOGGING_FORMAT = (
    '%(asctime)s %(levelname)-8s %(name)s.%(funcName)s: %(message)s'
)


logger = logging.getLogger(__name__)


def create_customer_example():
    """
    In this example:
    - An API is instantiated
    - A randome name is generated and a Customer is created with that name
    :return:
    """
    logger.info("Creating a Customer")

    # Instantiate an API
    api = ApiApi(ApiClient(get_config()))

    # Generate a random person's name using the names library
    name = names.get_full_name()

    # Create a Customer with the random name
    customer = api.create_customer(
        body=Customer(name=name, email="fake@example.com", password="password")
    )

    # Write the Customer to the logger
    logger.info(f"Customer: {customer}")


def list_customers_example():
    """
    In this example:
    - An API is instantiated
    - A list of Customers is retrieved and written to the logger
    :return:
    """
    logger.info("Listing Customers")
    
    # Instantiate an API
    api = ApiApi(ApiClient(get_config()))

    # Get a list of Customers
    customers = api.list_customers()

    # Write the list of Customers to the logger
    for customer in customers:
        logger.info(f"Customer: {customer}")


def get_config():
    """
    This is an example of how one might get a config.
    Feel free - and encouraged - to copy and modify this function in your application!

    In this code, API_KEY is a constant that is provided to the running code in a
    secure way. The way in which you provide the API_KEY is defined by your
    implementation, and it is your responsibility to secure this secret!
    """
    if not os.path.exists(DOWNLOADS_DIRECTORY):
        os.makedirs(DOWNLOADS_DIRECTORY)
    configuration = Configuration()
    configuration.api_key["Authorization"] = API_KEY
    configuration.api_key_prefix["Authorization"] = "Token "
    configuration.host = HOST
    configuration.temp_folder_path = DOWNLOADS_DIRECTORY
    return configuration

def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        handlers=[
            logging.FileHandler(filename="saspg_compare.log"),
            logging.StreamHandler()
        ],
        format=CONSOLE_LOGGING_FORMAT
    )


if __name__ == "__main__":
    configure_logging()
    start_time = datetime.now()
    logger.info("Starting example.py at %s", start_time)
    create_customer_example()
    list_customers_example()
    end_time = datetime.now()
    duration = end_time - start_time
    logger.info("Finished example.py at %s. Duration: %s", end_time, duration)


