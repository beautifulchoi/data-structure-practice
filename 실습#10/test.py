mygraph = { "A" : set([1,2]),
            "B" : set(["A", "D"]),
            "C" : set(["A", "D", "E"]),
            "D" : set(["B", "C", "F"]),
            "E" : set(["C", "G", "H"]),
            "F" : set(["D"]),
            "G" : set(["E", "H"]),
            "H" : set(["E", "G"])
          }
for i in mygraph['A']:
    i+=1
    mygraph.update(A=i)
print(mygraph)
