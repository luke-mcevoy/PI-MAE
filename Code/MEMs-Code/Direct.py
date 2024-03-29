import mirror as mems       # QuEST lab mirror library
import argparse             # Python parser for command-line options
import counter as c         # QuEST lab counter library
import time                 # Python time access and conversion
import math                 # Python math

"""
Utilizes argparse to interface with user via command line.
List of flags and their values below.
"""
parser = argparse.ArgumentParser()
parser.add_argument("-x","--xmin", type=float, help="X min value", default=-0.1)        
parser.add_argument("-X", "--xmax", type=float, help="X max value", default =0.1)
parser.add_argument("-y", "--ymin", type=float, help="Y min value", default=-0.1)
parser.add_argument("-Y", "--ymax", type=float, help="Y max value", default=0.1)
parser.add_argument('-s', '--xstep', type=float, help='x step size', default=0.02)
parser.add_argument('-u', '--ystep', type=float, help='y stepsize', default=0.02)
parser.add_argument('-f', '--filename', type=str, help='filename to save the data', default='lidar.csv')
parser.add_argument('-t', '--tdc', type=int, help='tdc integration time', default=10)
parser.add_argument('-p', '--peakcheck', type=float, help='peak check', default=10)
parser.add_argument('-l', '--lidar', help='doing a normal lidar', action='store_true')
parser.add_argument('-v', '--verbose', help='print the verbose', action='store_true')
parser.add_argument('--zlast', help='zlast or the initial position of the delay', default=0) 

'''
Parse command line input & instantiate file descriptors (FD).
Throw if FDs fail.
'''
args = parser.parse_args()
fds = {'mirror_fd':None, 'save_fd':None, 'count_fd':None, 'control_fd':None}

fds['mirror_fd'] = mems.open_mirror()
if(fds['mirror_fd']<0):
    print "unable to connect to mirror"
    exit()

fds['save_fd'] = open(args.filename, 'w+')
fds['save_fd'].write('y,x,counts\n')
time.sleep(1)

'''
Method: 
    Range function that accepts float increments.
Input: 
    Start, end, increment between points, and precision for range.
Output:
    Returns list of float range. Used to trace (x, y, or z) path for scanning. 
    Where to start, where to end, how far between points.
'''

### Broken legacy code. Keeping it for explination of what not to do

# def frange(end,start=0,inc=0,precision=1):
#     if not start:
#         start = end + 0.0
#         end = 0.0
#     else: end += 0.0
    
#     if not inc:
#         inc = 1.0
#     count = int(math.ceil((start - end) / inc))

#     L = []
#     L.append(float(end))
#     for i in (range(1,count)):
#         L.append(L[i-1] + inc)
#     return L

#def frange(start, end, increment):
#	start = round(start, 3)
#	end = round(end, 3)
#	increment = round(increment, 3)
#	print('start', start)
#	print('end', end)
#	print('increment', increment)
#	result = []
#    	current = start
#    	while round(current, 3) < round(end, 3):
#        	result.append(current)
#        	current += increment
#	print(result)
#	return result


def frange(start, end, increment):
	precision = 10
	start = round(start, precision)
	end = round(end, precision)
	increment = round(increment, precision)
	#print('start', start)
	#print('end', end)
	#print('increment', increment)
	result = []
    	current = start
    	while round(current, precision) < round(end, precision):
		current = round(current, precision)
        	result.append(current)
        	current += increment
	#print(result[0:2])
	#return result[0:2]
	#return result[0:1]
	return result


'''
Method:
    What does this do?
Input:
    File descriptors object
Output:
    count of?
'''
def count_helper(fds):
    fds['count_fd'], fds['control_fd'] = c.open_counter(args.tdc)
    count = c.count(fds['control_fd'], fds['count_fd'], args.tdc)
    c.close(fds['control_fd'], fds['count_fd'])
    time.sleep(args.tdc/1000000)
    if count!=None:
        return count
    else: return count_helper(fds)     

'''
Method:
    Mirror scan logic
Input:
    Command line input object & file descriptors object
Output:
    pass
'''    
def lidar(args, fds):
        for x in frange(args.xmin, args.xmax, args.xstep):
            wait_mirror = 0
            for y in frange(args.ymin, args.ymax, args.ystep):
                mems.set_pos(fds['mirror_fd'], x, y)
                time.sleep(0.002) #wait time to follow beam
                if (wait_mirror == 0):
                    time.sleep(0.002)
                    wait_mirror = 1
                count =  c.get_count(args.tdc)
                out = '{:.3f}, {:.3f}, {}'.format(y, x, count)
                fds['save_fd'].write(out+'\n')
                if(args.verbose ): print out       

start = time.clock()
if(args.verbose):
    print "Starting at time {}".format(start)
    
if(args.lidar):
    lidar(args, fds)
else:
    lidar(args, fds)
if(args.verbose):
    end = time.clock()
    print "Ending at time {}".format(end)
    print "Time taken {}".format(end-start)

mems.close_mirror(fds['mirror_fd'])


'''
Misc Notes:
    DLY_START = 100
    DLY_END = 260
    DLY_INC = 5
    TDC = 5000
'''
