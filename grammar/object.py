def transition_table(transition):
   #string motoro
    transition[("q39", "m")] = "q6"
    transition[("q0","m")] = "q6"
    transition[("q6","o")] = "q19"
    transition[("q19","t")] = "q20"
    transition[("q20","o")] = "q21"
    transition[("q21","r")] = "q22"
    transition[("q21","o")] = "q22"

#string konro
    transition[("q39", "k")] = "q24"
    transition[("q0", "k")] = "q24"
    transition[("q24","o")] = "q25"
    transition[("q25", "n")] = "q21"
    transition[("q21","r")] = "q22"
    transition[("q22", "o")] = "q5"

#string maggale
    transition[("q39", "m")] = "q6"
    transition[("q0", "m")] = "q6"
    transition[("q6","a")] = "q7"
    transition[("q7", "g")] = "q16"
    transition[("q16","g")] = "q17"
    transition[("q17", "a")] = "q18"
    transition[("q18", "l")] = "q4"
    transition[("q22", "e")] = "q5"

    return transition

def parse_table(parse):
    parse[('OB','ammak')] = ['error']
    parse[('OB','nakke')] = ['error']
    parse[('OB','andi')] = ['error']
    parse[('OB','mangge')] = ['error']
    parse[('OB','assassa')] = ['error']
    parse[('OB','anganre')] = ['error']
    parse[('OB','ancinik')] = ['error']
    parse[('OB','motoro')] = ['motoro']
    parse[('OB','konro')] = ['konro']
    parse[('OB','maggale')] = ['maggale']
    parse[('OB','EOS')] = ['error']

    return parse