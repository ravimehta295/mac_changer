import os

def change():
    new_mac = "00:11:22:33:44:55"
    os.system("ifconfig")
    commands = "ifconfig eth0 hw ether" +new_mac
    os.system("ifconfig eth0 down")
    os.system(commands)
    os.system("ifconfig eth0 up")
    os.system("ifconfig")

if __name__ == '__main__':
    change()