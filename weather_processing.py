"""
Created on Mon Feb  7 14:10:42 2022

@author: Okhrimchuk Roman
for Sierentz Global Merchants

Test task
"""


# TODO Import the necessary libraries
import findspark
findspark.init()

import re
import pandas as pd
from datetime import datetime
from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.sql.types import StringType, DecimalType, FloatType, TimestampType, DateType


# TODO Import the dataset


spark = SparkSession.builder.master("local[*]").appName("Sparkhelper").getOrCreate()
path = r'./data/weather_dataset.data'

with open(path) as f:
    lines = [re.sub(r'\s+', '|', line.strip()).split('|') for line in f]

# TODO  Assign it to a variable called data and replace the first 3 columns by a proper datetime index


@F.udf(returnType=DateType())
def convert_to_date(year: str, month: str, day: str):
    date = f"{month}-{day}-19{year}"
    return datetime.strptime(date, '%m-%d-%Y')


columns = lines[1]
data = spark.createDataFrame(lines[2:], columns)
data = data.withColumn('date', convert_to_date(F.col("Yr"), F.col('Mo'), F.col('Dy')))
columns.insert(0, 'date')

# TODO Check if everything is okay with the data. Create functions to delete/fix rows with strange cases and apply them


def cast_cols_to_type(data, columns, data_type):
    for col_name in columns:
        data = data.withColumn(col_name, F.col(col_name).cast(data_type))
    return data


data = cast_cols_to_type(data, [f"loc{i}" for i in range(1, 13)], FloatType())


# TODO Write a function in order to fix date (this relate only to the year info) and apply it


@F.udf(returnType=StringType())
def fix_year(year: str):
    return f"19{year}"


data = data.withColumn('year', fix_year(F.col("Yr")))\
    .drop("Yr")\
    .withColumnRenamed('year', 'Yr')\
    .select(*columns)


# TODO Set the right dates as the index. Pay attention at the data type, it should be datetime64[ns]


data = data.toPandas()
data['date'] = pd.to_datetime(data['date'])
data.set_index('date')
data.info()


# TODO Compute how many values are missing for each location over the entire record


print("\nmissed_value: ")
missed_value = data[columns[4:]].isna().sum()
print(missed_value)


# TODO Compute how many non-missing values there are in total


print("\nnon_missed_value:")
non_missed_value = data[columns[4:]].count()
print(non_missed_value)


# TODO Calculate the mean windspeeds of the windspeeds over all the locations and all the times


print("\nmean windspeeds:")
mean_windspeeds = data.describe().loc['mean'].mean()
print(mean_windspeeds)


# TODO Create a DataFrame called loc_stats and calculate the min, max and mean windspeeds and standard deviations of the windspeeds at each location over all the days


loc_stats = data.describe().loc[['min', 'max', 'mean', 'std']]


# TODO Find the average windspeed in January for each location





# TODO Downsample the record to a yearly frequency for each location


# TODO Downsample the record to a monthly frequency for each location


# TODO Downsample the record to a weekly frequency for each location


# TODO Calculate the min, max and mean windspeeds and standard deviations of the windspeeds across all locations for each week (assume that the first week starts on January 2 1961) for the first 21 weeks
