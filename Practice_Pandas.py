import pandas as pd

data = {
    "Name": ["Aarav", "Bhavna", "Chirag", "Diya", "Esha", "Farhan"],
    "Maths": [85, 90, 78, 92, 88, 76],
    "Science": [80, 95, 70, 89, 84, 82],
    "English": [75, 89, 68, 90, 85, 80],
    "City": ["Mumbai", "Delhi", "Pune", "Kolkata", "Delhi", "Pune"]
}

df = pd.DataFrame(data)
#1
# print(df[["Maths","Science","English"]].agg(["mean","median","std"]))

#2
df["Average"] = df[["Maths","Science","English"]].mean(axis = 1)
# print(df[["Name","Average"]])

#3
df["Total"] = df[["Maths","Science","English"]].sum(axis=1)
df["Rank"] = df["Total"].rank(ascending=False)
#4
df.sort_values(["English"],inplace=True)
df.sort_values(["Science"],ascending=False,inplace=True)
# print(df)
#5
print(df.groupby("City")["Total"].mean())

#6
city_maths_mean = df.groupby("City")["Maths"].transform('mean')
df["Flag"] = df["Maths"] > city_maths_mean
print(df)

#7
print(df.corr(numeric_only=True))

city_avg_totals = df.groupby('City')[['Science','Total']].mean().reset_index()
city_avg_totals.columns = ['City','Avg_Sc_Marks' ,'Avg_Total_Marks']

print("\nAverage total marks by city:")
print(city_avg_totals[city_avg_totals["Avg_Total_Marks"]>250])

print(city_avg_totals[city_avg_totals['Avg_Sc_Marks']==city_avg_totals["Avg_Sc_Marks"].max()]['City'])

