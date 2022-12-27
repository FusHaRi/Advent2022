
def getContents(input_file: str):
    rucks = []
    with open(input_file) as contents:
        for line in contents:
            rucks.append(line.strip)

    return rucks


def main():
    rucks = getContents('ruck_contents.txt')
