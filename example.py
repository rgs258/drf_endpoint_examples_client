import logging
import os

import names

from secrets import API_KEY
from swagger_client import Configuration, ApiClient, ApiApi, Customer

HOST = "http://localhost:8000/"
DOWNLOADS_DIRECTORY = os.path.join(os.path.dirname(__file__), "downloads")

logger = logging.getLogger(__name__)


def create_customer_example():
    """
    In this example:
    - An API is instantiated
    - A randome name is generated and a Customer is created with that name
    :return:
    """
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


if __name__ == "__main__":
    create_customer_example()
    list_customers_example()
