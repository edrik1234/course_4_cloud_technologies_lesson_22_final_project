import subprocess
import time
import json

def run_local_command(command):
    try:
        # Run the command
        result = subprocess.run(command, shell = True, check = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, text = True, cwd = "/var/log")
        if result.stdout:
            return result.stdout
        else:
            return result.stderr

    except subprocess.CalledProcessError as e:
        print(f"Command '{command}' returned non-zero exit status {e.returncode}")
        print(f"Error output: {e.stderr}")


dicitionary_of_statuses = {}
#result = run_local_command("sudo grep -i -E ERROR|INFO|WARNING  syslog |wc -l |sudo tee my_sys_log_alert_file.txt > /dev/null")


search_words = ["ERROR", "INFO", "WARN"]
for word in search_words:
    dicitionary_of_statuses[word] = int(run_local_command(f'sudo grep -i {word} /var/log/syslog | wc -l').strip())
dicitionary_of_statuses["Time_Stamp"] = int(run_local_command("date +%s").strip())
print(json.dumps(dicitionary_of_statuses))

# dicitionary_of_statuses["ERROR"] = int(run_local_command("sudo grep -i ERROR /var/log/syslog | wc -l").strip())
# dicitionary_of_statuses["INFO"]  = int(run_local_command("sudo grep -i INFO /var/log/syslog | wc -l").strip())
# dicitionary_of_statuses["WARN"]  = int(run_local_command("sudo grep -i WARN /var/log/syslog | wc -l").strip())


