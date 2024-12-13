no_of_student=int(input("Enter the no: of students attending to the trip : "))
no_of_teacher=int(input("Enter the no: of teachers attending to the trip : "))
#small bus=16 seats and perday cost=$140
#larger bus=46 seats and per day cost=$360

#total number of participents in trip
total_members_in_trip=no_of_student+no_of_teacher


#larger bus=46
large_coaches_required=total_members_in_trip//46

remaining_participents=total_members_in_trip%46
print("large coaches required", large_coaches_required)
#small bus=16 seats
small_coaches_required=remaining_participents//16


remaining_particpants_of_small_bus=remaining_participents%16
if remaining_particpants_of_small_bus>0:
    small_coaches_required+=1
print("small coaches required",small_coaches_required)



#small bus per day cost in INDIAN CURRENCY
smallbus_perday_cost=140*88.76
largebus_perday_cost=360*88.76
print("per day cost of one small bus", smallbus_perday_cost)
print("per day cost of one large bus", largebus_perday_cost)

#total cost of hiring these coaches for a day.
small_bus_for_trip_cost=small_coaches_required*smallbus_perday_cost
large_bus_for_trip_cost=large_coaches_required*largebus_perday_cost
print("total cost of hiring small coaches for a day.",small_bus_for_trip_cost)
print("total cost of hiring large coaches for a day.",large_bus_for_trip_cost)


total_cost_for_trip=small_bus_for_trip_cost+large_bus_for_trip_cost
print("total_cost_for_trip",total_cost_for_trip)

cost_perhead_of_trip=total_cost_for_trip//total_members_in_trip
print("cost_perhead_for_trip",cost_perhead_of_trip)