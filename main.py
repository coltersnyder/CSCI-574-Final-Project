import os

if __name__ == "__main__":
    print(os.getcwd())
    rNum = ''
    with open('randoms/Rnumbers.txt', 'r') as f:
        rNum = f.read()
    rNum = int(rNum)
    rNum = str(bin(rNum))
    print(rNum[2:100])