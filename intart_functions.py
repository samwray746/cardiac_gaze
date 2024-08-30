#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 13:16:40 2017
Updated Nov 27, 2018

@author: Alberto, Dennis
"""
##%% 1.Importing Modules
from psychopy import event, core
#Module needed to use C and DLL. Very imporant to comunicate with the parallel port for triggers
from ctypes import windll

#%% 2.Experimental Functions

#% 4.1 shutdown: it incorporates win.close (specified by the input exp_window) and core.quit in a single function
def shutdown(exp_window):
    exp_window.close()
    core.quit()
    
# 4.2 get_keypress: it checks for the pressed keys and quit the experiment if 'q' is pressed (after having closed the results file)
def escape_keypress(results_file,exp_window):
    keys = event.getKeys()
    if keys and keys[0] == 'q':
        results_file.close() #close result file before quitting the program
        shutdown(exp_window)
    else:
        return None

#ONLY FOR DESKTOP COMPUTERS
# 4.3 sendParallelTrigger: this function allows me to send triggers via Parallel Port after having specified:
    #1) the address of the parallel port
    #2) the specific event marker

pport=windll.inpoutx64 
def sendParallelTrigger(pport_address_out,triggerCode):
    try:
        pport.Out32(pport_address_out,triggerCode)  #set the pins to the correspondent input (triggerCode)
        #print 'signal out: '+str(pport.Inp32(pport_address_out))
        core.wait(0.01)
        pport.Out32(pport_address_out,0)   #reset all the pins to 0
    except:
        print("Error")
        
def sendParallelTrigger2(pport_address_out,triggerCode):
    try:
        pport.Out32(pport_address_out,triggerCode)  #set the pins to the correspondent input (triggerCode)
        #print 'signal out: '+str(pport.Inp32(pport_address_out))
        core.wait(0.05)
        pport.Out32(pport_address_out,0)   #reset all the pins to 0
    except:
        print("Error")
        
def sendParallelTrigger3(pport_address_out,triggerCode):
    try:
        pport.Out32(pport_address_out,triggerCode)  #set the pins to the correspondent input (triggerCode)
        #print 'signal out: '+str(pport.Inp32(pport_address_out))
        core.wait(0.10)
        pport.Out32(pport_address_out,0)   #reset all the pins to 0
    except:
        print("Error")
        
def sendParallelTrigger4(pport_address_out,triggerCode):
    try:
        pport.Out32(pport_address_out,triggerCode)  #set the pins to the correspondent input (triggerCode)
        #print 'signal out: '+str(pport.Inp32(pport_address_out))
        core.wait(0.20)
        pport.Out32(pport_address_out,0)   #reset all the pins to 0
    except:
        print("Error")

def readParallelTrigger(pport_address_in):
    #try:
    byte = pport.Inp32(pport_address_in)
    return byte
    #except:
        #print "ERROR in receiving signal"