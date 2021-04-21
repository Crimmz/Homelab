#Technical Challenge Submission for SADA by Ethan S 
import csv #This library will help us work with the data file
import json#For part 3

def count_rows(datafile):
    counter= 0#Using a counter for iteration as a throwback to my highschool days. 

    data=open(datafile)  
    parse=csv.DictReader(data)
    for rows in parse: #This loop iterates through each row and updates the counter so we can print the total number of rows. 
        counter +=1
    print ("The total number of rows actually containing data is",counter) #Our porgram knows the first row is metadata and not part of the dataset
    

count_rows("data.csv")

def validate_profits(datafile):
    data=open(datafile)  
    parse=csv.DictReader(data)
    newfile= open("validated.csv", "w", newline="")
    output = csv.writer(newfile)
    outputlist=[]

    for rows in parse: #Looping through CSV files to check each profit column. 
        try:
            (float(rows["Profit (in millions)"]))
            outputlist.append(rows)
            

        except ValueError:
            pass
    counter=0   
    while True:
        try:
            counter+=1
            output.writerows([[outputlist[counter]]])
        except IndexError:
            break
    count_rows("validated.csv")
validate_profits("data.csv")

def json_converter(datafile):
    data=open(datafile)  
    parse=csv.DictReader(data)
    
    #Json File
    newfile= open("data2.json", "w", newline="")
    for rows in parse:
        try:
            (float(rows["Profit (in millions)"]))#This validates that the value in this column is a number. 
            newfile.write(json.dumps([rows], indent=4))
            
            
            
        except ValueError:
            pass
    
    

json_converter("data.csv")    


def highest-profit(datafile):
