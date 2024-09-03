# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 14:21:15 2024

@author: bsms9zh8
"""

from psychopy import event 

def instructions(training_instructions_one, training_instructions_two, training_instructions_three, training_instructions_four, training_instructions_five, training_instructions_six, training_instructions_seven, training_instructions_eight, training_instructions_nine, win):
    training_instructions_one.draw()
    win.flip()
    event.waitKeys(keyList=['space'])
    win.flip()
    training_instructions_two.draw()
    win.flip()
    event.waitKeys(keyList=['space'])
    win.flip()
    training_instructions_three.draw()
    win.flip()
    event.waitKeys(keyList=['space'])
    win.flip()
    training_instructions_four.draw()
    win.flip()
    event.waitKeys(keyList=['space'])
    win.flip()
    training_instructions_five.draw()
    win.flip()
    event.waitKeys(keyList=['space'])
    win.flip()
    training_instructions_six.draw()
    win.flip()
    event.waitKeys(keyList=['space'])
    win.flip()
    training_instructions_seven.draw()
    win.flip()
    event.waitKeys(keyList=['space'])
    win.flip()
    training_instructions_eight.draw()
    win.flip()
    event.waitKeys(keyList=['space'])
    win.flip()
    training_instructions_nine.draw()  
    win.flip()
    event.waitKeys(keyList=['space'])
    win.flip()
