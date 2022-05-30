def transition_table(transition):
    #string assassa
    transition[("q39", "a")] = "q10"
    transition[("q0", "a")] = "q10"
    transition[("q10","s")] = "q28"
    transition[("q28", "s")] = "q29"
    transition[("q29","a")] = "q30"
    transition[("q30", "s")] = "q31"
    transition[("q31", "s")] = "q32"
    transition[("q32", "a")] = "q5"

    #string anganre
    transition[("q39", "a")] = "q10"
    transition[("q0","a")] = "q10"
    transition[("q10","n")] = "q14"
    transition[("q14","g")] = "q36"
    transition[("q36","a")] = "q37"
    transition[("q37","n")] = "q38"
    transition[("q38","r")] = "q4"
    transition[("q4","e")] = "q5"

    #string ancinik
    transition[("q39", "a")] = "q10"
    transition[("q0","a")] = "q10"
    transition[("q10","n")] = "q14"
    transition[("q14","c")] = "q33"
    transition[("q33","i")] = "q34"
    transition[("q34","n")] = "q35"
    transition[("q35","i")] = "q13"
    transition[("q13","k")] = "q5"

    return transition

def parse_table(parse):
    parse[('VB','ammak')] = ['error']
    parse[('VB','nakke')] = ['error']
    parse[('VB','andi')] = ['error']
    parse[('VB','mangge')] = ['error']
    parse[('VB','assassa')] = ['assassa']
    parse[('VB','anganre')] = ['anganre']
    parse[('VB','ancinik')] = ['ancinik']
    parse[('VB','motoro')] = ['error']
    parse[('VB','konro')] = ['error']
    parse[('VB','maggale')] = ['error']
    parse[('VB','EOS')] = ['error']

    return parse