import tracemalloc

tracemalloc.start(25)

import numpy as np

objs = []


def make_object(size):
    x = 10 * np.ones(size)
    objs.append(x)


make_object(2000000)

snapshot1 = tracemalloc.take_snapshot()

make_object(1000000)

snapshot2 = tracemalloc.take_snapshot()


# --- show second snapshot
top_stats = snapshot2.statistics("traceback")

print("[ Top 10 memory users ]")
for stat in top_stats[:10]:
    print(f"-  {stat}")

stat = top_stats[0]  # pick the biggest memory block
print("%s memory blocks: %.1f KiB" % (stat.count, stat.size / 1024))
for line in stat.traceback.format():
    print(line)

# --- show stats for difference between first and second snapshots
diff_stats = snapshot2.compare_to(snapshot1, "traceback")

print("[ Top 10 differences ]")
for stat in diff_stats[:10]:
    print(f"-  {stat}")

stat = diff_stats[0]  # pick the biggest memory block
print("%s memory blocks: %.1f KiB" % (stat.count, stat.size / 1024))
for line in stat.traceback.format():
    print(line)
