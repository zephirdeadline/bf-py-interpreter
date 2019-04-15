import sys
import datetime
MEMORY = [0]

def run(ptr, content):
    jump = -1
    for i, c in enumerate(content):
        if jump != -1 and i < jump:
            continue

        if c == '+':
            MEMORY[ptr[0]] += 1
        elif c == '-':
            MEMORY[ptr[0]] -= 1
        elif c == '>':
            ptr[0] += 1
            if len(MEMORY) - 1 < ptr[0]:
                MEMORY.append(0)
        elif c == '<':
            ptr[0] -= 1
        elif c == '.':
            print(chr(MEMORY[ptr[0]]), end='')
        elif c == '[':
            skiploop = 1
            end_index = i + 1
            while MEMORY[ptr[0]] > 0:
                while skiploop != 0:
                    if content[end_index] == '[':
                        skiploop += 1
                    elif content[end_index] == ']':
                        skiploop -= 1
                    end_index += 1
                run(ptr, content[i + 1: end_index - 1])
            jump = end_index - 1


def main():
    start = datetime.datetime.now()
    f = open(sys.argv[1], "r")
    content = f.read()
    print(content)
    ptr = [0]
    run(ptr, content)
    print((datetime.datetime.now() - start).microseconds, 'ns')

main()