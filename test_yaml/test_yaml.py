from yaml import load, dump

def test_yaml():
    env = {
        "docker.testing-studio.com":{
            "dev": "1.1.1.1.",
            "test": "1.1.1.2"
        },
        "default": "dev"
    }

    print(env)
    print(dump(env))

    # yaml_str="""
    # default:dev
    # docker.testing-studio.com:
    # dev:1.1.1.100
    # test:1.1.1.200
    # """

   # print(load(yaml_str))


    f = open("demo.yaml","w")
    print(dump(env, f))


def add():
    a = 1
    b = 2
    c = a + b
    print(c)