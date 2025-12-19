import subprocess
import time

# 1. Dashboard start karo (Background mein)
print("Starting Dashboard...")
subprocess.Popen(["streamlit", "run", "app.py"])

time.sleep(5) # Dashboard load hone ka intezar

# 2. Main AI Engine start karo
print("Starting AI Guard...")
subprocess.run(["python", "main.py"])