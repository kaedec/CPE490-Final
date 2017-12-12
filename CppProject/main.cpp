/*
 * CPE 490 Midterm
 *
 * Author: Katelyn Charbonneau
 * Date: 12/14/2017
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

#define LDR_PATH "/sys/bus/iio/devices/iio:device0/in_voltage" // used for both LDR and TMP sensors

//This function reads the value from the requested file (either AIN0 or AIN1)
int readAnalog(int number){
   stringstream ss;
   ss << LDR_PATH << number << "_raw";
   fstream fs;
   fs.open(ss.str().c_str(), fstream::in);
   fs >> number;
   fs.close();
   return number;
}

//This function converts the TMP reading to Celcius
float getTemperature(int adc_value){
   float cur_voltage = adc_value * (1.80f/4096.0f);
   float diff_degreesC = (cur_voltage-0.75f)/0.01f;
   return (25.0f + diff_degreesC);
}

int main(int argc, char* argv[]){
	/*
	 * GPIO Locations:
	 * LED: pin 17 = slot 23 = gpio49
	 * LDR: analog0 = slot 39
	 * TMP: analog1 = slot 40
	 */
	
   GPIO ledGPIO(49); // Using GPIO class
   ledGPIO.setDirection(OUTPUT);

   int LDRvalue = readAnalog(0); //Get reading from LDR

   if(LDRvalue < 2000){ //2000 was chosen as the breakpoint for the environment that testing was completed in
	   ledGPIO.setValue(HIGH); //Turn the indicator LED on
		
			/*
			 * This reads the value from the TMP sensor, converts it to Celcius, and then writes
			 * the LDR reading, TMP reading, and Celcius conversion to the output.
			 * This output will be grabbed by the Python script.
			 */
		   int TMPvalue = readAnalog(1);
		   float temperature = getTemperature(TMPvalue);
		   cout << LDRvalue << "," << TMPvalue << "," << temperature << endl;
	   
   }
	   else{
	   ledGPIO.setValue(LOW); //Turn the indicator LED off
	   
   }
   return 0;
}
