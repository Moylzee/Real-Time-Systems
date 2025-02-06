import subprocess
from datetime import datetime
import schedule
import time

def run_command():
    print("Running the command")
    # Define the command to run
    command = "ntpq -p"
    
    # Run the command and capture the output
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    # Get the current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    # Define the output file name
    output_file = f"data/output_{timestamp}.txt"
    
    # Save the output to the file
    with open(output_file, "w") as file:
        file.write(result.stdout)
        file.write(result.stderr)

def schedule_task():
    schedule.every(20).minutes.do(run_command)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    schedule_task()