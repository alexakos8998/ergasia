import sys
import matplotlib.pyplot as plt
import numpy as np

with open(sys.argv[1], 'r') as f:
    text = f.read()

freq = {}
for c in text: 
    if c in freq: 
        freq[c] += 1
    else: 
        freq[c] = 1

per = [val / len(text) for val in list(freq.values())]
fig = plt.figure(figsize=(8,8))
ax1 = fig.add_subplot(2,1,1)
ax1.bar(freq.keys(), per)
ax1.set_title("Occurancy percentage for each character")
ax1.set_ylabel("Percentage")
ax1.set_xlabel("Characters")

ax2 = fig.add_subplot(2,1,2)
ax2.bar(freq.keys(), freq.values())
ax2.set_title("Frequency for each character")
ax2.set_ylabel("Frequency")
ax2.set_xlabel("Characters")
fig.tight_layout(pad=3.0)
# Save the full figure...
fig.savefig('quest2.png')
