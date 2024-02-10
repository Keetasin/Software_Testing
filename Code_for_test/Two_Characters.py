def alternate(s):
    
    c = tuple(set(s))
    if len(c) < 2:
        return 0
    max_length = 0
    for i in range(len(c) - 1):
        for j in range(i + 1, len(c)):
            test = "".join([a for a in s if a in (c[i], c[j])])
            if all(test[k] != test[k+1] for k in range(len(test) - 1)):
                max_length = max(max_length, len(test))
    return max_length

