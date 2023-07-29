#Q44. Write a program using pandas to the first three rows of a given data frame.
import pandas as pd

# Sample data for the DataFrame
data = {
    'Name': ['John', 'Jane', 'Bob', 'Alice', 'Michael'],
    'Age': [30, 25, 40, 35, 28],
    'City': ['New York', 'Los Angeles', 'Chicago', 'San Francisco', 'Seattle']
}

# Create the DataFrame
df = pd.DataFrame(data)

# Print the first three rows of the DataFrame using the head() method
first_three_rows = df.head(3)
print(first_three_rows)
