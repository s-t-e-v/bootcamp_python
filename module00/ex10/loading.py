from time import sleep, time


def ft_progress(lst):
    total = len(lst)
    start = time()
    bar_length = 20

    for i, elem in enumerate(lst, 1):
        elapsed = time() - start
        percentage = int((i / total) * 100)
        filled_length = int(bar_length * percentage / 100)

        bar = "=" * filled_length + (">" if percentage < 100 else "")
        eta = (elapsed / i) * total

        print(
            f"\r\33[KETA: {eta:.2f}s "
            f"[{percentage:3d}%][{bar:<20}] "
            f"{i}/{total} | elapsed time {elapsed:.2f}s",
            end="",
            flush=True
        )

        yield elem


# Examples
listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    sleep(0.01)
print()
print(ret)

listy = range(3333)
ret = 0
for elem in ft_progress(listy):
    ret += elem
    sleep(0.005)
print()
print(ret)
