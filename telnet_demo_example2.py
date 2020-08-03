import asyncio
from asyncio import StreamReader, StreamWriter


async def send_event(msg: str):
    """
    Pretend that this coroutine actually contacts an external server to submit event notifications.

    Args:
        msg (str): message sent to each external source
    """
    await asyncio.sleep(1)


async def echo(reader: StreamReader, writer: StreamWriter):
    print("New connection")
    try:
        while data := await reader.readline():
            writer.write(data.upper())
            await writer.drain()
        print("Leaving Connection")

    except asyncio.CancelledError:
        message = "Connection dropped"
        print(message)
        asyncio.create_task(send_event(message))
        # Because the event notifier involves network access, it is common for such calls to
        # be made in a separate async task; that’s why we’re using the create_task() function
        # here.


async def main(host="127.0.0.1", port=8889):
    server = await asyncio.start_server(echo, host, port)
    async with server:
        await server.serve_forever()


try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Bye!")


####################### To Start Server ####################
# 1) Terminal 1 :
# python telnet_demo.py

# 2) Terminal 2:
# telnet 127.0.0.1 8889
