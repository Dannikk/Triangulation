# Triangulation

This is my student project. In this work, the polygon triangulation algorithm is implemented using the ear cutting method.
Due to the use of a doubly connected list of vertices and the assumption that after cutting off the ear, an ear may appear on the neighboring vertex, the time complexity of this algorithm is O(n^2).

## Install dependencies

It's require to install third-party dependencies.
For this write in the python console.

```
pip install -r requirements
```

## Input and output data format

Provided that __N__ is the number of vertices of the polygon.
- Input:
The file contains __N__ lines of the vertices of the triangle in the sequential order of traversing the vertices. Each line contains two space-separated numbers corresponding to the **x** and **y** coordinates of the vertex, respectively.
- Output:
There are __N-2__ lines in the file. Each line corresponds to a triangulation triangle and contains 6 numbers separated by spaces or 3 consecutive pairs of numbers. Each pair of numbers corresponds to the **x** and **y** coordinates of the vertex, respectively.
For example:
We get a square at the input
input.txt:
```
0 0
0 1
1 1
1 0
```

Return two triangles formed by the diagonal of a square
output.txt:
```
0 0 0 1 1 1
0 0 1 1 1 0
```

## Example of using the program:

by running in the console:
```
python main.py my_input.txt my_output.txt -show
```
