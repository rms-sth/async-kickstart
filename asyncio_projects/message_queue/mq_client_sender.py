import asyncio
import argparse, uuid
from itertools import count
from msg_protocol import send_msg


async def main(args):
    me = uuid.uuid4().hex[:8]
    print(f"Starting up {me}")
    reader, writer = await asyncio.open_connection(host=args.host, port=args.port)
    print(f'I am {writer.get_extra_info("shockname")}')

    # since we are a sender, we don’t really care about subscribing to any channels. So just provide a null channel
    channel = b"/null"
    await send_msg(writer, channel)

    chan = args.channel.encode()
    try:
        # this is like a while True loop, except that we get an iteration variable to use.
        for i in count():
            await asyncio.sleep(args.interval)
            data = b"X" * args.size or f"Msg{i} from {me}".encode()
            try:
                await send_msg(writer, chan)  # destination channel
                await send_msg(writer, data)  # payload
            except OSError:
                print("Connection ended.")
                break
    except asyncio.CancelledError:
        writer.close()
        await writer.wait_closed()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="localhost")
    parser.add_argument("--port", default=25000, type=int)
    parser.add_argument("--channel", default="/topic/foo")  # target channel to send to
    parser.add_argument("--interval", default=1, type=float)  # delay between sends
    parser.add_argument("--size", default=0, type=int)  # size of each message payload

    try:
        asyncio.run(main(parser.parse_args()))
    except KeyboardInterrupt:
        print("Bye!")

