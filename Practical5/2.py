import matplotlib.pyplot as plt#import matplotlib
uk_countries=[57.11,3.13,1.91,5.45]
china_provinces=[65.77,41.88,45.28,61.27,85.15]
uk=sorted(uk_countries)#sort uk_countries
cn=sorted(china_provinces)#sort china_provinces
print(uk)#print sorted data
print(cn)#print sorted data
plt.pie(uk, labels=None, autopct=None, colors=None, startangle=0)
plt.show()#shoe the pie of uk
plt.pie(cn, labels=None, autopct=None, colors=None, startangle=0)
plt.show()#shoe the pie of cn
