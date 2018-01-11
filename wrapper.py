import functools


def watch_instance_param(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(args[0].instance_id)
        return func(*args, **kwargs)
    return wrapper


if __name__ == '__main__':

    @watch_instance_param(1234)
    def main():
        print('hhaha')

    main()