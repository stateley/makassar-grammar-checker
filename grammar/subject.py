def transition_table(transition):
    #string nakke
    transition[("q39", "n")] = "q1"
    transition[("q0", "n")] = "q1"
    transition[("q1","a")] = "q2"
    transition[("q2", "k")] = "q3"
    transition[("q3","k")] = "q4"
    transition[("q4", "e")] = "q5"

    #string ammak
    transition[("q39", "a")] = "q10"
    transition[("q0", "a")] = "q10"
    transition[("q10","m")] = "q11"
    transition[("q11", "m")] = "q12"
    transition[("q12","a")] = "q13"
    transition[("q13", "k")] = "q5"

    #string mangge
    transition[("q39", "m")] = "q6"
    transition[("q0", "m")] = "q6"
    transition[("q6","a")] = "q7"
    transition[("q7", "n")] = "q8"
    transition[("q8","g")] = "q9"
    transition[("q9", "g")] = "q4"
    transition[("q4", "e")] = "q5"

    #string andi
    transition[("q39", "a")] = "q10"
    transition[("q0", "a")] = "q10"
    transition[("q10","n")] = "q14"
    transition[("q14", "d")] = "q15"
    transition[("q15","i")] = "q5"

    return transition

def parse_table(parse):
    parse[('SB','ammak')] = ['ammak']
    parse[('SB','nakke')] = ['nakke']
    parse[('SB','andi')] = ['andi']
    parse[('SB','mangge')] = ['mangge']
    parse[('SB','assassa')] = ['error']
    parse[('SB','anganre')] = ['error']
    parse[('SB','ancinik')] = ['error']
    parse[('SB','motoro')] = ['error']
    parse[('SB','konro')] = ['error']
    parse[('SB','maggale')] = ['error']
    parse[('SB','EOS')] = ['error']

    return parse