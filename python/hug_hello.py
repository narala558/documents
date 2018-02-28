import hug


@hug.get('/login')
def login(request, response):
    return 'failed'


if __name__ == '__main__':
    login.interface.api()
