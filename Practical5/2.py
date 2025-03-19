import matplotlib.pyplot as plt#import matplotlib
uk_countries=[57.11,3.13,1.91,5.45]
uklabels=['England','Wales','Northern Ireland','Scotland']#provide labels
china_provinces=[65.77,41.88,45.28,61.27,85.15]
cnlabels=['Zhejiang','Fujian','Jiangxi','Anhui','Jiangsu']#provide labels
uk=sorted(uk_countries)#sort uk_countries
cn=sorted(china_provinces)#sort china_provinces
print(uk)#print sorted data
print(cn)#print sorted data
plt.pie(uk, labels=uklabels, autopct=None, colors=None, startangle=0)
plt.show()#show the pie of uk
plt.pie(cn, labels=cnlabels, autopct=None, colors=None, startangle=0)
plt.show()#show the pie of cn
