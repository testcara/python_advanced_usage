def outFunc():
    num_a = 1

    def innerFunc():
        numb_b = 2
        return num_a + numb_b
    return innerFunc()


print(outFunc())
