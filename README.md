# Cooper-test-results

The Cooper test is a test of physical fitness. The main idea of the test is to run as far as possible within 12
minutes. The outcome is based on the distance the person ran, their age and sex. In this exercise, we focus only
on men's norms at the age of 20-29. For the men of the age of 20-29, the results can be interpreted as follows:

● Excellent if the test person runs more than 2800 meters

● Good if the test person runs 2400-2800 meters

● Average if the test person runs 2200-2399 meters

● Bad if the test person runs 1600-2199 meters

● Terrible if the test person runs less than 1600 meters

The university wants to test male students and calculate how many of them get Good or Excellent results. The
results in meters are written into a simple text file (create a .txt file yourself). An example:

1900

2600

2801

2500

1800

Furthermore, new students can also perform the test. The students want to know the interpretation of their
results.

Create a function called good_excellent_results which takes a list of the results in meters as a
parameter and returns the number of good and excellent results.

An example of the function call:

>>> good_excellent_results([1900,2600,2801,2500,1800])

Write a program which:

● prompts the user for a file name; the program should not crash if the file does not exist (use
try-except);

● reads the test results from the file and adds them into a list;

● calculates and prints out the average of all results rounded to the integer (you can use round for that, e.g.
round(2.5) will give 3);

● counts and prints out the number of good and excellent results using the above-mentioned function
good_excellent_results;

● prompts the user for a result of the test in meters and prints out the interpretation of the result.

Sample content of the file results.txt:

1900

2600

2801

2500

1800

The program prints out (the user inputs are shown in italic):

Enter the file name: results.txt

The average result is 2320

There are 3 good or excellent results

Enter your result in meters: 2555

This is a good result.


If the content of the file results.txt is as follows:

1000


2550

4000

3555

2200

1800

2400

2000

The program outputs (the user inputs are shown in italic):

Enter the file name: results.txt

The average result is 2438

There are 4 good or excellent results

Enter your result in meters: 1950

This is a bad result.
