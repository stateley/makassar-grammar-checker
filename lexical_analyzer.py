from collections import defaultdict
import grammar.subject as subject
import grammar.object as object
import grammar.verb as verb
import streamlit as st 

def analyze(input_string):
    input_string = input_string.lower() + "#"

    # Inisialisasi State 
    state_list = []; list(state_list.append(f'q{i}') for i in range(39))

    # Inisilisasi Nili Awal
    transition_table = defaultdict(lambda: "ERROR", {})

    # Initial State (q0)
    transition_table[("q0", " ")] = "q0"

    # Final state
    transition_table[("q5", "#")] = "ACCEPT"
    transition_table[("q5", " ")] = "q39"

    transition_table[("q39", "#")] = "ACCEPT"
    transition_table[("q39", " ")] = "q39"
    
    # Pemanggilan Transition Tabel Untuk Masing-Masing Grammar
    transition_table = subject.transition_table(transition_table)
    transition_table = object.transition_table(transition_table)
    transition_table = verb.transition_table(transition_table)

    # Lexical Analysis Process
    idx_char = 0 #inisialisasi idx_char (pemrosesan dimulai dari karakter paling kiri)
    state = "q0"
    current_token = "" 

    while state != "ACCEPT":
        current_char = input_string[idx_char]
        current_token += current_char
        state = transition_table[(state, current_char)]
        if state == "q5": #untuk melakukan pengecekan per token
            st.write("Current token: {} is valid".format(current_token),u'\u2705')
            current_token = ""
        if state == "ERROR":
            print("error")
            break
        idx_char += 1 #proses untuk karakter selanjutnya

    return state == "ACCEPT"
