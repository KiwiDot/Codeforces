# 백준 785A Anton and Polyhedrons
import sys
put = sys.stdin.readline

n = int(put())
poly = {"Tetrahedron": 4,
        "Cube": 6,
        "Octahedron": 8,
        "Dodecahedron": 12,
        "Icosahedron": 20}

print(sum(poly[put().strip()] for i in range(n)))