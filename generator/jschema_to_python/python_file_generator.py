import os


class PythonFileGenerator(object):
    def __init__(self, output_directory):
        self.output_directory = output_directory

    def make_output_file_path(self, file_name):
        return os.path.join(self.output_directory, file_name)
