import os
import subprocess
import sys

STACK_FLAG = 1
WRITE_FLAG = 2
TEST_FLAG = 3


def main():
    flag = check_flags()
    run(flag)

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


def diff_test():
    for x, y in zip(get_files("llvm"), get_files("llvm")):
        with open(f"../llvm/test/diff-output/{x}", 'w') as f:
            subprocess.run(["diff", "-I", "label", f"../llvm/{x}", f"../llvm/test/{y}"], stdout=f)
    if get_files("llvm/test/diff-output") == []:
        subprocess.run("rm", "-rf", "../llvm/test/")
    else:
        print(f"Differences detected in the following files..\n{', '.join(get_files('llvm/test/diff-output'))}")

def run(flag):
    mini_files = get_files("mini")
    mini_files = list(filter(lambda x: ".json" not in x, mini_files))

    for f in mini_files:
        fname = f.split(".mini")[0]
        if flag == TEST_FLAG:
            with open(f"../llvm/{fname}.ll", 'w') as f:
                subprocess.run(["python3", "Compiler.py", f"{fname}"], stdout=f)

if __name__ == "__main__":
    main()