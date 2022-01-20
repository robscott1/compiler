import sys
import subprocess
import json

from TypeChecker import TypeChecker
from TypeFactory import TypeFactory as tf


def main():
    if len(sys.argv) != 2:
        print("Usage: Compiler <filename>")
    
    filename = sys.argv[1]
    with open(f"{filename}.json", 'w') as out_file:
        subprocess.run(["java", "-jar", "MiniCompiler.jar", filename], stdout=out_file)

    with open(f"{filename}.json", 'r') as out_file:
        json_repr = dict(json.load(out_file))

    type_checker = TypeChecker()
    print(type_checker.build_type_map(json_repr))
    print(type_checker.build_global_map(json_repr))
    print(json_repr.get("functions"))


if __name__ == "__main__":
    main()