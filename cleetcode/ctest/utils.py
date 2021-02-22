import inspect


def decorator_default(method_name, class_name="Solution"):
    def decorator(func):
        def decorated(*args, **kwargs):

            kws = dict(class_name=class_name, method_name=method_name)

            signature = inspect.signature(func)
            for key, value in signature.parameters.items():
                if value.default and (value.default != inspect._empty):
                    kws.update({key: value.default})

            kws.update(kwargs)

            for a, b in zip(args, signature.parameters):
                kws.update({b: a})

            new_kws = dict()
            for key, value in kws.items():
                new_kws.update({key: value if isinstance(value, str) else value.__name__})

            new_args = list()
            for i, a, b in zip(range(max(len(args), len(signature.parameters))), args, signature.parameters):
                new_args.append(new_kws[b])
                new_kws.pop(b)

            return func(*new_args, **new_kws)

        return decorated
    return decorator
