import sys
import subprocess
import json

from CompilerError import CompilerError
from Program import Program
from TypeChecker import TypeChecker


def main():

    filename = sys.argv[1]
    print(filename)
    with open(f"../mini/{filename}.json", 'w') as out_file:
        subprocess.run(["java", "-jar", "../MiniCompiler.jar", f"../mini/{filename}.mini"], stdout=out_file)

    with open(f"../mini/{filename}.json", 'r') as out_file:
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

    if len(sys.argv) >= 3 and sys.argv[2] == "--stack":
        print(string)


if __name__ == "__main__":
    main()
