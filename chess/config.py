import yaml


class Config:

    def __init__(self, path=None):
        self.__defaultConfigFilePath: str = "chess/config.yaml"
        self.__set_config_file_path(path)
        self.__configs: dict = dict()
        self.__read_config()

    def get_config(self, key: str) -> any:
        return self.__configs[key]

    def __set_config_file_path(self, path):
        if path is None:
            self.configFilePath: str = self.__defaultConfigFilePath
        else:
            self.configFilePath: str = path

    def __read_config(self):
        with open(self.configFilePath, 'r') as rawConfigFile:
            try:
                self.__configs = yaml.load(rawConfigFile)
            except OSError:
                print("The file 'config.yaml' is not accessible. It must be placed in the root directory.")
            except Exception:
                print("An unexpected error occured in: ConfigFile.__ReadConfig")