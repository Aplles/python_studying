import os


def export_vars(request):
    data = {'DEBUG': os.environ['DEBUG']}
    return data
