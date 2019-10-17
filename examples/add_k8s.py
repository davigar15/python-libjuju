"""
This example:

Requirements:
```
sudo snap install microk8s --channel 1.14/stable --classic
sudo usermod -a -G microk8s $USER
newgrp microk8s
microk8s.status --wait-ready
microk8s.enable storage dns
```

1. Connects to current controller.
2. Adds a new k8s cloud to the current controller
3. Disconnects from the controller

"""
import logging

from juju import loop
from juju.controller import Controller
from juju.client import client
import time
import subprocess
import yaml

async def main(kube_config):
    cloud_name = 'microk8s'
    model_name = 'test2'
   
    controller = Controller()
    # connect to current controller with current user, per Juju CLI
    await controller.connect()
    
    config = yaml.safe_load(kube_config)
    cacert_data = config['clusters'][0]['cluster']['certificate-authority-data']
    endpoint = config['clusters'][0]['cluster']['server']
    credential_name = config['users'][0]['name']
    username = config['users'][0]['user']['username']
    password = config['users'][0]['user']['password']

    # await controller.add_k8s(
    #     cloud_name,
    #     cacert_data=cacert_data,
    #     endpoint=endpoint,
    #     credential_name=credential_name,
    #     username=username,
    #     password=password,
    #     operator_storage='ebs-1',
    #     workload_storage='ebs-1'
    # )

    model = await controller.add_model(
        model_name,
        cloud_name=cloud_name,
        # credential_name='admin'
    )

    applications = await model.deploy(
            'cs:osm',
            channel='stable',
        )
    # time.sleep(60)

    # await controller.destroy_models(
    #     model_name,
    #     destroy_storage=True
    # )

    # while model_name in await controller.list_models():
    #     time.sleep(5)
    # time.sleep(5)
    # error = await controller.remove_cloud([cloud_name])

    import pdb; pdb.set_trace()
    await controller.disconnect()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    ws_logger = logging.getLogger('websockets.protocol')
    ws_logger.setLevel(logging.INFO)
    import subprocess
    kubeconfig = subprocess.check_output(['/bin/bash', '-c', 'cat ~/.kube/config'])
    loop.run(main(kubeconfig))
