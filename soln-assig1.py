## CMPT 120 2014-3 
## Time goes by
## solution to assignment #1
## author: Diana Cukierman

'''
Program description:
Two dates are asked to the user. The user is assumed to type correctly
The program  calculates the distance between the two dates,
expressed in differnt ways
The dates will be asked as three numbers, one after the other:year,month,day
It is assumed that years may be between 1901 and 2099
and all months have 30 days
'''

# Other solutions are possible


# FUNCTIONS DEFINITIONS
### IT IS NOT REQUIRED IN ASSIGNMENT #1
### TO DECOMPOSE THE PROBLEM IN FUNCTIONS !!!!!
### the solution is presented using functions for
### further reference


def welcome_message():
    '''
    subroutine - does not return any value, just prints a welcome message
    does not receive any values either
    '''
    print  "-" * 65
    print  'Welcome to the CMPT 120  "Time goes by" system!'
    print  "You will be able to calculate the distance between dates"
    print  "The dates will be asked in the format year,month,day"
    print  "where it is assumed that:"
    print  "   - years may be between 1901 and 2099"
    print  "   - all months have 30 days"
    print  
    print  "Please follow the system prompts"
    print  "-" * 65, "\n"
    return


    

# TOP LEVEL


welcome_message()


D_MONTH = 30
D_YEAR = 360
# usual convention - constants are variables, but  the variable name
# is  written all in upper cases

# the constant values could be used directly in the code, 
# but with a constant it is more self-documented
# and it allows that future revisions are simpler (for example
# if in a later version one wishes to consider the real number of
# days per month, and distinguish leap years)

# ASK VALUES--------------------------
# In this solution we use 6 variables,
# one for each value

print "Please provide the first (earliest) date"
print
y1 = input("year (between 1901 and 2099 inclusive): ")
m1 = input("month (between 1 and 12 inclusive): ")
d1 = input("day (between 1 and 30 inclusive): ")

print
print "Please provide the second (latest) date"
print
y2 = input("year (between 1901 and 2099 inclusive): ")
m2 = input("month (between 1 and 12 inclusive): ")
d2 = input("day (between 1 and 30 inclusive): ")

# DAYS SINCE 1901,1,1-----------------------------

days_1901_since1 = 1900 * D_YEAR 

d1_since = (y1-1) * D_YEAR + (m1-1) * D_MONTH + (d1-1) - days_1901_since1
d2_since = (y2-1) * D_YEAR + (m2-1) * D_MONTH + (d2-1) - days_1901_since1

print
print "First result"
print "------------"
print

print "The number of days since 1901,1,1 to ...:"
print
print str(y1)+","+str(m1)+","+str(d1),"is:",d1_since
print str(y2)+","+str(m2)+","+str(d2),"is:",d2_since


# DIFF DAYS -------------------------------
message = "Second result"
print
print message
print len(message)*"-"
print

total_dif_days = d2_since - d1_since

print "The difference in days is:",total_dif_days

# FROM DIFF IN DAYS CALCULATE IN YEARS,MONTHS,DAYS------

## converting the dif to the format yy mm dd, with mm <12 and dd <30
yy_dif = total_dif_days/D_YEAR
left_over_days = total_dif_days % D_YEAR
mm_dif = left_over_days /D_MONTH
dd_dif = left_over_days % D_MONTH

message = "Third (and last) result"
print 
print message,"\n",len(message)*"-"
print

print "The difference in days is expressible also as:", \
      yy_dif, "years,",mm_dif,"months and",dd_dif, "days"

print "\nEnd of the program! Bye!"


# END 
