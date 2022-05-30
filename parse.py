import grammar.subject as subject
import grammar.object as object
import grammar.verb as verb
import streamlit as st 

def analyze(sentence):
    tokens = sentence.lower().split()
    tokens.append('EOS')

    non_terminals = ['S', 'SB', 'VB', 'OB']
    terminals = [
        'nakke','ammak','mangge','andi','motoro','konro','maggale','assassa',
        'anganre','ancinik'
    ]

    parse_table = {}
    
    # Non Terminal S
    parse_table[('S', 'nakke')] = ['SB', 'VB', 'OB']
    parse_table[('S', 'ammak')] = ['SB', 'VB', 'OB']
    parse_table[('S', 'mangge')] = ['SB', 'VB', 'OB']
    parse_table[('S', 'andi')] = ['SB', 'VB', 'OB']
    parse_table[('S', 'konro')] = ['error']
    parse_table[('S', 'motoro')] = ['error']
    parse_table[('S', 'maggale')] = ['error']
    parse_table[('S', 'assassa')] = ['error']
    parse_table[('S', 'anganre')] = ['error']
    parse_table[('S', 'ancinik')] = ['error']
    parse_table[('S', 'EOS')] = ['error']

    # Non Terminal SB
    parse_table = subject.parse_table(parse_table)

    # Non Terminal VB
    parse_table = verb.parse_table(parse_table)

    # Non Terminal OB
    parse_table = object.parse_table(parse_table)

    stack = []
    stack.append('#')
    stack.append('S')

    token = 0
    symbol = tokens[token]

    while(len(stack) > 0):
        top = stack[len(stack)-1]

        st.write(f'Top    = {top}')
        st.write(f'Symbol = {symbol}')

        if top in terminals:
            if top == symbol:
                stack.pop()
                token += 1
                symbol = tokens[token]

                if symbol == 'EOS':
                    st.write('Isi Stack :', stack)
                    st.write("\n")
                    stack.pop() 
            else:
                st.write('error')
                break
        elif top in non_terminals:
            if parse_table[(top, symbol)][0] != 'error':
                stack.pop()
                push = parse_table[(top, symbol)]

                for i in range(len(push)-1, -1, -1):
                    stack.append(push[i])
            else:
               # st.write('error')
                break
        else:
            #st.write('error')
            break

        st.write(f'Isi Stack : {stack} \n')        
    
    if symbol == 'EOS' and len(stack) == 0:
        st.success(f'Input string {sentence}, diterima karena sesuai Grammar')
    else:
        st.error(f'Ups, input string {sentence}, tidak diterima karena tidak sesuai Grammar. Silakan coba lagi :nerd_face:')
