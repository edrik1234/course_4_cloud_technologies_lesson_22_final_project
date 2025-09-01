import paramiko


class SshToServer:
    def __init__(self, pem_file_path, host, username):
        self.pem_file_path = pem_file_path
        self.host = host
        self.username = username
        self.sshClient = paramiko.SSHClient()
        self.connect()

    def connect(self):
        self.sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        private_key = paramiko.RSAKey.from_private_key_file(self.pem_file_path)
        self.sshClient.connect(hostname = self.host, username = self.username, pkey = private_key)

    def runRemoteCommand(self, command):   
        try:   
            stdin, stdout, stderr = self.sshClient.exec_command(command) # tuple ( , , )
            output = stdout.read().decode()
            error = stderr.read().decode()
            return output, error
        except Exception as e:
            print(f"An error occurred: {e}")

    def result_of_command(self, command):
        try:
            stdin, stdout, stderr = self.sshClient.exec_command(command)
            output = stdout.read().decode()
            error  = stderr.read().decode()
            if output:
                return output
            elif error:
                return f"Error is : {error}"
            else:
                return "no output or error"
        except Exception as error_description:
            print(f"Error is {error_description}")
            

my_ssh = SshToServer(r"C:\Users\edrik_cgifjkr\Desktop\Course_4_CLOUD_TECHNOLOGY\my_key_pair.pem", "13.60.25.172", "ubuntu")
file_name = input("please enter file name: ")
time_to_wait = input("Please enter how much time to wait: ")
command = f"./coures_4_lesson_31_final_project.sh {file_name} {time_to_wait}"
# second way -> command_2 = "./coures_4_lesson_31_final_project.sh " + file_name + " "  + time_to_wait 
result = my_ssh.result_of_command(command)
print(result)

