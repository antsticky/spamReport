from datetime import datetime

PERIODS = [
    ("year", 60 * 60 * 24 * 365),
    ("month", 60 * 60 * 24 * 30),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("minute", 60),
    ("second", 1)
]


def human_readable_time_diff(start_time: datetime, end_time: datetime) -> str:
    time_diff = end_time - start_time
    seconds = int(time_diff.total_seconds())

    parts = []
    for period_name, period_seconds in PERIODS:
        if seconds >= period_seconds:
            period_value, seconds = divmod(seconds, period_seconds)
            if period_value == 1:
                parts.append(f"{period_value} {period_name}")
            else:
                parts.append(f"{period_value} {period_name}s")

    if len(parts) == 1:
        return parts[0]
    elif len(parts) == 2:
        return f"{parts[0]} and {parts[1]}"
    else:
        return ", ".join(parts[:-1]) + " and" + parts[-1]
