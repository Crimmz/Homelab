#Technical Challenge Submission for SADA by Ethan S 
import csv #This library will help us work with the data file
import json#For part 3


def count_rows(datafile):
    counter=0 #Using a counter for iteration as a throwback to my highschool days. 

    data=open(datafile)#Open and parse csv.
    parse=csv.DictReader(data)
    for rows in parse: #This loop iterates through each row and updates the counter so we can print the total number of rows excluding the header row. 
        counter +=1
    print ("The total number of rows actually containing data is",counter) #Our program knows the first row is metadata and not part of the dataset.
    

def validate_profits(datafile):
    #this will remove non numeric profits rows so we can get a count of our useful dataset.
    data=open(datafile)  #Open then parse data.
    parse=csv.DictReader(data)
    newfile= open("validated.csv", "w", newline="")#New file for output. 
    insert_header=csv.writer(newfile)#I found due to the way the data structures worked in the library I needed to use csv.writer for the header and then use DictWriter for the values
    output = csv.DictWriter(newfile, fieldnames=parse.fieldnames)#This line makes sure our values go into the correct column. 
    headers=['Year','Rank','Company','Revenue (in millions)','Profit (in millions)']
    insert_header.writerow(headers)
    count = 0
    for row in parse:
        try:
            _ = float(row["Profit (in millions)"])#This is just a very simple way to get rid of any non numeric values
            output.writerow(row)
            count += 1
        except ValueError:
            pass
    print ("The total number of rows actually containing data is",count) #Printing the amount of row of financial data. 


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
    newfile.write(json.dumps(output_list, indent=4))#Output the JSON data
    
    

  


def highest_profit(datafile):#Sorting and printing the highest profits. 
    data=open(datafile) 
    parse=json.load(data)
    sort=sorted(parse, key=lambda x: (x["Profit (in millions)"]),reverse=True)#Sorting the JSON data by the profit row. 
    for i in range (20):#Printing top 20 results
        print(json.dumps(sort[i], indent=4, sort_keys=True))

count_rows("data.csv")
validate_profits("data.csv")
json_converter("data.csv")  
highest_profit("data2.json")
