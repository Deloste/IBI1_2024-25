import matplotlib.pyplot as plt#import matplotlib
dict={'JavaScript':62.3,'HTML':52.9,'Python':51,'SQL':51,'TypeScript':38.5}
print(dict)#print the dictionary
i=input('Language:')#get the inputted language
print(dict[i])#output the matched value
k=dict.keys()#keys of dict
v=dict.values()#values of dict
plt.bar(k,v,color='blue')#draw the bar
