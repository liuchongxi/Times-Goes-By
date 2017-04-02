##name:Jacky Liu
##date of last revision: 26 01 2015
##the time of working on this exercise:5.5 hours
##description of the program decription: clear, easy understand,but a little bit time consuming
print("------------------------------------")
print("Welcome to the CMPT 120 'Time goes by' system!")
print("You will be able to calculate the distance between dates")
print("The dates will be asked in the format year,month,day ")
print("where it is assumed that:")
print("     - years may be between 1901 and 2099 ")
print("     - all months have 30 days \n ")
print("Please follow the system prompts")
print("------------------------------------")

print ("Please provide the first (earliest) date \n")
year1 = input("year (between 1901 and 2099 inclusive):")
while( year1 <1901 or year1>2099):
    ## raw_input() for integer input requirement\
           year1=input("wrong year,pls re-enter year between 1901 and 2099 inclusive:")
month1 = input("month:")
##using while function to avoid wrong years provided by user 
while( month1 <1 or month1>12):
           month1=input("wrong month,pls re-enter month between 1 and 12 inclusive:")
day1 = input ("day (between 1 and 30 inclusive):")
while( day1 <1 or day1>30):
           day1=input("wrong day,pls re-enter day between 1 and 30 inclusive:")

print ("\npls provide the second (lastest) date \n")
year2 = input("year(between 1901 and 2099 invlusive):")
while( year2 <1901 or year2>2099):
           year2=input("wrong year,pls re-enter year between 1901 and 2099 inclusive:")
month2 = input("month:")
while( month2 <1 or month2>12):
           month2=input("wrong month,pls re-enter month between 1 and 12 inclusive:")
day2 = input ("day (between 1 and 30 inclusive):")
while( day2 <1 or day2>30):
           day2=input("wrong day,pls re-enter day between 1 and 30 inclusive:")

defaultyear =1901
defaultmonth =1
defaultday = 1

R1ayearDiff= year1-defaultyear
R1amonthDiff = month1 - defaultmonth
R1aday = day1-defaultday
result1a= R1ayearDiff*360+R1amonthDiff*30+R1aday

R1byearDiff= year2-defaultyear
R1bmonthDiff = month2 - defaultmonth
R1bday = day2-defaultday
result1b= R1byearDiff*360+R1bmonthDiff*30+R1bday

print ("\nFisrt result")
print ("--------------\n")

print ("The number of days since 1901,1,1 to ...:")
print year1,",",month1,",",day1,",", 'is:',result1a
print year2,",",month2,",",day2,",", 'is:',result1b


R2yearDiff=year2-year1
R2monthDiff=month2-month1
R2dayDiff=day2-day1
result2=R2yearDiff*360+R2monthDiff*30+R2dayDiff

print("\nSecond result")
print("---------------\n")
print 'The differentce in days is:', result2



print("\nThird (and last) result")
print("---------------\n")
print 'The difference indays is expressible also as:',R2yearDiff,"years",R2monthDiff,"months and",R2dayDiff,"days"
print ("\nEnd of the program! Bye!")

