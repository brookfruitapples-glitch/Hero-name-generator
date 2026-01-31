import heroes
import time
import sys
try:
    print(" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
    print("/                             \ ")
    print("| Hero Name Generator Program |")
    print("\_ _ _ _ _ _ _ _ _ _ _ _ _ _ _/ ")
except SyntaxWarning:
    pass
try:
    for i in range(10):
        i += 1
        print(f"{i}. Hero: {heroes.gen()}")
        time.sleep(3)
except KeyboardInterrupt:
    sys.exit()
