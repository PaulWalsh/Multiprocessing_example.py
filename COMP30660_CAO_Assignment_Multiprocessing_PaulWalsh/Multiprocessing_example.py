# COMP30660 COMPUTER ARCHITECTURE & ORGANISATION
# ASSIGNMENT:   A Python script demonstrating the use of multiprocessing.
#
# NAME:         Paul Walsh
# STUDENT ID:
# DATE:         23NOV15
# Designed for Python2
#
# To demonstrate the use of the python multiprocessing library and show
#  the performance improvements possible with parallelising code/spreading
#  its execution across multiple cores.
#
# Websites used as an aid:
# https://docs.python.org/2/library/multiprocessing.html
# http://sebastianraschka.com/Articles/2014_multiprocessing_intro.html
# https://docs.python.org/2/library/multiprocessing.html?highlight=pool#module-multiprocessing.pool
#
# Addition: 08JAN18 -> readability improvements to adhere with PEP8 style guide
#
##################################################################################

# Import multiprocessing and time modules to use cpu_count(), map(), time() functions
import multiprocessing
import time

# Obtain the number of cpu cores on the PC
numCPU_cores = multiprocessing.cpu_count()

# Setup variables for number of process cores, number of process cores by 2, and number of process cores by 4
PROCESSES = numCPU_cores
PROCESSES_by2 = PROCESSES*2
PROCESSES_by4 = PROCESSES*4

print "########################################"
print "START PROGRAM:"
print "This PC has:", numCPU_cores, "CPU cores."
print "----------------------------------------"


# -----------------------------------------------
# Function used to test out multiprocessing
# Simple function to return the square of the argument
def sqF(n):
    return n**2
# -----------------------------------------------


###############################################################
# MAIN PROGRAM PART
# Important to create the Process instances inside this section because child processes import the script where the
#  target function is contained. If this is not included the pc can lock up.
 
if __name__ == '__main__':
    
    # Setup a number to perform test with
    value = 5000000
    #print "----------------------------------------"

    # ================================================================
    # SINGLE PROCESSING
    # ------------------------------------
    print "Single Process:"

    # Setup the single process start time variable
    serStartTime = time.time()
    
    # Using the map function to invoke the 'sqF' function passing numbers in range from 0 to the value test number
    #  set above and returns the numbers as a tuple and assigns this to variable 'sqF_results1'
    sqF_results1 = map(sqF, range(value+1))
    #print sqF_results1
    # Setup the single process stop time variable
    serStopTime = time.time()
    
    # Print out the time took for single process
    print "Serial processing time (1 process):", serStopTime-serStartTime
    
    # If uncomment out the below will produce the returned squared numbers in a tuple
    # However only recommended to do this for a small value!
#    print "Value:", value
#    print "Result after function:", sqF_results1

    ################################################
    print "----------------------------------------"

    # ================================================================
    # MULTIPLE PROCESSING (NUM OF CORES*2)
    # ------------------------------------
    print "Multiple Process:"

    # multiprocessing.Pool is used to create/spawn several worker processes in order
    #  to spread the workload from one job across several running processes (i.e., num cores)
    poolAllCores = multiprocessing.Pool(PROCESSES)

    # Setup the multiple process (num of CPU cores) start time variable
    parStartTime = time.time()
    
    # Using the map function to invoke the 'sqF' function passing numbers in range from
    #  0 to the value test number set above across the pool of processes setup above
    #  and returns the numbers as a tuple and assigns this to variable 'sqF_results2'
    sqF_results2 = poolAllCores.map(sqF, range(value))
    
    # Setup the multiple process (num of CPU cores) stop time variable
    parStopTime = time.time()

    # Print out the time took for multiple process (num of CPU cores)
    print "Multiple processing time (#PC_cores):", parStopTime-parStartTime
    
    # If uncomment out the below will produce the returned squared numbers in a tuple
    #  However only recommended to do this for a small value!
#    print "Value:", value
#    print "Result after function:", sqF_results2
    
    # Signal to say no more work to do for the spawned processes
    poolAllCores.close()
    # Signal to say join up
    poolAllCores.join()
    
    print "\tDELAY FOR 3 SECONDS TO OBSERVE CLOSE AND JOIN OF PROCESSES (IN WINDOWS TASK MANAGER)..."
    time.sleep(3)

    # ================================================================
    # MULTIPLE PROCESSING (NUM OF CORES*2)
    # ------------------------------------

    # multiprocessing.Pool is used to create/spawn several worker processes in order
    #  to spread the workload from one job across several running processes (i.e., num cores*2)
    poolAllCoresBy2 = multiprocessing.Pool(PROCESSES_by2)

    # Setup the multiple process (num of CPU cores*2) start time variable
    parStartTime2 = time.time()

    # Using the map function to invoke the 'sqF' function passing numbers in range from
    #  0 to the value test number set above across the pool of processes setup above
    #  and returns the numbers as a tuple and assigns this to variable 'sqF_results3'
    sqF_results3 = poolAllCoresBy2.map(sqF, range(value))
    
    # Setup the multiple process (num of CPU cores*2) stop time variable
    parStopTime2 = time.time()

    # Print out the time took for multiple process (num of CPU cores*2)
    print "Parallel processing time (#PC_cores*2):", parStopTime2-parStartTime2
    
    # If uncomment out the below will produce the returned squared numbers in a tuple
    #  However only recommended to do this for a small value!
#    print "Value:", value
#    print "Result after function:", sqF_results3

    # Signal to say no more work to do for the spawned processes
    poolAllCoresBy2.close()
    # Signal to say join up
    poolAllCoresBy2.join()
    
    print "\tDELAY FOR 3 SECONDS TO OBSERVE CLOSE AND JOIN OF PROCESSES (IN WINDOWS TASK MANAGER)..."
    time.sleep(3)

    # ================================================================
    # MULTIPLE PROCESSING (NUM OF CORES*4)
    # ------------------------------------

    # multiprocessing.Pool is used to create/spawn several worker processes in order
    #  to spread the workload from one job across several running processes (i.e., num cores*4)
    poolAllCoresBy4 = multiprocessing.Pool(PROCESSES_by4)
    
    # Setup the multiple process (num of CPU cores*4) stop time variable
    parStartTime3 = time.time()

    # Using the map function to invoke the 'sqF' function passing numbers in range from
    #  0 to the value test number set above across the pool of processes setup above
    #  and returns the numbers as a tuple and assigns this to variable 'sqF_results4'
    sqF_results4 = poolAllCoresBy4.map(sqF, range(value))
    
    # Setup the multiple process (num of CPU cores*4) stop time variable
    parStopTime3 = time.time()

    # Print out the time took for multiple process (num of CPU cores*4)
    print "Parallel processing time (#PC_cores*4):", parStopTime3-parStartTime3
    
    # If uncomment out the below will produce the returned squared numbers in a tuple
    #  However only recommended to do this for a small value!
#    print "Value:", value
#    print "Result after function:", sqF_results4

    # Signal to say no more work to do for the spawned processes
    poolAllCoresBy4.close()
    # Signal to say join up
    poolAllCoresBy4.join()
    
    print "\tDELAY FOR 3 SECONDS TO OBSERVE CLOSE AND JOIN OF PROCESSES (IN WINDOWS TASK MANAGER)..."
    time.sleep(3)
    ################################################
    print "----------------------------------------"


print "Program Finished!"
