print("Inputs")
emer_vehicle=input("Is there an emeregency vehicle nearby? (yes/no)")
pedestrians=input("Are pedestrians currently crossing? (yes/no)")
traffic_light=input("Is the traffic light green? (yes/no)")
raining=input("Is it raining heavily? (yes/no)")
accident=input("Is there an accident reported ahead? (yes/no)")
school_zone=input("Is this a school zone? (yes/no)")
rush_hour=input("Is it rush hour? (yes/no)")

print("Outputs")
if(emer_vehicle.lower()=='yes'):
    print("emergency vehicle nearby,all traffic must stop")
elif pedestrians.lower()=='yes':
    print("pedestrians are crossing,vehicles must stop")
elif accident.lower()=='yes':
    print("Caution:Accident Ahead.Proceed Slowly")
elif raining.lower()=='yes':
    if traffic_light.lower()=='no':
        print("Wait for Green visibility Low")
    if traffic_light.lower()=='yes':
        print("Proceed Slowly wet roads")
elif school_zone.lower()=='yes':
    if rush_hour.lower()=='yes':
        print("Extra Caution: School Zone during Rush Hour")
    if rush_hour.lower()=='no':
        print("Drive carefully- School Zone")
elif (traffic_light.lower()=='yes'):
        print("You may go")
else: print ("Stop and wait for green")
    

    
    
