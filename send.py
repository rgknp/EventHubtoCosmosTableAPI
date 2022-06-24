import asyncio
from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData

async def run():
    # Create a producer client to send messages to the event hub.
    # Specify a connection string to your event hubs namespace and
    # the event hub name.
    producer = EventHubProducerClient.from_connection_string(conn_str="Endpoint=sb://eventhubsourcesample.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=BXsDZWuV5vrPsJ2YHRHu1sUNcp2MHfH/mpT8Ebd/Dhc=", eventhub_name="samples-workitems")
    async with producer:
        # Create a batch.
        event_data_batch = await producer.create_batch()

        # Add events to the batch.
        #event_data_batch.add(EventData('''{"key":"20845B65BCB9583F41B4541458AD47E6","val":"1 Prestige Room - Rate Breakup"}'''))
        #event_data_batch.add(EventData('''{"key":"20845B65BCB9583F41B4541458AD47E7","val":"2 Prestige Room - Rate Breakup"}'''))
        #event_data_batch.add(EventData('''{"key":"20845B65BCB9583F41B4541458AD47E8","val":"3 Prestige Room - Rate Breakup"}'''))
        #event_data_batch.add(EventData('''{"key": "ABE72B20D2B4A920B5B236451562CCD1", "val": " 1 Double Bed Nonsmoking - AdvancePurchase - Expedia Special Rate - Rate Breakup: { Sat:[175 USD]}USD"}'''))

        # Send the batch of events to the event hub.
        await producer.send_batch(event_data_batch)

loop = asyncio.get_event_loop()
loop.run_until_complete(run())