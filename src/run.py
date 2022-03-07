import os
import subprocess
import sys

STACK_FLAG = 1
WRITE_FLAG = 2
TEST_FLAG = 3


def main():

    # mini_files = os.listdir("./mini")
    # mini_files = list(filter(lambda x: ".json" not in x, mini_files))
    # flag = check_flags()
    run()



def check_flags():
    # For when the stack flag is used with file arg
    if len(sys.argv) == 3:
        return STACK_FLAG
    elif sys.argv[2] == "--write":
        return WRITE_FLAG
    else:
        return TEST_FLAG




def run():
    mini_files = os.listdir("../mini")
    mini_files = list(filter(lambda x: ".json" not in x, mini_files))

    for f in mini_files:
        fname = f.split(".mini")[0]
        subprocess.run(
            ["python3", "Compiler.py", f"{fname}"]
        )
        print("\n")


if __name__ == "__main__":
    main()