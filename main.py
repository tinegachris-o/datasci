import matplotlib.pyplot as plt
import pandas as pd
"""
variable_x=[1,3,5,8,9,12,34]
variable_y=[x*3 for x in variable_x]
plt.plot(variable_x,variable_y)
plt.title("Tempereture over hours")
plt.xlabel("Hour")
plt.ylabel("Temperature")
plt.show()
#Bar Chart
categories=["Apples","Oranges","Bananas"]
values=[30,45,20]
plt.bar(categories,values,color="green")
plt.title("Fruit sales")
plt.xlabel("Fruit Type")
plt.ylabel("Quantity sold")
plt.show()

#Horizontal Barchrt
categories=["Apples","Oranges","Bananas"]
values=[30,45,20]
plt.title("Fruit sales (Horizontal)")
plt.xlabel("Quantity Sold")
plt.ylabel("Fruit Type")


plt.barh(categories,values,color="green")
plt.show()

#PIE CHART
sizes=[50,30,20]
labels=["food","Rent","Travel"]
plt.pie(sizes,labels=labels,autopct='%1.1f%%')
plt.title("Budget Distribution")
plt.show()
"""
# Scatter Plot
study_hours=[1,2,3,4,5,6]
test_scores=[10,47,70,80,82,85]
plt.scatter(study_hours,test_scores,color="red",marker="o")
plt.title("Study hours vs Test Scores")
plt.xlabel("Study Hours")
plt.ylabel("Test Score")
plt.show()