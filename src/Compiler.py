import sys
import subprocess
import json

def main():
    if len(sys.argv) != 2:
        print("Usage: Engine <filename>")
    
    filename = sys.argv[1]
    with open(f"{filename}.json", 'w') as out_file:
        subprocess.run(["java", "-jar", "../given_parser/MiniCompiler.jar", filename], stdout=out_file)


    with open(f"{filename}.json", 'r') as out_file:
        json_repr = dict(json.load(out_file))

    print(json_repr.keys())
    print("-----------------------------------")
    print(json_repr.get("types"))

    

    
if __name__ == "__main__":
    main()