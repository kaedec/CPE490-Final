import csv
import os

os.system("/home/debian/Katelyn_Charbonneau_IoT/CPE490-Final/CppProject/Debug/CPE490-Final >> /home/debian/Katelyn_Charbonneau_IoT/CPE490-Final/Python/raw_data.csv")

with open('/home/debian/Katelyn_Charbonneau_IoT/CPE490-Final/Python/raw_data.csv','rb') as f:
	reader = csv.reader(f)
	read_list = list(reader)

s1 = []
s2 = []
s3 = []

for i in range(-1,len(read_list)-1):
	s1.append(read_list[i][0])
	s2.append(read_list[i][1])
	s3.append(read_list[i][2])

print s1
print s2
print s3

s1 = map(int, s1)
s2 = map(int, s2)
s3 = map(int, s3)

s1_results = [float(format(sum(map(float, s1))/len(s1), '.1f')), min(s1), max(s1)]
s2_results = [float(format(sum(map(float, s2))/len(s2), '.1f')), min(s2), max(s2)]
s3_results = [float(format(sum(map(float, s3))/len(s3), '.1f')), min(s3), max(s3)]

f = open('/home/debian/Katelyn_Charbonneau_IoT/CPE490-Final/report.txt','w+')
f.write('\t\t\tSummary of Data from Sensors\n')
f.write('\t\tAverage\t\tMinimum Reading\t\tMaximum Reading\n')
f.write('LDR Raw\t\t%.1f\t\t%i\t\t\t%i\n' % (s1_results[0], s1_results[1], s1_results[2]))
f.write('TMP Raw\t\t%.1f\t\t%i\t\t\t%i\n' % (s2_results[0], s2_results[1], s2_results[2]))
f.write('TMP Celcius\t%.1f\t\t%i\t\t\t%i\n' % (s3_results[0], s3_results[1], s3_results[2]))
