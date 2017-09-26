from subprocess import check_call


def call_command(cmd):
    check_call(cmd, shell=True)
