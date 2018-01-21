import argparse as argp
BUFFER_SIZE = 16

def print_chunk(chuck, count):
    e = " "*3*(16 -len(chuck)) + " \t"
    print("%06X" % count,end="\t")
    print(" ".join("{:02x}".format(ord(ch)) for ch in chuck), end=e)
    print(chuck.replace('\n','\\n'),end='\n')


if __name__ == "__main__":
    parser = argp.ArgumentParser(description='Dump file contents as hex')
    parser.add_argument('-f','--file', help='file name',required=True,type=str)

    args = parser.parse_args()
    line_counter = 0
    try:
        file = open(args.file, encoding="latin-1", errors='ignore')
        open = True
        print("Dumping as hex")
        while open:
            chunk = file.read(BUFFER_SIZE)
            print_chunk(chunk,line_counter)
            line_counter+=0x10
            if(len(chunk) == 0):
                open = False
    except FileNotFoundError:
        print("file not found")

