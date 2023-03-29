def game():
    progress = True
    word = ['sun']
    lifes = 5
    word_in_play = get_word(word)
    template= start_template(word_in_play)
    welcome_speech(list_to_string_convert(template))

    while progress:
        user_guess = input('Введите букву:')
        template = build_template(template,word_in_play,user_guess)
def welcome_speech(t):
    print(f'Загаданное слово состоит из {len(t)} букв{t}')

def build_template(t,w,g=''):
    for i in range(len(w)):
        if w[i] == '_':
            if w[i] == g:
                t[i] = w[i]
            else:
                t[i] = '_'



def start_template(w):
    t = []
    for _ in w:
        t.append('_')
    return t 
def list_to_string_convert(t):
    s = ''
    return s.join(t)
def get_word(w):
    return w[0]

game()
