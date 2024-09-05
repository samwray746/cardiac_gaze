from main_script import listenforHR_basic
from intart_functions import sendParallelTrigger
import random
import psychopy
from psychopy import core, visual, event

# This function runs the training trials for the experiment. The training trials allows the participant to get used to the task, and also sets the difficulty thresholds for each trial type 
# that the participant begins with in the experimental blocks. 

def training_block(win, countdown, fixation_dot_grey, fixation_dot_yellow, fixation_dot_green, one_frame, training_trials, isi, iti, diff_trial_conditions)
    trial_type_rec = [] # i.e., systole high-frequency, diastole high-frequency etc. 
    angle_offset_rec = [] # offset of the Gabor patch 
    lr = [] # whether the Gabor patch was presented left or right 
    clock_or_anti_rec = [] # whether it was clockwise or anticlockwise 
    correct_incorrect = [] # whether response was correct or incorrect
    r_peak_times_list = [] # the times of the R-peaks for each trial 
    mean_rr_ints_list = [] # mean R-peak time for each trial 
    predicted_rr_ints_list = [] # the predicted R-peak time that the code generates 

    s_hf_offset_rec = [] # record of the offsets used in the systole high-frequency trials
    s_lf_offset_rec = [] # systole, low-frequency
    d_hf_offset_rec = [] # diastole, high_frequency 
    d_lf_offset_rec = [] # diastole, low-frequency 

    # Starting off the training block by showing the grey fixation dot for three seconds
    countdown.reset() 
    fixation_dot_grey.draw() 
    win.flip()

    while True: 
        if countdown.getTime() < (-2 + one_frame)
            break 

    prev_trial_condition = 'first_trial' # using this variable to ensure non-consecutive trials 

    for trial in range(training_trials):
        if len(diff_trial_conditions) == 0: # we're selecting each of the 4 trial types randomly then removing from the list...
            diff_trial_conditions = ['s_hf', s_lf', 'd_hf', 'd_lf'] # ...so need to reset when all 4 have been removed 

        this_trial_condition = random.choice(diff_trial_conditions) # random selection 
        
        if this_trial_condition == prev_trial_condition: # if the trial selected is the same as the previous trial 
            while True:
                this_trial_condition = random.choice(diff_trial_conditions) # selecting again 
                if this_trial_condition != prev_trial_condition: # if it's not the same, break loop 
                    break
                # otherwise, continue selection 
                 

        

        if (this_trial_type == 's_hf') or (this_trial_type == 's_lf'): # systole trial 
            
        

        
        
    
                   
