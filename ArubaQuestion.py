__author__ = 'bhushan'

input_string = "server1.aruba.com,10.2.1.1,2,30;server2.aruba.com,10.2.1.2,2,30;server3.aruba.com,10.2.1.1,1,50"

class server:
    def __init__(self, name, ip, priority, ttl):
        self.name = name
        self.ip = ip
        self.priority = priority
        self.ttl = ttl



