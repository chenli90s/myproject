import yaml


def main():
    with open('manifest.yml', 'r')as f:
        data = yaml.load(f)
        print(data)

if __name__ == '__main__':
    main()