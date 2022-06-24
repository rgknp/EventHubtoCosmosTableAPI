from encodings import utf_8
import logging
import azure.functions as func
import uuid
import json

def main(event: func.EventHubEvent, message: func.Out[str]):
    logging.info(f'Function triggered to process a message: {event.get_body().decode()}')
    #logging.info(f'  EnqueuedTimeUtc = {event.enqueued_time}')
    #logging.info(f'  SequenceNumber = {event.sequence_number}')
    #logging.info(f'  Offset = {event.offset}')

    # {"key":"20845B65BCB9583F41B4541458AD47E8","val":"3 Prestige Room - Rate Breakup"}
    # Metadata
    #for key in event.metadata:
    #    logging.info(f'Metadata: {key} = {event.metadata[key]}')

    jsonData = json.loads(event.get_body().decode())

    rowKey = jsonData["key"]
    eventVal = jsonData["val"]

    logging.info(f'rowKey: {rowKey}')
    logging.info(f'eventVal: {eventVal}')

    # rowKey = str(uuid.uuid4())

    data = {
        "PartitionKey": "message",
        "RowKey": rowKey,
        "val": eventVal
    }

    message.set(json.dumps(data))
