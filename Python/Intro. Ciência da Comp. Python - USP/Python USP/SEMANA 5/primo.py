def maior_primo(k):
    primos = []
    for i in range(k):
        c = 0
        for j in range(k):
            if i%(j+1) == 0: 
                c += 1
        if c == 2:
            primos.append(i)
    return(max(primos))
