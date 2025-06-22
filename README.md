# civ-ipriot-car-park
Object-Oriented Programming - Car Park System - AT3project IP4RIoT

**Project Overview:**  
The City of Moondalup has commissioned the development of a smart carpark application to manage and monitor parking spaces in several key areas around the city. The application will integrate with sensors at each parking bay to detect when cars enter and exit, thereby providing real-time data on parking availability. Additionally, the application will display the number of available parking bays and current temperature to assist drivers in making informed parking decisions.

**Objective:**  
To develop a robust, user-friendly smart carpark application that seamlessly integrates with parking bay sensors, provides real-time parking data, and improves the overall efficiency of car parks in the City of Moondalup.  

**Key Components of the Smart Carpark System:**
1. Sensors:
   1. EntrySensor: Detects cars entering the carpark.
   2. ExitSensor: Detects cars exiting the carpark.
2. Carpark Management Center:
   1. Tracks the status of each parking bay (occupied or available).
   2. Maintains a log of all cars entering and exiting, including timestamps.
3. Display:
   1. Shows the number of available parking bays.
   2. Displays the current temperature (sourced from an external weather data file).
4. Car Class:
   1. Represents a car with attributes such as license plate, car model, entry time, and exit time.
5. Carpark Class:
   1. Manages the collection of cars and parking bays.
   2. Interfaces with the sensors to update parking bay status.

**Client Requirements:**  
1. The system must accurately track the status of each parking bay in real-time.
2. The display must be updated promptly as cars enter or exit.
3. The system should be robust, easy to maintain, and scalable for future enhancements.
4. The application must follow best coding practices and include comprehensive unit testing.
