import matplotlib.pyplot as plt#import matplotlib
dict={'JavaScript':62.3,'HTML':52.9,'Python':51,'SQL':51,'TypeScript':38.5}
print(dict)#print the dictionary
k=dict.keys()#keys of dict
v=dict.values()#values of dict
bars = plt.bar(k, v, color='blue')#draw the bar
for bar in bars:
    height = bar.get_height() #get height
    plt.text(bar.get_x() + bar.get_width() / 2, height, str(height), ha='center', va='bottom') #add data on the bars
plt.show()#show the bar
