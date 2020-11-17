def pattern(letter):
    patterns = {1 : "*", 2 : "* *", 3 : "* * * ", 4: "* * * * "}
    #print (patterns)
    for a in patterns[letter.uppper()]:
        print (a)
pattern("a")