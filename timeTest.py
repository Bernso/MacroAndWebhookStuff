import time

time_to_wait = int(input("How many seconds do you want to wait? "))
start_time = time.time()

while True:
    current_time = time.time()
    elapsed_time = current_time - start_time
    
    if elapsed_time >= time_to_wait:
        print("Time's up!")
        break
    else:
        print(elapsed_time)
        
    # Adjust the checking interval as needed
    time.sleep(0.1)
