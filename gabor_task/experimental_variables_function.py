from psychopy import core

def experiment_variables(win):
    
    ### VARIABLES, PATHS, FUNCTIONS ### 

    pport_address_spike = 16360
    trigger_code_spike = 255

    experiment_clock = core.MonotonicClock() # the main clock used in the experiment 
    countdown = core.CountdownTimer()
    
    fr = win.getActualFrameRate() # getting frame rate of the monitor 
    one_frame = 1/fr

    trials_p_block = 60 # trials in a block 
    iti = [1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0] # inter-trial interval
    isi = [2, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0] # inter-stimulus interval

    diff_trial_conditions = ['s_hf', 's_lf', 'd_hf', 'd_lf']

    return pport_address_spike, trigger_code_spike, experiment_clock, countdown, fr, one_frame, trials_p_block, isi, iti, diff_trial_conditions



    
