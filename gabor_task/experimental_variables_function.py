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

    sequence_SD = ['S', 'D', 'D', 'S', 'D', 'S', 'S', 'D'] # basic systole-diastole sequence 
    sequence_HF_LF = ['HF', 'LF', 'LF', 'HF', 'LF', 'HF', 'HF', 'LF'] # basic high-freq / low-freq sequence

    # Sequence one, SD
    sd_1 = (sequence_SD * (60 // len(sequence_SD))) + sequence_SD[:(60 % len(sequence_SD))]

    # Sequence two, SD
    sd_2 = ['D' if x == 'S' else 'S' for x in sd_1]

    # Sequence three, freq
    freq_1 = (sequence_HF_LF * (60 // len(sequence_HF_LF))) + sequence_HF_LF[:(60 % len(sequence_HF_LF))]

    # Sequence four, freq
    freq_2 = ['LF' if x == 'HF' else 'HF' for x in freq_1]

    return pport_address_spike, trigger_code_spike, experiment_clock, countdown, fr, one_frame, trials_p_block, isi, iti, sd_1, sd_2, freq_1, freq_2



    
