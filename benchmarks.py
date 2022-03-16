import os
import subprocess


def main():
    # TODO: run through each directory, compile it
    benchmarks_dir = os.listdir("benchmarks")
    for working_dir in benchmarks_dir:
        subprocess.run(["cd", f"~/431/compiler/benchmarks/{working_dir}"])
        print(f"{working_dir}...")
        with open(f"{working_dir}.ll", 'w') as f:
            subprocess.run(["python3", "../src/Compiler.py", f"{working_dir}", "--stack"], stdout=f)
        print(f"Successfully compiled. Running..")

        #TODO: with each binary, run it with the sample input within the same dir
        subprocess.run(["clang", "-m32", f"{working_dir}.ll", "-o", f"{working_dir}.o"])
        with open("input", "r") as f:
            subprocess.run([f"./{working_dir}.o"], stdin=f)
        print(f"Successfully executed {working_dir}.o. Diff testing...")


    # TODO: python launch a bash script that does the diff






if __name__ == "__main__":
    main()