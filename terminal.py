import time
import random
import subprocess
from datetime import datetime

print("🚀 Auto Commit Script")

total_minutes = int(input("Enter total time in minutes (ex: 3 or 4): "))
total_commits = int(input("Enter number of commits (ex: 12-16): "))

total_seconds = total_minutes * 60

# random delays that sum approx to total time
delays = [random.randint(5, total_seconds // total_commits + 5) for _ in range(total_commits)]

# normalize delays so total fits time
scale = total_seconds / sum(delays)
delays = [int(d * scale) for d in delays]

for i in range(total_commits):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("fakecommit.txt", "a") as f:
        f.write(f"Commit {i+1} at {now}\n")

    subprocess.run(["git", "add", "fakecommit.txt"])
    subprocess.run(["git", "commit", "-m", f"auto commit {i+1} at {now}"])
    subprocess.run(["git", "push", "origin", "main"])

    print(f"✅ Commit {i+1}/{total_commits} done")

    if i < total_commits - 1:
        time.sleep(delays[i])

print("🔥 All commits done. Script finished.")
