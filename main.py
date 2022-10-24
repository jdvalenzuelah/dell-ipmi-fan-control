from sys import argv
from fancontrol import enable_fancontrol
from fancontrol import set_manual_fanspeed

def print_usage():
    print('usage:\n\nmain.py FANSPEED \n\n\tFANSPEED: Int (between 0 and 100)')

def main(speed):
    print('enabling manual fan control')
    if(not enable_fancontrol()):
        print('enabled manual fan control')
        print('setting fan speed to {speed}')
        set_manual_fanspeed(speed)
        print('fan speed set to {speed}')
    else:
        print('Fatal error')

if __name__ == "__main__":
    if(len(argv) == 1 or not argv[1].isnumeric()):
        print_usage()
    else:
        main(int(argv[1]))



