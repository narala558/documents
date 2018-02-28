import sys
import time


registry = {}


def register_class(target_class):
    registry[target_class.__name__] = target_class
    print('Class {} registered'.format(target_class))


class MetaRegistry(type):
    def __new__(meta, name, bases, class_dict):
        name = 'Magic_{}'.format(name)
        cls = type.__new__(meta, name, bases, class_dict)
        print(meta, name, bases, class_dict, cls)
        if name not in registry:
            register_class(cls)
        return cls


class BaseClass(metaclass=MetaRegistry):
    pass


class Foo(BaseClass):
    pass


class BaseClass:
    def __init_subclass__(cls, **kwargs):
        if cls not in registry:
            register_class(cls)
        super().__init_subclass__(**kwargs)


# class BaseClass():
#     pass


class Foo(BaseClass):
    pass


class Bar(BaseClass):
    pass


class Baz(Bar):
    pass


def subclasses(cls, registry=None):
    if registry is None:
        registry = set()

    subs = cls.__subclasses__()

    for sub in subs:
        if sub in registry:
            return
        registry.add(sub)
        yield sub
        for sub in subclasses(sub, registry):
            yield sub


# registry = {cls.__name__: cls for cls in subclasses(BaseClass)}
print(registry)


# if len(sys.argv) != 1:
#     while True:
#         print(registry)
#         time.sleep(1)


class PluginBase:
    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)


class FooPlugin(PluginBase):
    pass


print(PluginBase.subclasses)
