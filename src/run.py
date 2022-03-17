import os
import subprocess
import sys

STACK_FLAG = 1
WRITE_FLAG = 2
TEST_FLAG = 3


def main():
    flag = check_flags()
    run()

def get_files(dir):
    return filter(lambda x: ".json" not in x, os.listdir(f"../{dir}"))

def check_flags():
    # For when the stack flag is used with file arg
    if len(sys.argv) == 3:
        return STACK_FLAG
    elif sys.argv[1] == "--write":
        return WRITE_FLAG
    else:
        return TEST_FLAG


def run():
    mini_files = get_files("mini")
    mini_files = list(filter(lambda x: ".json" not in x, mini_files))

    for f in mini_files:
        fname = f.split(".mini")[0]
        print(f"Compiling {f}...")
        with open(f"../llvm/{fname}.ll", 'w') as f:
            subprocess.run(["python3", "Compiler.py", f"{fname}"], stdout=f)
        print(f"Converting {fname}.ll to executable...")
        subprocess.run(["clang", "-m32", f"../llvm/{fname}.ll", "-o", f"../executable/{fname}.o"])
        print("\n")

if __name__ == "__main__":
    main()