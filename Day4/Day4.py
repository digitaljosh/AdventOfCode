import csv;

file_reader= open('Day4data.csv');
read = csv.reader(file_reader);
num_valid_rows = 0;
row =0;
for row in read:
    new_row = []
    matches = False;
    for item in row:
        new_row.extend(item.split());
     
    
    for i in range(len(new_row)-1):
        row = len(new_row);
        pw_a = new_row[i];
        if matches == True:
            break;
       
        for k in range(len(new_row)-1):
            if k+i+1 <= len(new_row)-1:
                pw_b = new_row[k+i+1];
                if pw_a == pw_b:
                    matches = True;
                    break;
    
    if matches == False:
            num_valid_rows+=1;
            row=0;
                

print(num_valid_rows);
