import json
import logging
import os
import sys
import traceback
from http import HTTPStatus

from app.vulnerability.vulnerability_service_factory import vulnerability_service_factory
from vulnerability.vulnerability import Vulnerability

def lambda_handler(payload):
    logger = logging.getLogger()
    logger.setLevel(os.getenv("LOG_LEVEL") or logging.INFO)

    try:
        logger.info(f"start with payload: {str(payload)}")

        if "body" not in payload:
            raise Exception("malformed body")

        vulnerability = Vulnerability.from_json_string(payload["body"])
        vulnerability_service = vulnerability_service_factory(logger)
        response = vulnerability_service.insert(vulnerability)

        logger.info(f"response: {str(response)}")

        return {
            "statusCode": HTTPStatus.CREATED,
            "body": json.dumps({
                "message_id": response["MessageId"]
            })
        }
    except BaseException as e:
        ex_type, ex_value, ex_traceback = sys.exc_info()
        trace_back = traceback.extract_tb(ex_traceback)
        stack_trace = list()

        for trace in trace_back:
            stack_trace.append(
                "file: %s, line: %d, function name: %s, message: %s"
                % (trace[0], trace[1], trace[2], trace[3])
            )

        logger.error(f"exception type: {ex_type.__name__}")
        logger.error(f"exception message: {ex_value}")
        logger.error(f"stack trace: {stack_trace}")

        return {
            "statusCode": HTTPStatus.INTERNAL_SERVER_ERROR,
            "body": json.dumps({
                "message": str(ex_value),
            })
        }
