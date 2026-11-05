import pandas as pd
df=pd.read_csv("diabetes.csv")
#(i)
print("Column names:")
print(df.columns)
#(ii)
print("First 10 rows:")
print(df.head(10))
#(iii)
print("Mean of Blood Pressure:")
print(df['BloodPressure'].mean())
#(iv)
print("First 4 rows of columns 3,4,5")
print(df.iloc[:4,2:5])
#(v)max-min normalization:
min_bp=df['BloodPressure'].min()
max_bp=df['BloodPressure'].max()
df['NormalizedBP']=(df['BloodPressure']-min_bp)/(max_bp-min_bp)
print("Normalized BP:")
print(df[['BloodPressure','NormalizedBP']])
#(vi)categorize age:
def categorize_age(age):
    if age>=1 and age<=18:
        return "Youth"
    elif age>=19 and age<=50:
        return "Adult"
    else:
        return "Senior"
df['AgeCategory']=df['Age'].apply(categorize_age)
print("Age Category:")
print(df[['Age','AgeCategory']])
