"""
This example:

1. Connects to current controller.
2. Creates a new model.
3. Deploys an application on the new model.
4. Disconnects from the model
5. Destroys the model

"""
import logging
import asyncio
from juju.controller import Controller
from juju import loop

async def deploy_ubuntu(controller, model=None):
    model = await controller.add_model(model)
    await model.deploy(
        "ubuntu-0",
        application_name='ubuntu',
        series='trusty',
        channel='stable',
    )
async def main():
    controller = Controller()
    # connect to current controller with current user, per Juju CLI
    print(1)
    await controller.connect(
        endpoint="10.199.130.6:17070",
        username="admin",
        password="36ce0005d38406c16ce75da9a041112c",
        cacert="""-----BEGIN CERTIFICATE-----
MIIErTCCAxWgAwIBAgIVAKN6xwdjdkWq/htq1YgUh1XSa+u2MA0GCSqGSIb3DQEB
CwUAMG4xDTALBgNVBAoTBGp1anUxLjAsBgNVBAMMJWp1anUtZ2VuZXJhdGVkIENB
IGZvciBtb2RlbCAianVqdS1jYSIxLTArBgNVBAUTJDE0NzhiY2MzLWQwNjYtNDM2
Ni04MDZjLTZhNzE0ZTU1ZjczYTAeFw0yMDA0MjkwODM5NTdaFw0zMDA1MDYwODM5
NTZaMG4xDTALBgNVBAoTBGp1anUxLjAsBgNVBAMMJWp1anUtZ2VuZXJhdGVkIENB
IGZvciBtb2RlbCAianVqdS1jYSIxLTArBgNVBAUTJDE0NzhiY2MzLWQwNjYtNDM2
Ni04MDZjLTZhNzE0ZTU1ZjczYTCCAaIwDQYJKoZIhvcNAQEBBQADggGPADCCAYoC
ggGBAKdF57Fw5BvQpAgtVTmTMgPqMsVR+rRDyhefWIws7UsnJN2WsrOZwDSWPqrx
3t5o//wLcRHCz82JLV0bGdwITsVxdFWGsaomT/SWl98KcEo1tZbNzsHZHAj/yH2t
ytjz9ZSwrOE4oypRdJHhnUB5zZDJrq4RWBFoYhN8Q6H1bN1IlRrWc0wVe/quQV2k
5Lhk7afb5yW3vXrbLQ74xiOvhsxQVAhN1vRC8rDyS1YwiyeHrd6pc/i7gVluZAlD
PvbVObVRS+pSoxtZFqxhGOdu/u69TIpRc8feTW1fgn+cfqI0e4Oy4gisgQOkqoOW
6ISdSNp5iFmes7SYt6tNto/yQxYQ28/zuXglAnUlhwataJaDLQ6oMiPPfMcWtAtZ
H6jhGOw+tO1rJMjBol+9jjXU/e89oXllJDUotHsn/OulOtykQZf9gAFk1JgegZsh
a1N4s5lKvcRUFDyzFXT9xsYnn1Eb6HOYwn1dTCXJhyQ+MGjsB9dBVLbru+UdOoJN
Q6Rp9wIDAQABo0IwQDAOBgNVHQ8BAf8EBAMCAqQwDwYDVR0TAQH/BAUwAwEB/zAd
BgNVHQ4EFgQUfMfdBE3wbxT58Vvx9CTATTLORd0wDQYJKoZIhvcNAQELBQADggGB
AB2Tk55FmNdSlEmTQ8z9oCJ7gCj8VQzBjPxxTYirBDU1ULiCAEinZ120hweLhf2t
XHaXnAwh3dQRfJysZu8mUktt+WFBUFuH/xW+sbPypxr5JHKMX0GHud2J60cXQr29
aeUxhIguxCKZi1RfnM6IoMxtb00yA+HlgEv7azNimWnk93Nu934DzYEXY2qYL9ip
LYkj/sbUqA1JZF7JFFYeoOwApv1+zMk0+s8etbSALPpV4AaOpkm3IeR/bL63fcUk
BUCeZtNs7t0l0XWPX5lmLzuXLkcf1X3dvtOVQN5gVlsZax+9ic3KI1yrsAenCwQj
kmW1Q1VVfERzv+6EOMnLgcWeWZLKIGkREKxj41xpdGhnCcssPEJPYqhvZQKy0Tqo
aIJdEIoADKYvr64NERpYwBe15YN5BOrD+rUgOjnoc7jFgqmWfnbf7lwjLLEZsIJP
pEhNRS6wjMO+G1tT3xTN2gBgA6S+t7ixu0knmou1D0TCeJbIlVnhTDZwA0AtpRV6
lw==
-----END CERTIFICATE-----"""
    )
    print(1)
    # model = await controller.add_model("test")
    # await model.disconnect()
    # await controller.destroy_model(model.info.uuid)
    while True:
        # application = await model.deploy("ubuntu")
        # model="test"
        # import pdb; pdb.set_trace()
        # await deploy_ubuntu(controller, model=model)
        # import pdb; pdb.set_trace()
        await asyncio.sleep(1)
        # print([e for (e, cacert) in controller.connection().endpoints])
        # print(controller.connection().endpoint)
        # print(controller.connection().is_open)
        # print(controller.connection().connect_params())

    await controller.disconnect()

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    ws_logger = logging.getLogger('websockets.protocol')
    ws_logger.setLevel(logging.INFO)
    loop.run(main())
