def quiz_d():
    quiz_data = [
    {
        'question': 'Что такое Python?',
        'options': ['Язык программирования', 'Тип данных', 'Музыкальный инструмент', 'Змея на английском'],
        'correct_option': 0
    },
    {
        'question': 'Какой тип данных используется для хранения целых чисел?',
        'options': ['int', 'float', 'str', 'natural'],
        'correct_option': 0
    },
     {
        'question': 'Что создал Алан Тьюринг',
        'options': ['Машину Тьюринга', 'Энигму', 'Первый компьютер', 'IBM'],
        'correct_option': 0
    },
     {
        'question': 'Что из перечисленного не является Linux или Unix системой',
        'options': ['Centos', 'macOS', 'RISC iX', 'Android', 'TOS'],
        'correct_option': 4
    },
     {
        'question': 'Что из перечисленного не является системой контейнеризации',
        'options': ['dBrain', 'Kubernetes', 'ThinAPP', 'Docker'],
        'correct_option': 2
    },
     {
        'question': 'Что означает p?',
        'options': ['давление в физике', 'буква в кирилице', 'фосфор', 'вектор электрической поляризации'],
        'correct_option': 0
    },
     {
        'question': 'Кто не предавал?',
        'options': ['Фулгрим', 'Магнус', 'Ульфрик', 'Конрад Кёрз'],
        'correct_option': 1
    },
     {
        'question': 'За название какой страны можно получить бан на Твиче',
        'options': ['Нигерия', 'Черногория', 'Нигер', 'Тайвань'],
        'correct_option': 2
    },
     {
        'question': 'Самая маленькая страна по площади в мире?',
        'options': ['Ватикан', 'Люксембург', 'Сан-марино', 'Монако'],
        'correct_option': 0
    },
     {
        'question': 'У каких стран самая длинная неприрывная сухопутная граница?',
        'options': ['США и Канада', 'Франция и Великобритания', 'Япония и Австралия', 'Россия и Казахстан'],
        'correct_option': 3
    },

]
    result=quiz_data
    if result is not None:
        return result
    else:
        return 0


