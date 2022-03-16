import sys
import subprocess
import json

from CompilerError import CompilerError
from Program import Program
from TypeChecker import TypeChecker


def main():

    filename = sys.argv[1]
    with open(f"benchmarks/{filename}/{filename}.json", 'w') as out_file:
        subprocess.run(["java", "-jar", "../MiniCompiler.jar", f"benchmarks/{filename}/{filename}.mini"], stdout=out_file)

    with open(f"benchmarks/{filename}/{filename}.json", 'r') as out_file:
        json_repr = dict(json.load(out_file))

    tc = TypeChecker(json_repr)
    try:
        tc.analyze()
        for function in tc.fn_map.values():
            function.create_cfg()
            function.cfg.valid_control_flow()
    except CompilerError as e:
        print(e.__repr__())

    program = Program(tc)
    string = program.print_program()

    with open(f"../llvm/{filename}.ll", 'w') as w:
        w.write(string)

    if len(sys.argv) == 3:
        print(string)


if __name__ == "__main__":
    main()
