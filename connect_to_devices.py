"""
I have 2 solutions for this problem.
1. Use netmiko and Asyncio to set up concurrent sessions.
2. Use parallel-ssh, which is a python package, written for the same purpose. Unfortunately this package doesn't work well when different usernames
   and passwords are used. So for the sake of this exercise, let us assume all the devices use the same user/pass combination.
"""
import json, asyncio
from device import Device
from pssh.pssh_client import ParallelSSHClient
device_dict = {}
with open('device_data.json', 'r') as f:
    json_out = json.loads(f.read())

def connect_using_async():
    """
    This method uses netmiko to connect to SSH to the servers.
    To run mulitple SSH sessions concurrently, I used asyncio
    """
    for item in json_out['device_list']:
        device_dict['%s' %(item['hostname'])] = Device(
                address = item['address'],
                host = item['hostname'],
                username = item['username'],
                password = item['password'],
                port = item['port'],
                commands = json_out['commands']
            )
            
    @asyncio.coroutine
    def my_coroutine(server,*args):
        print('{0} Connecting ...'.format(server.host))
            #print('{0} sleeping for: {1} seconds'.format(task_name, seconds_to_sleep))
        server.execute()
    
    loop = asyncio.get_event_loop()
    tasks = [my_coroutine(v) for k,v in device_dict.items()]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

def connect_using_pssh():
    """
    This method uses parallel-ssh package to connect to the devices
    """
    device_list = [item['address'] for item in json_out['device_list']]
    user = set([item['username'] for item in json_out['device_list']]).pop()
    password = set([item['password'] for item in json_out['device_list']]).pop()
    client = ParallelSSHClient(device_list, user=user, password=password)
    output = client.run_command('whoami')
    for host, host_output in output.items():
        for line in host_output:
                print(line)

if __name__=='__main__':
    connect_using_async()
    connect_using_pssh()
