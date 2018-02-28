import Pyro4


@Pyro4.expose
class GreetingMaker(object):
    def get_fortune(self, name):
        return "Hello, {0}".format(name)


daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()

uri = daemon.register(GreetingMaker)
ns.register("pavillion.greeting", uri)


print("Ready.")
daemon.requestLoop()
