import sys
import subprocess
import json


def main():
    if len(sys.argv) != 2:
        print("Usage: Compiler <filename>")
    
    filename = sys.argv[1]
    with open(f"{filename}.json", 'w') as out_file:
        subprocess.run(["java", "-jar", "MiniCompiler.jar", filename], stdout=out_file)


    with open(f"{filename}.json", 'r') as out_file:
        json_repr = dict(json.load(out_file))

    print(json_repr.keys())

    

    
if __name__ == "__main__":
    main()