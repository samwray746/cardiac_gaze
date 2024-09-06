from main_script import listenforHR_basic
from intart_functions import sendParallelTrigger
import random
import psychopy
from psychopy import core, visual, event

# This function runs the training trials for the experiment. The training trials allows the participant to get used to the task, and also sets the difficulty thresholds for each trial type 
# that the participant begins with in the experimental blocks. 

def training_block(win, countdown, fixation_dot_grey, fixation_dot_yellow, fixation_dot_green, one_frame, training_trials, isi, iti, diff_trial_conditions, left_right, clockwise_anticlockwise, gabor_orientation, training_begins, pport_address_spike, trigger_code_spike)
    trial_type_rec = [] # i.e., systole high-frequency, diastole high-frequency etc. 
    angle_offset_rec = [] # offset of the Gabor patch 
    lr_rec = [] # whether the Gabor patch was presented left or right 
    clock_or_anti_rec = [] # whether it was clockwise or anticlockwise 
    correct_incorrect_rec = [] # whether response was correct or incorrect
    isi_rec = []
    iti_rec = [] 
    r_peak_times_list = [] # the times of the R-peaks for each trial 
    mean_rr_ints_list = [] # mean R-peak time for each trial 
    predicted_rr_ints_list = [] # the predicted R-peak time that the code generates 

    s_hf_offset_rec = [] # record of the offsets used in the systole high-frequency trials
    s_lf_offset_rec = [] # systole, low-frequency
    d_hf_offset_rec = [] # diastole, high_frequency 
    d_lf_offset_rec = [] # diastole, low-frequency 

    anti_or_clockwise = random.choice(clockwise_anticlockwise) # kicking things off by randomly choosing whether the first presentation is clockwise/anticlockwise 

    if anti_or_clockwise == 'ac': #i.e., clockwise
        gabor_orientation = -gabor_orientation 
        
    s_hf_offset_rec.append(gabor_orientation) # starting orientation 
    s_lf_offset_rec.append(gabor_orientation) # starting orientation 
    d_hf_offset_rec.append(gabor_orientation) # starting orientation    
    d_lf_offset_rec.append(gabor_orientation) # starting orientation 

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

        diff_trial_conditions.remove(this_trial_condition) # once selected, remove from the possible trial types until the list is refreshed 
        lr_choice = random.choice(left_right)
        
        if lr_choice = 'left':
            gabor_pos = (-30, 0) # just example values 
        else:
            gabor_pos = (30, 0)
        
        isi_this_trial = random.choice(isi)
        iti_this_trial = random.choice(iti) 
        r_peak_counter = 0
        
        r_peak_times = [] 
        rr_intervals = [] 

        if (this_trial_type == 's_hf') or (this_trial_type == 's_lf'): # systole trial 
           # preparing the stimulus - change upon converting to visual angle 
            if this_trial_type == 's_hf': 
                g_stim = visual.GratingStim(win=win, 
                        tex='sin', 
                       mask='gauss', 
                       size=50,  # Size of the Gabor patch in pixels
                       sf=0.1,   # Spatial frequency (cycles per pixel)
                       pos = gabor_pos, # Position of the Gabor patch - again arbitrary for now 
                       ori=s_hf_offset_rec[-1],   # Orientation of the Gabor patch (in degrees)
                       contrast=1.0)  # Contrast of the Gabor patch
            
            if this_trial_type == 's_lf': 
                g_stim = visual.GratingStim(win=win, 
                        tex='sin', 
                       mask='gauss', 
                       size=50,  # Size of the Gabor patch in pixels
                       sf=0.2,   # Spatial frequency (cycles per pixel) - just an example until we change 
                       pos = gabor_pos, # Position of Gabor patch, arbitrary for now 
                       ori=s_lf_offset_rec[-1],   # Orientation of the Gabor patch (in degrees)
                       contrast=1.0)  # Contrast of the Gabor patch
            
            fixation_dot_green.draw() # now that R-peak sensing is beginning, draw the green fixation dot 
            win.flip() 
            g_stim.draw() # preparing the Gabor patch for presentation 

            ### R-PEAK DETECTION ### 
                 
             # For diastole trials we're going to be gathering 3 RR-intervals, so waiting for 4 R-peaks, then presenting
             # the stimulus just before the 5th R-peak. 
             
             # We'll do the same for systole trials to keep the ISIs similar, i.e., detecting 5 R-peaks, and presented 250ms after the 5th  
                 
            for peak in range(5): 
                 r_peak_time = listenforHR_basic()
                 r_peak_times.append(r_peak_time)
                 countdown.reset()
                 r_peak_counter += 1 
                 
                 # A potential problem has been that when the threshold is crossed (i.e., an R-peak), the listenforHR_basic doesn't only send once, but during the
                 # whole time that the signal crosses the threshold. So I'm introducing a delay during the sensing period, in order to pause everything
                 # Until the signal has gone back below the threshold 
                 
                 if r_peak_counter < 5:
                     core.wait(0.5)
             
            while True: # waiting 250ms after R-peak has been detected
                 if countdown.getTime() < (-0.250 + one_frame):
                     break

            win.flip()
            countdown.reset()
            sendParallelTrigger(pport_address_spike, trigger_code_spike)
            fixation_dot_grey.draw()

            while True:
                     if countdown.getTime() < (-0.04 + one_frame): #40ms presentation 
                         break
                     
            win.flip() # remove stimulus, grey fixation dot presented 

            ### FOR SYSTOLE TRIALS, CALCULATING THE MEAN RR-INTERVAL AND ADDING RR-INTERVALS TO LIST ### 
                
            for peak in range(len(r_peak_times) - 1): # going through the R-peak list
                rr_interval = r_peak_times[peak + 1] - r_peak_times[peak] # R-peak, index + 1, minus R-peak, index
                rr_intervals.append(rr_interval)
                
            mean_rr_int = mean(rr_intervals)
        
        if (this_trial_type == 'd_hf') or (this_trial_type == 'd_lf'): # diastole trial 
           # preparing the stimulus - change upon converting to visual angle
            if this_trial_type == 'd_hf': 
                g_stim = visual.GratingStim(win=win, 
                        tex='sin', 
                       mask='gauss', 
                       size=50,  # Size of the Gabor patch in pixels
                       sf=0.1,   # Spatial frequency (cycles per pixel)
                       pos = gabor_pos, # Position of the Gabor patch - again arbitrary for now 
                       ori=d_hf_offset_rec[-1],   # Orientation of the Gabor patch (in degrees)
                       contrast=1.0)  # Contrast of the Gabor patch
            
            if this_trial_type == 'd_lf': 
                g_stim = visual.GratingStim(win=win, 
                        tex='sin', 
                       mask='gauss', 
                       size=50,  # Size of the Gabor patch in pixels
                       sf=0.2,   # Spatial frequency (cycles per pixel) - just an example until we change 
                       pos = gabor_pos, # Position of Gabor patch, arbitrary for now 
                       ori=d_lf_offset_rec[-1],   # Orientation of the Gabor patch (in degrees)
                       contrast=1.0)  # Contrast of the Gabor patch

            fixation_dot_green.draw() # now that R-peak sensing is beginning, draw the green fixation dot 
            win.flip() 
            g_stim.draw() # preparing the Gabor patch for presentation 

            ### R-PEAK DETECTION AND RR-INTERVAL CALCULATION ### 
                
            for peak in range(4): # gathering 4 R-peaks
                r_peak_time = listenforHR_basic()
                r_peak_times.append(r_peak_time)
                countdown.reset()
                r_peak_counter += 1
            
                if peak < r_peak_counter < 4: # again stopping multiple signals being sent per R-peak 
                    core.wait(0.5)

            ### CALCULATING RR-INTERVALS ### 
            
            for peak in range(len(r_peak_times) - 1): # going through the R-peak list
                rr_interval = r_peak_times[peak + 1] - r_peak_times[peak] # R-peak, index + 1, minus R-peak, index
                rr_intervals.append(rr_interval)
                
            mean_rr_int = mean(rr_intervals) # this is useful to know to check for faulty trials 
            
            predicted_rr_int = (rr_intervals[-1]*0.5) + (rr_intervals[-2]*0.3) + (rr_intervals[-3]*0.2)
            # ^ I'm calculating the predicted RR-interval by weighting the calculated RR-intervals, most recent with the highest weighting 
            
            ### DOING SOME BASIC ADJUSTMENTS BASED OFF THE MEAN RR-INTERVALS ### 
            
            if predicted_rr_int >= 1: # i.e., less than 60bpm
                while True:
                    if countdown.getTime() < (-predicted_rr_int + 0.150 + one_frame): # we present the stimulus 150ms before the next predicted R-peak
                        break
            elif (1 > predicted_rr_int) and (predicted_rr_int >= 0.86): #i.e., between 60 and 70bpm
                while True:
                    if countdown.getTime() < (-predicted_rr_int + 0.135 + one_frame): # present the stimulus 0.135ms before the next predicted R-peak
                        break    
            elif predicted_rr_int < 0.86: # i.e., greater than 70bpm
                while True: 
                    if countdown.getTime() < (-predicted_rr_int + 0.125 + one_frame): # present the stimulus 0.125ms before the next predicted R-peak 
                        break                
        
            win.flip()
            countdown.reset()
            sendParallelTrigger(pport_address_spike, trigger_code_spike)
            fixation_dot_grey.draw()

            while True:
                if countdown.getTime() < (-0.04 + one_frame):
                    break
            win.flip()
            

        ### INTER-STIMULUS INTERVAL ### 

            
            

            

        
        
    
                   
