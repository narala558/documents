import bluetooth


devices = bluetooth.discover_devices(lookup_names=True)

from pprint import pprint; pprint(devices)

# for addr, name in devices:
#     for services in bluetooth.find_service(address=addr):
#         from pprint import pprint; pprint(services)
