#!/usr/bin/python3
import os
import sys

import love
import shock

def reward():
    love.vibe(time=1,power=5)
def punish():
    shock.shock(intensity=15,duration=2)

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('No arguments supplied')
        exit(1)
    args = sys.argv[1:]
    if args[0] == '-s':
        args = args[1:]
        return_code = args[-1]
    else:
        return_code = os.system(' '.join(sys.argv[1:]))

    # mommy returns immediately
    os.system('mommy -s ' + str(return_code))

    # reward and punish take a while
    if int(return_code) == 0:
        reward()
    else:
        punish()

