from importlib import import_module


class Activator(object):
    @staticmethod
    def get_instance(entity):
        class_str: str = entity
        try:
            module_path, class_name = class_str.rsplit('.', 1)
            module = import_module(module_path)
            return getattr(module, class_name)
        except (ImportError, AttributeError) as e:
            raise ImportError(class_str)
