import sys
import time
import asyncio
import json
import zmq


def publish_filename(fname):
    try:
        print("publish_string: %s", fname)
        word_ = {
            "word": fname
        }
        # convert into JSON:
        jsondata_string = json.dumps(word_)
        socket.send_string(jsondata_string)
        return True
    except Exception as e:
        print("data_publisher exception!", e)
        return False


def main():
    try:
        publish_filename(str(sys.argv[1]))
    except (KeyboardInterrupt, SystemExit, IndexError):
        print("Usage %s <test? == y> for test controller in atm")
        pass


if __name__ == '__main__':
    try:
        context = zmq.Context()
        socket = context.socket(zmq.PUB)
        socket.bind("tcp://*:%s" % 6868)
        print("wait 3 seconds...")
        time.sleep(3)
    except (KeyboardInterrupt, SystemExit):
        pass
    main()
