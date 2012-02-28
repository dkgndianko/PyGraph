###############################################################################
#
# Python stript to process the performance data of the 
# MC4 routing implementation
#
# author: Scott Anderson
#
###############################################################################

import sys
import numpy as np
import matplotlib.pyplot as plt

###############################################################################
# read values from a file
# and split the fields into separate lists
###############################################################################
def read_values(f):
	num_tests = []
	ns_tests = []
	us_tests = []
	ms_tests = []
	for line in open(f):
		fields = line.split(",")
		index = int(fields[0])
		ns = int(fields[1])
		us = int(fields[2])
		ms = int(fields[3])
		entry = (index, ns, us, ms)
		num_tests.append(entry)
		ns_tests.append(ns)
		us_tests.append(us)
		ms_tests.append(ms)
	yield num_tests
	yield ns_tests
	yield us_tests
	yield ms_tests

###############################################################################
# generate the names of the files passed to
# the program
###############################################################################
def open_files():
   if len(sys.argv) > 1:
      for f in sys.argv[1:]:
         yield f

###############################################################################
# loop throuh each file, read the values, and
# generate a chart of the results
###############################################################################
for file in open_files():
   print "Processing file: = " + str(file)
   rv=read_values(file)
   x = rv.next()
   y_ns = rv.next()
   y_us = rv.next()
   y_ms = rv.next()

   y_ns_max = str(max(y_ns))
   y_ns_min = str(min(y_ns))
   y_ns_avg = str(np.average(y_ns))

   y_ms_max = str(max(y_ms))
   y_ms_min = str(min(y_ms))
   y_ms_avg = str(np.average(y_ms))

   y_us_max = str(max(y_us))
   y_us_min = str(min(y_us))
   y_us_avg = str(np.average(y_us))

   if np.average(y_ms) >= 10.0:
      y = y_ms
      label = "\nmin="+y_ms_min+" max="+y_ms_max+" avg="+y_ms_avg\
      +"\nstd_dev="+str(np.std(y))+"\nvar="+str(np.var(y))
      plt.plot(y, 'r.')
      plt.ylabel("Time in Milliseconds")
      plt.title(file+label)
   elif np.average(test_us) >= 10.0:
      y = y_us
      label = "\nmin="+y_us_min+" max="+y_us_max+ " avg="+y_us_avg\
      +"\nstd_dev="+str(np.std(y))+"\nvar="+str(np.var(y))
      plt.plot(y, 'r.')
      plt.ylabel("Time in Microseconds")
      plt.title(file+label)
   else:
      y = y_ns
      label = "\nmin="+y_ns_min+" max="+y_ns_max+ " avg="+y_ns_avg\
      +"\nstd_dev="+str(np.std(y))+"\nvar="+str(np.var(y))
      plt.plot(y, 'r.')
      plt.ylabel("Time in Nanoseconds")
      plt.title(file+label)

   plt.xlabel("Samples")
   plt.show()

###############################################################################
# if you want to wait before exiting the application
#raw_input()
###############################################################################


