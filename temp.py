# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
from mcpi.minecraft import Minecraft
block=0
mc=Minecraft.create('anorfire.club')
mc.postToChat('jason')
uuid=mc.getPlayerEntityId('JASON')

while 1:
     block=random.randint(1,8)
     x,y,z=mc.entity.getTilePos(uuid)
     mc.setBlocks(x,y,z,x+5,y,z+5,38,block)