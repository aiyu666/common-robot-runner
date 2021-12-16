import fire
import os
from lib.robot_runner import RobotRunner
from lib.docker_runner import DockerRunner
from lib.resource_name import ResourceName
from lib.filter_testcase import FilterTestCase
from settings import *

def robot(project_name, docker_skip, path, include_tag, exclude_tag, retry_count, robot_option, browser) -> None:

    # Check project existing
    projects = os.listdir(path)
    if project_name not in projects:
        print(f'{project_name} is not in directory')
        exit()

    project_config = FilterTestCase.fetch_config(path, project_name)

    for sub_project in project_config['sub_project']:
        test_flag = FilterTestCase.check_test_status(
                include_tag, exclude_tag, sub_project
        )
        options_list = FilterTestCase.convert_option(robot_option)

        if test_flag:
            if docker_skip == False:
                docker_runner = DockerRunner()
                image_name = DOCKERFILE_LIST['testing']
                docker_runner.pull_image(image_name)
                random_str = ResourceName.id_generator()
                container_name = f'testing-{random_str}'
                docker_runner.run(container_name, path, image_name)
            else:
                container_name = None

            robot_runner = RobotRunner(project_name=project_name, robot_option=options_list, container_name=container_name, browser=browser, test_type=sub_project['name'], docker_skip=docker_skip)
            result_code = robot_runner.run_test()
            
            if isinstance(result_code, bool) and result_code == False:
                robot_runner.retest(retry_count)
            
            if docker_skip == False:
                docker_runner.remove_container(container_name)

def pytest():
    print('test2')


if __name__ == '__main__':
    fire.Fire({
        "robot": robot,
        "pytest": pytest
    })