p = [('P1', 2, 5), ('P2', 3, 1), ('P3', 0, 2), ('P4', 1, 3), ('P5', 1, 6)]

t = 0
done = []

total_tat = 0
total_wt = 0

while len(done) < len(p):
    a = [x for x in p if x[1] <= t and x not in done]

    if not a:
        t = min(x[1] for x in p if x not in done)
        continue

    x = min(a, key=lambda x: x[2])
    pid, at, bt = x

    t += bt
    ct = t
    tat = ct - at
    wt = tat - bt

    total_tat += tat
    total_wt += wt

    print(pid, "CT", ct, "TAT", tat, "WT", wt)
    done.append(x)

n = len(p)
avg_tat = total_tat / n
avg_wt = total_wt / n

print("-" * 30)
print(f"Average TAT = {avg_tat:.2f}")
print(f"Average WT = {avg_wt:.2f}")
