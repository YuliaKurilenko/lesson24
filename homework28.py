import inspect
from pprint import pprint
def introspection_info(obj):
    type_ = type(obj).__name__
    attribute = dir(obj)
    methods = [method for method in attribute if callable(getattr(obj, method))]
    module = obj.__class__.__module__
    func = inspect.isfunction(obj)
    info = {'type': type_, 'attributes': attribute, 'methods': methods, 'module': module, 'function': func}
    return info
number_info = introspection_info(42)
pprint(number_info)