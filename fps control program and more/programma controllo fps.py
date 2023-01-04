import time
import psutil
import GPUtil

def get_system_stats():
    # Initialize variables to track the frame count and elapsed time
    frame_count = 0
    start_time = time.time()

    # Loop until the user closes the window
    while True:
        # Increment the frame count
        frame_count += 1

        # Calculate the elapsed time
        elapsed_time = time.time() - start_time

        # If the elapsed time is greater than 1 second, calculate the FPS
        if elapsed_time > 1:
            fps = frame_count / elapsed_time
            print("FPS:", fps)

            # Reset the frame count and start time
            frame_count = 0
            start_time = time.time()

        # Get the CPU temperature
        cpu_temp = get_cpu_temp()
        print("CPU Temperature:", cpu_temp)

        # Get the GPU temperature
        gpu_temp = get_gpu_temp()
        print("GPU Temperature:", gpu_temp)

        # Get the CPU usage
        cpu_usage = psutil.cpu_percent()
        print("CPU Usage:", cpu_usage)

        # Get the GPU usage
        gpu_usage = get_gpu_usage()
        print("GPU Usage:", gpu_usage)

def get_cpu_temp():
    # Replace this with code to get the CPU temperature
    return 0

def get_gpu_temp():
    # Replace this with code to get the GPU temperature
    return 0

def get_gpu_usage():
    # Replace this with code to get the GPU usage
    return 0

# Call the get_system_stats function to start displaying the system stats
get_system_stats()
