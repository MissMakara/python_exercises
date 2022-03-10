from datetime import datetime
#get timestamp in UTC and append to list 
time_list = []
rr_lis = []

for i in range (10):
    now_utc = datetime.utcnow()
    #now_current = datetime.now()

    time_list.append(now_utc)


#iterate in index form
for x in range (len(time_list)):
    #print(len(time_list))
    if x < (len(time_list)-1):
        print(x)
        timestamp_1 = time_list[x]
        timestamp_2 = time_list[x+1]
        print(timestamp_1)
        print(timestamp_2)

        time_diff = (timestamp_2 - timestamp_1)
        rr_time = round(time_diff.total_seconds() * 1000)

        rr_lis.append(rr_time)

print(rr_lis)


#print(time_stamp_1,",", time_stamp_2)
#time_delta = (time_stamp_2 -  time_stamp_1)
#print("now current time", now_current)
#print("now UTC time", now_utc)
#print("time difference", type(time_diff))
#print(execution_time)

#to do:
#figure out how to get time difference in python in milliseconds
#add that here