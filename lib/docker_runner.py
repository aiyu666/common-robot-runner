import docker
from lib import message

class DockerRunner(object):

    def __init__(self):
        self.client = docker.from_env()
        self.message = message
    
    def pull_image(self, image_name):
        self.client.images.pull(image_name)
        self.message.info_message('Pull robot-runner image successfully.')

    def start_container(self, container_name):
        try:
            container = self.client.containers.get(container_name)
            container.start()
            self.message.show_cmd(['docker', 'start', container_name])
        except Exception as e:
            self.message.warn_msg(
                ['docker', 'start', 'fail', 'with', '{}'.format(str(e))])

    def run(self, container_name, path, image_name):
        environment = ['TZ=Asia/Taipei']
        volumes = {
            '/var/run/docker.sock': {
                'bind': '/var/run/docker.sock', 'mode': 'rw'},
            path: {
                'bind': '/home/robot', 'mode': 'rw'}
        }

        container = self.client.containers.run(
            image_name, detach=True, environment=environment, name=container_name, network_mode='host', stdin_open=True, volumes=volumes)
        self.message.show_msg([image_name, 'container start.'])
        print(container.id, container.name)

    def remove_container(self, container_name):
        try:
            container = self.client.containers.get(container_name)
            container.remove(force=True)
            self.message.show_cmd(['docker', 'rm', '-f', container_name])
        except Exception as e:
            self.message.warn_msg(
                ['docker', 'remove containers', 'fail', 'with', '{}'.format(str(e))])
