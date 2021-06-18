import statistics
import pandas as pd
import csv
import plotly.express as px
import plotly.figure_factory as ff


df = pd.read_csv("students.csv")
list = df["math score"].to_list()
mean = statistics.mean(list)
median = statistics.median(list)
mode = statistics.mode(list)

print("Mean, Median and Mode of math score is {}, {} and {} respectively".format(mean,median,mode))

sd = statistics.stdev(list)
first_sd_start, first_sd_end = mean-sd, mean+sd
second_sd_start, second_sd_end =mean-sd*2, mean+sd*2
third_sd_start, third_sd_end = mean-sd*3, mean+sd*3

data_within_first_sd = [result for result in list if result> first_sd_start and result< first_sd_end]
data_within_second_sd = [result for result in list if result> second_sd_start and result< second_sd_end]
data_within_third_sd = [result for result in list if result> third_sd_start and result< third_sd_end]
print("{}% of data for math score lies between first standered deviation".format(len(data_within_first_sd)*100/len(list)))
print("{}% of data for math score lies between second standered deviation".format(len(data_within_second_sd)*100/len(list)))
print("{}% of data for math score lies between third standered deviation".format(len(data_within_third_sd)*100/len(list)))

list = df["reading score"].to_list()
mean = statistics.mean(list)
median = statistics.median(list)
mode = statistics.mode(list)

print("Mean, Median and Mode of reading score is {}, {} and {} respectively".format(mean,median,mode))

sd = statistics.stdev(list)
first_sd_start, r_first_sd_end = mean-sd, mean+sd
second_sd_start, r_second_sd_end = mean-sd*2, mean+sd*2
third_sd_start, r_third_sd_end = mean-sd*3, mean+sd*3

data_within_first_sd = [result for result in list if result> first_sd_start and result< first_sd_end]
data_within_second_sd = [result for result in list if result> second_sd_start and result< second_sd_end]
data_within_third_sd = [result for result in list if result> third_sd_start and result< third_sd_end]
print("{}% of data for reading score lies between first standered deviation".format(len(data_within_first_sd)*100/len(list)))
print("{}% of data for reading score lies between second standered deviation".format(len(data_within_second_sd)*100/len(list)))
print("{}% of data for reading score lies between third standered deviation".format(len(data_within_third_sd)*100/len(list)))

list = df["writing score"].to_list()
mean = statistics.mean(list)
median = statistics.median(list)
mode = statistics.mode(list)

print("Mean, Median and Mode of writing score is {}, {} and {} respectively".format(mean, median, mode))

std = statistics.stdev(list)
first_sd_start, first_sd_end = mean-std, mean+std
second_sd_start, second_sd_end = mean-std*2, mean+std*2
third_sd_start, third_sd_end = mean-std*3, mean+std*3

data_within_first_sd = [result for result in list if result> first_sd_start and result< first_sd_end]
data_within_second_sd = [result for result in list if result> second_sd_start and result< second_sd_end]
data_within_third_sd = [result for result in list if result> third_sd_start and result< third_sd_end]
print("{}% of data for writing score lies between first standered deviation".format(len(data_within_first_sd)*100/len(list)))
print("{}% of data for writing score lies between second standered deviation".format(len(data_within_second_sd)*100/len(list)))
print("{}% of data for writing score lies between third standered deviation".format(len(data_within_third_sd)*100/len(list)))

