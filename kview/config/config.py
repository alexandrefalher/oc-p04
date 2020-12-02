import yaml


class Config:

    def __init__(self, path: str):
        self.__configFilePath: str = path
        self.__configs: dict = dict()
        self.__read_config()

    def get_config(self, key: str) -> any:
        return self.__configs[key]

    def __read_config(self):
        with open(self.__configFilePath, 'r') as rawConfigFile:
            try:
                self.__configs = yaml.load(rawConfigFile)
            except OSError:
                print("The file 'config.yaml' is not accessible. It must be placed in the root directory.")
            except Exception:
                print("An unexpected error occured in: ConfigFile.__ReadConfig")
