import os
import json
from lib import message

class FilterTestCase(object):
    
    @staticmethod
    def fetch_config(rootPath, project):
        with open(os.path.join(rootPath, project, '.robot-runner', 'config.json')) as data_file:
            data = json.load(data_file)
            
        return data

    @staticmethod
    def check_test_status(include_tag, exclude_tag, sub_project):
        should_do_testing = True
        if include_tag is not None:
            if sub_project['tag'] not in include_tag:
                should_do_testing = False
        if exclude_tag is not None:
            if sub_project['tag'] in exclude_tag:
                should_do_testing = False
        if should_do_testing:
            message.info_message("Found the {} tag, preparing {} test".format(
                include_tag[0], sub_project['name']))

        return should_do_testing
    
    @staticmethod
    def convert_option(options):
        option_array = []
        for option in options:
            option_array.append(
                {'option': option.split("=")[0], 'value': option.split("=")[1]})
        
        return option_array