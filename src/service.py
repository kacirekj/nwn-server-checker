from datetime import datetime

from src import dao, connector, util, s3, constant


def update_records(event, context):
    stats = connector.get_current_server_stats()
    data = {
        **stats,
        'timestamp': datetime.now().isoformat()
    }
    item = dao.store(data)
    items = dao.find()

    image = util.plot(items)
    ret = s3.save_image_public(constant.DEMONA_CHART_FILE_NAME_S3, image)
    return {"statusCode": 200, "body": item}
