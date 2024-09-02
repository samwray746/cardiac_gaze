import psychopy
from psychopy import visual 
import os.path as op

def create_experimental_stimuli(win):
  
    ### COLOURS ### 
    grey = '#808080'
    green = '#008000'
    yellow = '#FFFF00'
    
    ### FIXATION DOT ### 
     
    fixation_dot_grey = visual.Circle(
    win=win,         
    radius=0.05,     
    fillColor=grey, 
    lineColor=grey)

    fixation_dot_green = visual.Circle(
    win=win,         
    radius=0.05,     
    fillColor=green, 
    lineColor=green)

    fixation_dot_yellow = visual.Circle(
    win=win,         
    radius=0.05,     
    fillColor=yellow, 
    lineColor=yellow)

    ### INSTRUCTIONS ### 

    training_instructions_one = visual.TextStim(win, text='Welcome to the task!\n\nDuring the task, you will need to look at a fixation 'dot' in the centre of the screen.\n\n\nPress spacebar to continue.', height = 25)
    training_instructions_two = visual.TextStim(win, text='While you are looking at the dot, stimuli will be briefly presented to the left or right of the dot.\n\n\nPress spacebar to continue.', height = 25)
    training_instructions_three = visual.TextStim(win, text='Even when you notice the stimuli being presented, please continue to look at the dot.\n\n\nPress spacebar to continue.', height = 25)
    training_instructions_four = visual.TextStim(win, text='These are examples of the stimuli that will be presented.\n\nNote that the stimuli are rotated slightly clockwise or anticlockwise from vertical.\n\n\nPress spacebar to continue.', height = 25)
    training_instructions_five = visual.TextStim(win, text='After the presentation of a stimulus, you will need to quickly judge whether it was rotated clockwise or anticlockwise.\n\n\nUse the arrow keys to make your response (left = anticlockwise, right = clockwise).', height = 25)
    training_instructions_six = visual.TextStim(win, text='When the fixation dot is GREEN, the stimulus could be presented at any time (so pay attention!).\n\nWhen the dot turns YELLOW, you need to make your response', height = 25)
    training_instructions_seven = visual.TextStim(win, text='The experiment consists of 3 blocks. You can take a break in-between blocks.\n\n\nPress the spacebar to continue.', height = 25)
    training_instructions_eight = visual.TextStim(win, text='If you have any questions, ask the researcher now.\n\n\nPress the spacebar to continue.', height = 25)
    training_instructions_nine = visual.TextStim(win, text="Let's do a few training trials.\n\n\nPress the spacebar to continue.", height = 25)

    training_complete = visual.TextStim(win, text="Training block complete. Well done!\n\n\nIf you have any questions, ask the researcher now. Otherwise, press spacebar to start the first experimental block.", height = 25)
    block_complete = visual.TextStim(win, text="Experimental block complete. Well done!\n\n\nTake a rest, and press the spacebar to begin the next block.", height = 25)

    correct_response = visual.TextStim(win, text="Correct!", height = 25)
    incorrect_response = visual.TextStim(win, text="Incorrect!", height = 25)
    too_late = visual.TextStim(win, text="Too late", height = 25)

    return fixation_dot_grey, fixation_dot_green, fixation_dot_yellow, training_instructions_one, training_instructions_two, training_instructions_three, training_instructions_four, training_instructions_five, training_instructions_six, training_instructions_seven, training_instructions_eight, training_instructions_nine, training_complete, block_complete, correct_response, incorrect_response, too_late
    

    
