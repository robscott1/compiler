import sys
import subprocess
import json

from CompilerError import CompilerError
from TypeChecker import TypeChecker
from Factories.FunctionFactory import FunctionFactory as ff


def main():
    if len(sys.argv) != 2:
        print("Usage: Compiler <filename>")

    filename = sys.argv[1]
    with open(f"{filename}.json", 'w') as out_file:
        subprocess.run(["java", "-jar", "MiniCompiler.jar", filename], stdout=out_file)

    with open(f"{filename}.json", 'r') as out_file:
        json_repr = dict(json.load(out_file))

    tc = TypeChecker(json_repr)

    print(tc)


if __name__ == "__main__":
    main()
