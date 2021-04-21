#Technical Challenge Submission for SADA by Ethan S 
import csv #This library will help us work with the data file
import json#For part 3


def count_rows(datafile):
    counter= 0#Using a counter for iteration as a throwback to my highschool days. 

    data=open(datafile)#Open and parse csv.
    parse=csv.DictReader(data)
    for rows in parse: #This loop iterates through each row and updates the counter so we can print the total number of rows. 
        counter +=1
    print ("The total number of rows actually containing data is",counter) #Our porgram knows the first row is metadata and not part of the dataset.
    

count_rows("data.csv")

def validate_profits(datafile):#this will remove non numeric profits rows so we can get a count of our useful dataset.
    data=open(datafile)  #Open then parse data.
    parse=csv.DictReader(data)
    newfile= open("validated.csv", "w", newline="")#New file for output. 
    output = csv.writer(newfile)
    outputlist=[]

    for rows in parse: #Looping through CSV files to check each profit column. 
        try:
            (float(rows["Profit (in millions)"]))#This is the validation for the Profit column
            outputlist.append(rows)
            

        except ValueError:
            pass
    counter=0   
    while True:
        try:
            counter+=1
            output.writerows([[outputlist[counter]]])#Output the numericaly valid rows to a new file.
        except IndexError:
            break
    count_rows("validated.csv")

validate_profits("data.csv")

def json_converter(datafile):#Here is where we convert to JSON
    data=open(datafile)  
    parse=csv.DictReader(data)#opening the CSV
    
    #Json File
    newfile= open("data2.json", "w", newline="")#Creating a JSON file
    output_list = []
    for rows in parse:
        try:
            
            (float(rows["Profit (in millions)"]))#This validates that the value in this column is a number.
            output_list.append(rows)#Making sure we don't get any non numeric rows in our JSON file
        except ValueError:
            pass
    newfile.write(json.dumps(output_list, indent=4))#Oytput the JSON data
    
    

json_converter("data.csv")    


def highest_profit(datafile):#Sorting and printing the highest profits. 
    data=open(datafile) 
    parse=json.load(data)
    sort=sorted(parse, key=lambda x: (x["Profit (in millions)"]),reverse=True)#Sorting the JSON data by the profit row. 
    for i in range (20):#Printing top 20 results
        print (sort[i])
highest_profit("data2.json")