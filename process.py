#Opening the um-server-01.txt file and assigning to 
log_file = open("um-server-01.txt")

#Defining a function called sales_reports that takes in a file (log_file) as a parameter
def sales_reports(log_file):
    #Using a for loop to iterate through the log_file line by line.
    for line in log_file:
        #Removing any trailing whitespaces at the end of each line
        line = line.rstrip()
        #assigning the variable day to the first 3 characters of each line
        day = line[0:3]
        #Checking if day is the Tue
        if day == "Mon":
            #Printing the line
            print(line)

#Calling the function with the log
sales_reports(log_file)
