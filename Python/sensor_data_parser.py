#CPE 460 Final Project
#Author: Katelyn Charbonneau
#Date: 12/14/2017

import csv	#for parsing .csv file
import os	#for executing bash commands

#note that the significant weakness to this project is that due to the usage of Node-RED, absolute file paths had to be used

#execute the C++ program and write the output to a file
os.system("/home/debian/Katelyn_Charbonneau_IoT/CPE490-Final/CppProject/Debug/CPE490-Final >> /home/debian/Katelyn_Charbonneau_IoT/CPE490-Final/Python/raw_data.csv")

#open the file and parse data into a list
with open('/home/debian/Katelyn_Charbonneau_IoT/CPE490-Final/Python/raw_data.csv','rb') as f:
	reader = csv.reader(f)
	read_list = list(reader)

s1 = []
s2 = []
s3 = []

#parse through the data list created above
#place LDR Raw data into S1
#place TMP Raw data into S2
#place Celcius data into S3
for i in range(-1,len(read_list)-1):
	s1.append(read_list[i][0])
	s2.append(read_list[i][1])
	s3.append(read_list[i][2])

#debugging - uncomment any of these lines to see its contents
#print s1
#print s2
#print s3

#Convert data from string to int, or float, as required
s1 = map(int, s1)
s2 = map(int, s2)
s3 = map(float, s3)

#make new lists containing the average, minimum, and maximum values for each reading
#results[0] = average
#results[1] = minimum
#results[2] = maximum
s1_results = [float(format(sum(map(float, s1))/len(s1), '.1f')), min(s1), max(s1)]
s2_results = [float(format(sum(map(float, s2))/len(s2), '.1f')), min(s2), max(s2)]
s3_results = [float(format(sum(map(float, s3))/len(s3), '.1f')), min(s3), max(s3)]

#Open the ouput text file
#Print the data to it in a formatted manner
f = open('/home/debian/Katelyn_Charbonneau_IoT/CPE490-Final/report.txt','w+')
f.write('\t\t\tSummary of Data from Sensors\n')
f.write('\t\tAverage\t\tMinimum Reading\t\tMaximum Reading\n')
f.write('LDR Raw\t\t%.1f\t\t%i\t\t\t%i\n' % (s1_results[0], s1_results[1], s1_results[2]))
f.write('TMP Raw\t\t%.1f\t\t%i\t\t\t%i\n' % (s2_results[0], s2_results[1], s2_results[2]))
f.write('TMP Celcius\t%.1f\t\t%i\t\t\t%i\n' % (s3_results[0], s3_results[1], s3_results[2]))
