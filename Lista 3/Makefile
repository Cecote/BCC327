CXX = g++
CXXFLAGS = -Wall -std=c++11
LIBS = -lGL -lGLU -lglut

SRCS = main.cpp Cube.cpp HSV.cpp Transform.cpp Camera.cpp
OBJS = $(SRCS:.cpp=.o)
TARGET = cubo

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CXX) -o $@ $^ $(LIBS)

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $<

clean:
	rm -f *.o $(TARGET)
