# This is the main script for a task in which Gabor patches are presented at systole/diastole. Some details: 
# - A fixation dot is presented centrally on the screen throughout the task (0.2 degree size)
# - During each trial, a Gabor patch (2 degree size) is presented at a 4 degree eccentricity from the fixation dot 
# - The Gabor patch can either be high-frequency (6 cpd) or low-frequency (3 cpd) 
# - During each trial, the Gabor patch will be presented after an R-peak sensing period at systole/diastole for 40ms 
# - After Gabor patch presentation there will be an ISI of 2-3 seconds
# - When the fixation dot turns yellow, participants respond according to whether the Gabor patch was tilted clockwise or counterclockwise (1.5s)
# - Then, another inter-trial interval of 2-3 seconds 
# - In total, there are 3 blocks of 60 trials. Each block will have 15 HF-S/LF-S/HF-D/LF-D
# - The degree of orientation of the Gabor patch will be adjusted trial-by-trial to maintain a constant performance of 75% accuracy

# The trial type will be psuedorandomised, a non-consecutive random choice of the 4 trial types from a list of 4 (that is refreshed every 4 trials)

import psychopy
import os.path as op
from psychopy import event, visual, gui, core
from statistics import mean

from intart_functions import sendParallelTrigger, readParallelTrigger
from create_stimuli_function import create_experiment_stimuli
from experimental_variables_function import experiment_variables
from save_file_function import save_file_modification
from instructions_function import instructions
from experiment_block_function import experiment_block 
from save_experimental_block_function import save_experimental_block

### GATHERING PARTICIPANT INFO ### 

participant_info = {'Subject ID': '', 'Age': '', 'Sex': ['M', 'F'], 'Random seed': ''}

myDlg = gui.DlgFromDict(participant_info, title="Sam gaze experiment")

if not myDlg.OK:
    core.quit()
    
subject_id = str(participant_info['Subject ID'])
random_seed = int(participant_info['Random seed'])
age = str(participant_info['Age'])
sex = str(participant_info['Sex'])

win = visual.Window(color = '#000000', fullscr = True, monitor="testMonitor", units="pix")
win.mouseVisible = False

### VARIABLES FUNCTION ### 

pport_address_spike, trigger_code_spike, experiment_clock, countdown, fr, one_frame, trials_p_block, training_trials, isi, iti, diff_trial_conditions, left_right, clockwise_anticlockwise = experiment_variables(win) 

### STIMULI FUNCTION ### 

fixation_dot_grey, fixation_dot_green, fixation_dot_yellow, training_instructions_one, training_instructions_two, training_instructions_three, training_instructions_four, training_instructions_five, training_instructions_six, training_instructions_seven, training_instructions_eight, training_instructions_nine, training_begins, training_complete, block_complete, correct_response, incorrect_response, too_late = create_experiment_stimuli(win)

### FUNCTION FOR HEARTBEAT DETECTION ###

def listenforHR_basic(): 
    pport_address_in = 16361 # set to 889 for psychopys lab tests 16377        
    while True:
        signal_in = readParallelTrigger(pport_address_in)
        if signal_in > 63: 
            time_hb_prev = experiment_clock.getTime()
            break
    return time_hb_prev

### FUNCTION FOR CREATING THE SAVE FILE ### 

data_wb, save_file = save_file_modification(subject_id)

### INSTRUCTIONS ### 

instructions(training_instructions_one, training_instructions_two, training_instructions_three, training_instructions_four, training_instructions_five, training_instructions_six, training_instructions_seven, training_instructions_eight, training_instructions_nine, win)

### TRAINING BLOCKS ### 

training_block(win, countdown, fixation_dot_grey, fixation_dot_yellow, fixation_dot_green, one_frame, training_trials, isi, iti, diff_trial_conditions)












