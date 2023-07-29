'''
Q45. Write a program using pandas to create and display a dataframe from a specified
dictionary data which
has the index labels
sample dataframe
exam_data = {"name":[choose any 10 names], "score":[10 scores],"attempts":[10
entries],"qualify":[10 boolean values]}
labels=['a','b',...10 label]'''
import pandas as pd

# Sample data for the DataFrame
exam_data = {
    "name": ['John', 'Jane', 'Bob', 'Alice', 'Michael', 'Emma', 'David', 'Olivia', 'Ethan', 'Sophia'],
    "score": [85, 92, 78, 90, 88, 95, 82, 89, 75, 93],
    "attempts": [1, 2, 1, 3, 2, 1, 2, 3, 1, 2],
    "qualify": [True, True, False, True, True, True, False, True, False, True]
}

# Create the DataFrame with specified index labels
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels)

# Display the DataFrame
print(df)

