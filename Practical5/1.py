import matplotlib.pyplot as plt#import matplotlib
dict={'JavaScript':62.3,'HTML':52.9,'Python':51,'SQL':51,'TypeScript':38.5}
print(dict)#print the dictionary
k=dict.keys()#keys of dict
v=dict.values()#values of dict
plt.figure(figsize=(10, 6))
plt.bar(k, v, color='blue')
plt.title('popularity of programming languages', fontsize=14)#title for the figure
plt.xlabel('programming language', fontsize=12)# label for x
plt.ylabel('percentage(%)', fontsize=12)#label for y  
plt.tight_layout()  
plt.show()#show the bars
