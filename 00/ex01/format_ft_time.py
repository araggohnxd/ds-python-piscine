import datetime as dt

seconds_since_epoch = dt.datetime.now().timestamp()
comma_separated = f"{seconds_since_epoch:,.4f}"
scientific_notation = f"{seconds_since_epoch:.2e}"
mon_day_year = dt.datetime.now().strftime("%b %d %Y")

print(f"""\
Seconds since January 1, 1970: {comma_separated} or {scientific_notation} \
in scientific notation.
{mon_day_year}\
""")
