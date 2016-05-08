import time

def print_time(time):
    if(time > 60):
	    print 'It took', time/60, 'minutes.'
    else:
	    print 'It took', time, 'seconds.'