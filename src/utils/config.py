
import pathlib

from collections import UserDict

import tomli as tomllib


class Config(UserDict):

    def load(self, file):
        import yaml
        if file is None:
            if pathlib.Path('data/config.yaml').exists():
                file = open('data/config.yaml', 'rb')
            else:
                raise FileNotFoundError('未找到配置文件，请先创建配置文件')
        with file as stream:
            if file.name.endswith('.toml'):
                self.data = tomllib.load(stream)
            else:
                self.data = yaml.load(stream, Loader=yaml.FullLoader)



config = Config()
