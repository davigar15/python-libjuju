"""
This example:

1. Connects to current controller.
2. Gets the cloud by name
3. Disconnects from the controller

"""
import logging
import pdb

from juju import loop
from juju.controller import Controller


async def main():
    controller = Controller()
    await controller.connect()

    cloud1 = await controller.cloud('myk8scloud')
    cloud2 = await controller.cloud()
    print(cloud1, cloud2)

    pdb.set_trace()

    await controller.disconnect()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    ws_logger = logging.getLogger('websockets.protocol')
    ws_logger.setLevel(logging.INFO)
    loop.run(main())
