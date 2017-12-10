/*
 * CPE 490 Midterm
 *
 * Author: Katelyn Charbonneau
 *
 */

#include<iostream>
#include<unistd.h> //for usleep
#include"GPIO.h"
#include<fstream>
#include<string>
#include<sstream>
using namespace exploringBB;
using namespace std;

#define LDR_PATH "/sys/bus/iio/devices/iio:device0/in_voltage"

int readAnalog(int number){
   stringstream ss;
   ss << LDR_PATH << number << "_raw";
   fstream fs;
   fs.open(ss.str().c_str(), fstream::in);
   fs >> number;
   fs.close();
   return number;
}

float getTemperature(int adc_value){
   float cur_voltage = adc_value * (1.80f/4096.0f);
   float diff_degreesC = (cur_voltage-0.75f)/0.01f;
   return (25.0f + diff_degreesC);
}

int main(int argc, char* argv[]){
	/*
	 * pin 17 = slot 23 = gpio49
	 * analog0 = slot 39
	 */
   GPIO ledGPIO(49);

   // Basic Output - Flash the LED 10 times, once per second
   ledGPIO.setDirection(OUTPUT);

   int LDRvalue = readAnalog(0);

   if(LDRvalue < 2000){
	   ledGPIO.setValue(HIGH);
	   
		   int TMPvalue = readAnalog(1);
		   float temperature = getTemperature(TMPvalue);
		   cout << LDRvalue << "," << TMPvalue << "," << temperature << endl;
	   
   }
	   else{
	   ledGPIO.setValue(LOW);
	   
	   	   cout << LDRvalue << "," << 0 << "," << 0 << endl;
   }
   return 0;
}
