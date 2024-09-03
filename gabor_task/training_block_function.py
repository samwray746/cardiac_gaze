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
    correct_incorrect = []
    r_peak_times_list = []
    mean_rr_ints_list = [] 
    predicted_rr_ints_list = [] 
                   
