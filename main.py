# Function to create table
def create_table(rows, cols):
    table = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = int(input(f"Enter the value for cell [{i}][{j}]: "))
            row.append(value)
        table.append(row)
    return table

# Function to multiply two tables
def multiply_tables(table1, table2):
    result = []
    for i in range(len(table1)):
        row = []
        for j in range(len(table2[0])):
            cell_value = 0
            for k in range(len(table1[0])):
                cell_value += table1[i][k] * table2[k][j]
            row.append(cell_value)
        result.append(row)
    return result

# Main program
rows1 = int(input("Enter the number of rows for table 1: "))
cols1 = int(input("Enter the number of columns for table 1: "))
table1 = create_table(rows1, cols1)

rows2 = int(input("Enter the number of rows for table 2: "))
cols2 = int(input("Enter the number of columns for table 2: "))
table2 = create_table(rows2, cols2)

if cols1 != rows2:
    print("Error: Number of columns in table 1 must be equal to the number of rows in table 2")
else:
    result_table = multiply_tables(table1, table2)

    print("Result Table:")
    for row in result_table:
        print(row)
