import sys
import subprocess
import json

from TypeFactory import TypeFactory as tf


def main():
    if len(sys.argv) != 2:
        print("Usage: Compiler <filename>")
    
    filename = sys.argv[1]
    with open(f"{filename}.json", 'w') as out_file:
        subprocess.run(["java", "-jar", "MiniCompiler.jar", filename], stdout=out_file)


    with open(f"{filename}.json", 'r') as out_file:
        json_repr = dict(json.load(out_file))

    types = json_repr.get("types")
    types = list(map(lambda x: tf.generate(x), types))
    print(types)

    

    
if __name__ == "__main__":
    main()