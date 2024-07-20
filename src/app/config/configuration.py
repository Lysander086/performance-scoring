import os


class Config:
    def __init__(self):
        # in my case , the cwd is defined in the launch.json
        self.resource_dir = os.path.join( os.getcwd(), 'resources')
        