from flask import Flask, render_template, request
import random

app = Flask('mbti')

questions = {"ei1": [{"e1": "사람들과 교제한 후에는 에너지가 충전된다."},
                     {'i1': "사람들과 교제한 후에는 혼자 재충전할 시간이 필요하다."}],
             "ei2": [{"i2": "외부 자극이 달갑지 않고 나의 관심사에 집중한다."},
                     {"e2": "외부 자극을 흔쾌히 받아들이며 내 주변에서 일어나는 일에 관심이 많다."}],
             "ei3": [{"e3": "타인 지향적이며 외부 세계를 탐색한다."},
                     {"i3": "개인 지향적이며 내면세계를 탐색한다."}],
             "ei4": [{"i4": "주로 대화를 듣는 편이다."},
                     {"e4": "주로 대화를 주도하는 편이다."}],
             "ei5": [{"e5": "다른 사람과 교제할 때 생기가 돈다."},
                     {"i5": "혼자만의 시간을 가질 때 생기가 돈다."}],
             "sn1": [{"s1": "나는 감각적으로 느낄 수 있는 정보를 받아들이며 세부 특징에 주목한다. (ex. '사과'란 단어를 보면 빛깔, 맛, 향기, 촉감 등을 떠올린다.)"},
                     {"n1": "나는 세부 특징보다는 함축적 의미 또는 관련성에 주목한다. (ex. '사과'란 단어를 보면 관련된 이야기나 의미, 기억 등을 떠올린다.)"}],
             "sn2": [{"n2": "본능적인 직관을 신뢰하며 상상과 공상을 즐긴다."},
                     {"s2": "직접 경험한 것을 신뢰하며 현실적이다."}],
             "sn3": [{"s3": "범죄율을 낮추기 위해서는 경찰력의 보강, 엄중한 판결, 교도소의 확충이 필요하다."},
                     {"n3": "범죄율을 낮추기 위해서는 불우한 청소년을 위한 사회교육 프로그램이 필요하다."}],
             "sn4": [{"n4": "새로운 시스템으로 접근하거나 창조적으로 도전하는 것이 좋다."},
                     {"s4": "기존의 시스템을 유지하고 반복적인 절차를 따르는 것이 좋다."}],
             "sn5": [{"s5": "공학, 과학, 경영학 등 ‘확실한 실체가 있는 응용 과목’에 흥미를 보인다."},
                     {"n5": "인문학, 심리학, 사회학 등 ‘이론적인 과목’에 흥미를 느낀다."}],
             "tf1": [{"t1": "언성을 높인 격렬한 논쟁 직후에도 상대와 식사를 함께 할 수 있다. 논쟁은 논쟁일 뿐 마음에 담아두지 않는다."},
                     {"f1": "언성을 높인 격렬한 논쟁 직후에 상대와 식사를 함께 할 수 없다. 고통스러웠기에 식사를 함께할 기분이 아니다."}],
             "tf2": [{"f2": "개인적인 느낌과 정서에 따라 의사결정을 내린다."},
                     {"t2": "개인적 주관은 배제하고 객관적으로 의사결정을 내린다."}],
             "tf3": [{"t3": "상대방의 기분이 나쁠 것 같더라도 정직하게 말한다."},
                     {"f3": "선의의 거짓말을 해서라도 상대의 기분을 상하게 하지 않는다."}],
             "tf4": [{"f4": "나는 감정적인 호소에 설득된다."},
                     {"t4": "나는 논리 정연한 주장에 설득된다."}],
             "tf5": [{"t5": "나는 공명정대하고 분명하게 행동한다."},
                     {"f5": "나는 이타적이고 다정하게 행동한다."}],
             "jp1": [{"j1": "결정된 것이 없으면 불안하다. 신속하게 결정을 내려야 마음이 편하다."},
                     {"p1": "결정을 하는 것 자체가 부담스럽다. 결정을 미루는 것이 마음 편하다."}],
             "jp2": [{"p2": "입장을 명확히 하기보다는 우유부단한 편이다. 상황을 지배하려는 욕구가 적다."},
                     {"j2": "사소한 일부터 중요한 일까지 내 입장을 분명히 밝혀 상황을 지배하려 한다."}],
             "jp3": [{"j3": "먼저 계획을 세운 다음 그에 따라 일 처리를 한다."},
                     {"p3": "미리 계획을 세우지 않고 직면한 상황에 따라 일 처리를 한다."}],
             "jp4": [{"p4": "물건들을 바로바로 치우지 않는다. 부엌, 침실, 서재 등이 어수선하다."},
                     {"j4": "물건들을 바로바로 치운다. 생활 공간이 질서정연하다."}],
             "jp5": [{"j5": "나는 늘 계획된 일을 먼저 끝낸 후에 쉰다."},
                     {"p5": "나는 흥미로운 것이 있다면 일을 미룬다. 일은 나중에라도 처리할 수 있다."}]}

# examples = ['ei1', 'ei2', 'ei3', 'ei4', 'ei5']
ki = questions.keys()
ki = list(ki)


@app.route('/')
def home():
    # order = ki
    return render_template('index.html', **locals())


@app.route("/question")
def question():
    random.shuffle(ki)

    id = []
    content = []
    name = []
    for i in range(len(ki)):
        question = questions[ki[i]]
        # print(question)
        for i in range(len(question)):
            for key, value in question[i].items():
                id.append(key)
                content.append(value)
                if i == 0:
                    continue
                # print(id, i-1, i)
                name.append(id[-2]+id[-1])

    return render_template('question.html', **locals())


@app.route('/result')
def result():
    answers = list(request.args.values())
    for idx, answer in enumerate(answers):
        answers[idx] = answer[0]

    e = answers.count('e')
    i = answers.count('i')
    s = answers.count('s')
    n = answers.count('n')
    t = answers.count('t')
    f = answers.count('f')
    j = answers.count('j')
    p = answers.count('p')

    if e > i:
        energy = 'E'
    else:
        energy = "I"

    if s > n:
        information = 'S'
    else:
        information = "N"

    if t > f:
        decision = 'T'
    else:
        decision = "F"

    if j > p:
        lifestyle = 'J'
    else:
        lifestyle = "P"
    # print(answers)
    # answers = request.args
    # features=[]
    # for value in answers.values():
    #     feature = value[0]
    #     features.append(feature)
    return render_template('result.html', **locals())
    # features


# @app.route('/<question>')
# def xmpl(question):

#     idx = questions.index(question)
#     if questions.index(question) < len(questions)-1:
#         next = questions[idx+1]
#     else:
#         next = None
#     print(request.args.keys())
#     return render_template(f'{example}.html', **locals())


app.run()
