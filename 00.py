#! /usr/bin/env python2

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals
from base import *  # stubs so that the code below works


# La clase que tenemos y un ejemplo de uso

import time

class Cyborg(object):

    def __init__(self, name):
        self.name = name
        self.weapon = DeathRay(ammunition=25)
        self.teleporter = TimeMachine()

    def travel(self, destination, year):
        self.teleporter.go(destination, year)
        time.sleep(0.25)  # not instant, but almost

    def attack(self, target):
        self.weapon.vaporize(target)

# Lo ejecutamos... y no pasa nada, claro
robot = Cyborg('T-1000')
robot.travel('Los Angeles', 1995)
robot.attack('Sarah Connor')
robot.attack('John Connor')
