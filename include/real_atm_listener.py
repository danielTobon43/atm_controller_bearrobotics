import asyncio
import zmq
import time
import json
import atexit

import controller

##############
# import dataq_to_standard as ds
# import standard_to_plotly as sp

async def req_listener():
    try:
        while(1):
            message = socket.recv_string()
            jsonstr_res = json.loads(message)
            print( json.dumps(jsonstr_res, indent=2))
            answ = jsonstr_res["word"]
            print("test atm controller?:" ,answ)
            if answ == 'y':
                print("controller...")
                controller.test_controller()
            else:
                time.sleep(3)
    except Exception as e:
        print(e)


def do_on_exit():
    print("Stopping atm-interface gracefully")
    socket.close()

def main():
    try:
        loop.run_until_complete(req_listener())
        loop.close()
        while(True):
            #the main program goes here
            print("main")
            time.sleep(10)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    try:
        atexit.register(do_on_exit)
        context = zmq.Context()
        socket = context.socket(zmq.SUB)
        socket.connect("tcp://localhost:%s" % 6868)
        socket.subscribe("")  # Subscribe to all topics
        loop = asyncio.get_event_loop()
    except (KeyboardInterrupt, SystemExit):
        pass
    main()
