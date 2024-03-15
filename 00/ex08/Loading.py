def ft_tqdm(iterable):
    total = len(iterable)

    for i, item in enumerate(iterable, start=1):
        yield item

        percent = i * 100 // total
        str_progress = f"{percent:>3}%|{'█' * percent:<100}|"
        str_total = f"{i}/{total}"

        print(
            f"\r{str_progress} {str_total}",
            end='',
            flush=True
        )

# The code below works more similar to the original function than the above,
# but uses external libraries, which are forbidden.

# import time
# import os


# def format_time(t):
#     mins, s = divmod(int(t), 60)
#     h, m = divmod(mins, 60)
#     return f'{h:d}:{m:02d}:{s:02d}' if h else f'{m:02d}:{s:02d}'


# def ft_tqdm(iterable):
#     total = len(iterable)
#     start = time.time()
#     terminal_width = os.get_terminal_size().columns

#     for i, item in enumerate(iterable, start=1):
#         yield item

#         elapsed = time.time() - start
#         speed = i / elapsed
#         eta = (total - i) / speed
#         percent = i / total * 100

#         str_percent = f"{percent:3.0f}%|"
#         str_total = f"| {i:>{len(str(total))}}/{total} "
#         str_time = f"[{format_time(elapsed)}<{format_time(eta)}, "
#         str_speed = f"{speed:.2f}it/s]"

#         strs_len = len(str_percent + str_total + str_time + str_speed)
#         progress_bar_size = terminal_width - strs_len
#         current_size = int(i / total * progress_bar_size)

#         str_progress = f"{'█' * current_size:<{progress_bar_size}}"

#         print(
#             f"\r{str_percent}{str_progress}{str_total}{str_time}{str_speed}",
#             end='',
#             flush=True
#         )
