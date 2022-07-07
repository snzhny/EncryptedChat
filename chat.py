try:
    import socket, sys, time, tor
except ModuleNotFoundError:
    from subprocess import call
    modules = ["tor"]
    call("pip install " + ' '.join(modules), shell=True)
finally:
    pass
