import csv;



file_reader= open('Day2data.csv');
read = csv.reader(file_reader, delimiter='\t');
checksum = 0;
for row in read:
    list = [];
    for cell in row:
        list.append(int(cell));
    difference = max(list)-min(list);
    checksum+=difference;
        

print(checksum);

        
