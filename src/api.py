import base64
import json
from src import util, dao, connector, s3, constant


def get_records(event, context):
    data = dao.find()
    return {"statusCode": 200, "headers": constant.HEADERS, "body": json.dumps(data, cls=util.DecimalEncoder)}


def get_records_chart(event, context):
    data = s3.find(constant.DEMONA_CHART_FILE_NAME_S3)
    return {
        "statusCode": 200,
        "headers": {
            **constant.HEADERS,
            "Content-Type": "image/png",
            "Cache-Control": "no-cache, no-store, must-revalidate",
            'Content-Disposition': f'inline; filename="{constant.DEMONA_CHART_FILE_NAME_S3}"',  # Optional: for inline display
    },
        "body": base64.b64encode(data),
        "isBase64Encoded": True
    }


def get_records_current(event, context):
    data = connector.get_current_server_stats()
    return {"statusCode": 200, "headers": constant.HEADERS, "body": json.dumps(data, cls=util.DecimalEncoder)}

