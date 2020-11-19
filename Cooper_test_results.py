#Creating a function called good_excellent_results which takes a list of the results in meters as a parameter and returns the number of good and excellent results.
def good_excellent_result(my_list):
    sum = 0
    for result in my_list:
        if result > 2800:
            sum += 1
        if 2400 <= result <=2800:
            sum += 1     
    return sum

#Writing a program which:
#prompts the user for a file name; the program should not crash if the file does not exist (use try-except);
#reads the test results from the file and adds them into a list;

enterfile = input ("Enter the file name: ")
try:
    file = open (enterfile, 'r')
    my_list = []
    for line in file:
        my_list.append(line.strip())
except:
    print ("The file does not exist.")

my_list = [int(i) for i in my_list]
    
#calculating and printing out the average of all results rounded to the integer (you can use round for that, e.g. round(2.5) will give 3);
import statistics
avg = round(statistics.mean (my_list))
resultcount = good_excellent_result(my_list)

print ("The average result is", avg)
print ("There are", resultcount, "good or excellent results")
yourresult = int(input("Enter your result in meters: "))
if yourresult > 2800:
    print ("It is an excellent result.")
if 2400<=yourresult<=2800:
    print ("It is a good result.")
if 2200<=yourresult<=2399:
    print ("It is an average result.")
if 1600<yourresult<=2199:
    print ("It is a bad result.")
if yourresult<=1600:
    print ("It is a terrible result.")



