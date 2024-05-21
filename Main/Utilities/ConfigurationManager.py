import os.path


class ConfigurationManager:
    _config = {}

    @classmethod
    def load_config(cls, config_file='configuration.properties'):
        project_path = os.path.dirname(os.getcwd())
        config_path = os.path.join(project_path, config_file)
        if not cls._config:
            with open(config_path, 'r') as config_file:
                for line in config_file:
                    if line.strip() and not line.startswith('#'):
                        key, value = line.split('=', 1)
                        cls._config[key.strip()] = value.strip()
        return cls._config

    @classmethod
    def get_config_value(cls, key):
        if not cls._config:
            cls.load_config()
        return cls._config.get(key)
