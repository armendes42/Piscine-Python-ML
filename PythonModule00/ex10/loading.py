import time
import sys

def ft_progress(lst):
    start = time.time()
    size=20
    out = sys.stdout
    count = len(lst)
    def show(j):
        x = int(size * j / count)
        percentage = (j * 100) // count
        time_elapsed = time.time() - start
        time_elapsed = round(time_elapsed, 2)
        if j != 0:
            eta = (time_elapsed / j) * (count - j)
            eta = round(eta, 2)
        else:
            eta = 0
        out.write("\r" + "ETA: {:.2f}s [{}%][{}{}{}] {}/{} | elapsed time {:.2f}s".format(eta, percentage, "=" * (x - 1), ">", " " * (size - x), j, count, time_elapsed))
        out.flush()
    show(0)
    for i, item in enumerate(lst):
        yield item
        show(i+1)
    print("\n", flush=True, file=out)



listy = range(3333)
ret = 0
for elem in ft_progress(listy):
    ret += elem
    time.sleep(0.005)
print()
print(ret)
