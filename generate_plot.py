import os
import json
import pandas as pd
import matplotlib.pyplot as plt

base_dir = "results"
records = []

for folder in os.listdir(base_dir):
    folder_path = os.path.join(base_dir, folder)
    if os.path.isdir(folder_path):
        for fname in os.listdir(folder_path):
            if fname.endswith(".json"):
                with open(os.path.join(folder_path, fname)) as f:
                    data = json.load(f)
                    data["run"] = folder   # add folder as run label
                    data["filename"] = fname
                    records.append(data)

df = pd.DataFrame(records)
print(df.head())

for filename, group in df.groupby("filename"):
    plt.figure()
    plt.plot(group["run"], group["real_time_ms"], marker="o", label="real_time_ms")
    plt.plot(group["run"], group["cpu_time_ms"], marker="o", label="cpu_time_ms")
    plt.plot(group["run"], group["gc_time_ms"], marker="o", label="gc_time_ms")
    plt.title(f"Timing for {filename}")
    plt.xlabel("Run")
    plt.ylabel("Time (ms)")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"{filename[:-5]}.png")
