from a_read_in_the_data_PARAMETERS import cs, di

print("The head of cs is:\n", cs.head(2), "\n")
print("The head of cs is:\n", di.head(2), "\n")

# Check the dates in the data:

u = cs['date'].unique()
print('The unique values in cs date are: \n', sorted(u), '\n')

u = di['date'].unique()
print('The unique values in di date are: \n', sorted(u), '\n')


