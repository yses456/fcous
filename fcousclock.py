import time

def focus_clock(minutes):
    seconds = minutes * 60
    start_time = time.time()
    end_time = start_time + seconds

    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        print(f"Remaining time: {minutes:02d}:{seconds:02d}", end="\r")
        time.sleep(1)

    print("Time's up! Stay focused!")

# 调用函数，设置专注时长为25分钟
focus_clock(25)
