import matplotlib.pyplot as plt
import seaborn as sns 
import itertools 


lst = [11, 22, 44, 55, 66, 77, 88, 99, 0]

i = 0
j = 1

lst2 = [lst[i]*2 if lst[i]*2 == lst[i+1] else (lst[i], lst[i+1]) for i in range(len(lst)-1)]

lst2_flattened = list(itertools.chain(*[(i,) if not isinstance(i, tuple) else i for i in lst2]))

# create hist 
sns.histplot(lst2_flattened, bins=10, kde=False, color='skyblue', edgecolor='black')

# customize hist
plt.title("Histogram of lst2")
plt.xlabel("value")
plt.ylabel('frequency')


plt.show()