from SshToServer  import SshToServer
import pandas as pd
import os
import json
import subprocess
import datetime

def append_to_csv(file_path, data):
    #df_new = pd.DataFrame(data, columns = ("INFO", "WARNING", "ERROR", "DATE FROM 1.1.1970") )
    df_new = pd.DataFrame([data])
    if os.path.isfile(file_path):
        df_existing = pd.read_csv(file_path)
        df_combined = pd.concat([df_existing, df_new])
    else:
        df_combined = df_new
    df_combined.to_csv(file_path, index = False)


my_ssh = SshToServer(r"C:\Users\edrik_cgifjkr\Desktop\Course_4_CLOUD_TECHNOLOGY\my_key_pair.pem", "13.60.25.172", "ubuntu")
#stdout, stderr = my_ssh.result_of_command("python3 server_side.py")
#result, output_error = my_ssh.runRemoteCommand("sudo python3 server_side.py")
result = my_ssh.result_of_command("sudo python3 server_side.py")
result = json.loads(result)
append_to_csv("C:\\Users\\edrik_cgifjkr\\Desktop\\Course_4_CLOUD_TECHNOLOGY\\lesson 22 - final project\\sshtoserver, client_side, server_side before modifying\\course_4_cloud_technologies_lesson_22_final_project\\syslog_status.csv" , result)

file_path = "syslog_status.csv" 
commit_message = f"Auto update {file_path} {datetime.datetime.now():%Y-%m-%d %H:%M:%S}"
subprocess.run(["git", "add", file_path])
subprocess.run(["git", "commit", "-m", commit_message])
subprocess.run(["git", "push"])
