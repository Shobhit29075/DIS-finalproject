import subprocess

result = subprocess.run(["curl", "http://169.254.169.254/latest/meta-data/public-ipv4"], stdout=subprocess.PIPE)
output = result.stdout.decode('utf-8')
f = open("flaskapp", "r")
s=""
i=0
for lines in f:
    i=i+1
    if(i==3):
        s=s+"server_name "+output+";"
    else:
        s=s+lines.strip()+"\n"
print(s)
f.close()
f = open("flaskapp", "w")
f.write(s)
f.close()