#Known numbers are 36----0

import os

code = 999

os.remove("codes.txt")
f = open("codes.txt", "a")


while True:
  if not code == 9999:   
    code = code+1
    print("36", code, "0")
    codeToOutput = str(36) + str(code) + str(0) + "\n"
    f.write(codeToOutput)
  else:
    print("all possible codes generated")
    print("codes outputed to codes.txt (check working dir)")
    break
f.close()
