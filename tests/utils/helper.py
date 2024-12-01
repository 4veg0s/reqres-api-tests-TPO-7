import logging
from requests import Response


def response_logging(response: Response):
    logging.info("Request: " + response.request.url)
    if response.request.body:
        logging.info("INFO Request body: " + str(response.request.body))  # логирование тела запроса если оно есть
        logging.info("Request headers: " + str(response.request.headers))
        logging.info("Response code " + str(response.status_code))
        logging.info("Response: " + response.text)
