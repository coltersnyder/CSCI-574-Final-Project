CCFLAGS = 
CC = 
CPPFLAGS = 
CPP = 

CS = 
CSRun = 

JAVA = 
JAVARun = 

JS = 

PY = 

RR = 

RUST = 

ifeq ($(OS),Windows_NT)
CCFLAGS += -D WIN32
ifeq ($(PROCESSOR_ARCHITEW6432),AMD64)
CCFLAGS += -D AMD64
else
ifeq ($(PROCESSOR_ARCHITECTURE),AMD64)
CCFLAGS += -D AMD64
endif
ifeq ($(PROCESSOR_ARCHITECTURE),x86)
CCFLAGS += -D IA32
endif
endif

ifneq (,$(shell where gcc))
cc += gcc
else
ifneq (,$(shell where clang))
cc += clang
else
$(error "No C Compiler Found")
endif
endif

ifneq (,$(shell where mcs))
CS += mcs
else
$(error "No C# Compiler Found")
endif

ifneq (,$(shell where mono))
CSRun += mono
else
$(error "No Mono Found")
endif

ifneq (,$(shell where java))
JAVA += java
JAVARun += java
else
$(error "No JVM Found")
endif

ifneq (,$(shell where python))
PY += python
else
ifneq (,$(shell where python3))
PY += python3
else
$(error "No Python Interpreter Found")
endif
endif

else
UNAME_S := $(shell uname -s)
ifeq ($(UNAME_S),Linux)
CCFLAGS += -D LINUX
endif
ifeq ($(UNAME_S),Darwin)
CCFLAGS += -D OSX
endif
UNAME_P := $(shell uname -p)
ifeq ($(UNAME_P),x86_64)
CCFLAGS += -D AMD64
endif
ifneq ($(filter %86,$(UNAME_P)),)
CCFLAGS += -D IA32
endif
ifneq ($(filter arm%,$(UNAME_P)),)
CCFLAGS += -D ARM
endif

ifneq (,$(shell which g++))
CPP += g++
else
ifneq (,$(shell which clang))
CPP += clang
else
$(error "No C++ Compiler Found")
endif
endif

ifneq (,$(shell which gcc))
cc += gcc
else
ifneq (,$(shell which clang))
cc += clang
else
$(error "No C Compiler Found")
endif
endif

ifneq (,$(shell which mcs))
CS += mcs
else
$(error "No C# Compiler Found")
endif

ifneq (,$(shell which mono))
CSRun += mono
else
$(error "No Mono Found")
endif

ifneq (,$(shell which java))
JAVA += java
JAVARun += java
else
$(error "No JVM Found")
endif

ifneq (,$(shell which python))
PY += python
else
ifneq (,$(shell which python3))
PY += python3
else
$(error "No Python Interpreter Found")
endif
endif


endif