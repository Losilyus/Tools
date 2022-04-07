import os
def command(hostname, user): return os.system(f"ssh {user}@{hostname}")