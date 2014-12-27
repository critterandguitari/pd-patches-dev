
import subprocess
import time
#subprocess.Popen(["rm","-r","some.file"])

pd = subprocess.Popen(["/Applications/Pd-0.46-4.app/Contents/MacOS/Pd"])

time.sleep(10)

pd.kill()






