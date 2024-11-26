def createComa(file):
    f = open(file, "r")
    arraySet = f.read().replace("\n", ",").replace(" ", ",").replace(",,",",").replace("[,","[")

    print(arraySet)

    f.close

    f = open(file, "w")
    f.write(arraySet)
    f.close

createComa("w1.txt")
createComa("w2.txt")
createComa("b1.txt")
createComa("b2.txt")