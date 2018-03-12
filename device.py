from netmiko import ConnectHandler
class Device:
    """
    Device class uses python netmiko package to connect and execute commands on the server
    """
    def __init__(self, address, host, commands=[], device_type='linux', port=22, username='root', password='cisco123'):
        """
        address: IPv4 address of the server
        host: hostname of the server
        commands: list of commands to execute on servers
        device_type: default set to linux, netmiko can also be used to ssh to routers from different vendors
        username: username
        password: password
        """
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.address = address
        self.device_type = device_type
        self.commands = commands

    def execute(self, num_retries=3):
        """
        connect the router via netmiko and holds the session id
        """
        connect_dict = dict()        
        connect_dict['ip'] = self.address
        connect_dict['username'] = self.username
        connect_dict['password'] = self.password
        connect_dict['port'] = self.port
        connect_dict['device_type'] = self.device_type
        try_counter = 1
        import pdb ; pdb.set_trace()
        while try_counter <= num_retries:
            try:
                client = ConnectHandler(**connect_dict)
                break
            except Exception as e:
                print("Connect failed at try {} - {}".format(try_counter, repr(e)))
                try_counter += 1                
        else:
            raise ConnectFailed("Unable to connect router even after {} tries".format(num_retries))
        for cmd in self.commands:
            print (client.send_command(cmd))
