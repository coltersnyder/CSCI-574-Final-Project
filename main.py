import os

if __name__ == "__main__":
    cNum = ''
    with open('randoms/CNumbers.txt', 'r') as f:
        cNum = f.read()
    cNum = int(cNum, 16)
    cNum = str(bin(cNum))
    print("C Numbers:", cNum[2:103])

    cppNum = ''
    with open('randoms/C++Numbers.txt', 'r') as f:
        cppNum = f.read()
    cppNum = int(cppNum, 16)
    cppNum = str(bin(cppNum))
    print("C++ Numbers:", cppNum[2:103])
    
    csNum = ''
    with open('randoms/c_sharp_random.txt', 'r') as f:
        csNum = f.read()
    csNum = int(csNum)
    csNum = str(bin(csNum))
    print("C# Numbers:", csNum[2:103])

    javaNum = ''
    with open('randoms/JavaNumbers', 'r') as f:
        javaNum = f.read()
    javaNum = int(javaNum)
    javaNum = str(bin(javaNum))
    print("Java Numbers:", javaNum[2:103])
    
    jsNum = ''
    with open('randoms/JavaScriptNumbers', 'r') as f:
        jsNum = f.read()
    jsNum = int(jsNum)
    jsNum = str(bin(jsNum))
    print("JavaScript Numbers:", jsNum[2:103])

    pyNum = ''
    with open('randoms/PythonNumbers.txt', 'r') as f:
        pyNum = f.read()
    pyNum = int(pyNum, 16)
    pyNum = str(bin(pyNum))
    print("Python Numbers:", pyNum[2:103])

    rNum = ''
    with open('randoms/Rnumbers.txt', 'r') as f:
        rNum = f.read()
    rNum = int(rNum)
    rNum = str(bin(rNum))
    print("R Numbers:", rNum[2:103])

    rustNum = ''
    with open('randoms/RustNumbers', 'r') as f:
        rustNum = f.read()
    rustNum = int(rustNum)
    rustNum = str(bin(rustNum))
    print("Rust Numbers:", rustNum[2:103])

    