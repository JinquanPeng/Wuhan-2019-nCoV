from datetime import datetime
import subprocess
from apscheduler.schedulers.blocking import BlockingScheduler


def update_data():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cmds = [
        ["git", "pull"],
        ["pipenv", "run", "python", "dataset.py"],
        ["git", "commit", "-am", f"""{now}自动更新"""],
        ["git", "push"]
    ]
    for cmd in cmds:
        print(" ".join(cmd))
        print(subprocess.check_output(cmd).decode())


scheduler = BlockingScheduler(timezone="Asia/Shanghai")
scheduler.add_job(update_data, 'cron', minute="57")
scheduler.start()
