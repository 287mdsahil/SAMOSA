from arguments import parseArgs
from initialization import init

def main():
    print("Running SAMOSA...")
    args = parseArgs()
    init(args)
