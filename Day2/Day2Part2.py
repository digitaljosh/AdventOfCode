import csv;

file_reader= open('Day2data.csv');
read = csv.reader(file_reader, delimiter='\t');
checksum = 0;
for row in read:
    row = map(int, row);
    row = sorted(row);
    print(row);
    for cell_a in row:
        for cell_b in row:
            if cell_b == cell_a:
                pass;
            elif cell_b % cell_a == 0:
                result = cell_b/cell_a;
                checksum+=result;
       
        
print(checksum);