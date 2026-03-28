from loguru import logger
import os

counter_file = "logs/counter.txt"
os.makedirs("logs", exist_ok=True)

try:
    with open(counter_file, "r") as f:
        last_num = int(f.read().strip())
except (FileNotFoundError, ValueError):
    last_num = 0

next_num = last_num + 1

with open(counter_file, "w") as f:
    f.write(str(next_num))


def start_logging():
    logger.remove()

    logger.add(f"logs/common_{next_num}.log",
               filter=lambda record: record["extra"].get("type") != "animal",
               format="{time} | {level} | {message}",
               level="DEBUG"
               )

    logger.add(
        f"logs/animals_{next_num}.log",
        filter=lambda record: record["extra"].get("type") == "animal",
        format="{message}",
        level="DEBUG"
    )
