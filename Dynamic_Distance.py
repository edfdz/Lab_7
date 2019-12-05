def distance(s1, s2,v):
    p = range(len(s2) + 1)
    for i, x1 in enumerate(s1):
        d = [i + 1]
        for j, x2 in enumerate(s2):
            insert = p[j + 1] + 1
            delete = d[j] + 1
            if x1 == x2:
                subs = p[j]
            elif (x1 in vowels and x2 in v) or (x1 not in v and x2 not in v):
                subs = p[j] + 1
            else:
                subs = p[j] + 2
            d.append(min(insert, delete, subs))
        p = d
    return p[-1]



if __name__ == "__main__":
    
    vowels = ('a', 'e', 'i', 'u', 'o', 'A', 'E', 'I', 'U', 'O')
    s1 = input("First string:")   
    s2 = input("Second string:")
    print("Distance:", distance(s1, s2,vowels))
