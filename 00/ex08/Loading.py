import time


def format_time(seconds):
    m, s = divmod(seconds, 60)
    return f"{int(m):02d}:{int(s):02d}"


def ft_tqdm(iterable):
    total = len(iterable)
    progress = 0
    start = time.time()

    for i, item in enumerate(iterable, start=1):
        yield item

        elapsed = time.time() - start
        speed = i / elapsed
        eta = (total - i) / speed
        progress += 1
        percent_complete = progress * 100 // total

        str_speed = f"{speed:.2f}it/s"
        str_time = f"{format_time(elapsed)}<{format_time(eta)}"
        str_total = f"{item + 1:}/{total}"
        str_percent = f"{percent_complete:>3}%|{'█' * percent_complete:<100}|"

        print(
            f"\r{str_percent} {str_total} [{str_time}, {str_speed}]",
            end='',
            flush=True
        )
