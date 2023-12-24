#создай приложение для запоминания информации
from random import shuffle, randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class Question():
    def __init__ (self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question("вопрос",'правильный ответ','неправильный 1','неправильный 2','неправильный 3'))
app = QApplication([])
question_list.append(Question("почему спать на потолке не удобно?",'одеяло вспадает','можно упасть','монстр в шкафу останется без обеда','незнаю, мне удобно'))
question_list.append(Question("от чего люди глохнут?",'что ты сказал?','какая-то болезнь','громкий звук','люди не могут глохнуть, они заводят'))
question_list.append(Question("что будет если ворона сядет на оголённые провода?",'будет электрокар','она умрёт','будет смешно','шашлыки'))
question_list.append(Question("что это за греческая цифра (|||)",'3','4','1','2'))
question_list.append(Question("как переводится фраза i'm going to?",'я собираюсь','я иду','я ухожу','я приду'))


window = QWidget()
window.setWindowTitle('Memo card')
window.resize(400, 400)
window.total=1
window.score=0

lb_Question = QLabel('Какого цвета нет в русском флаге?')
btn_OK = QPushButton('Ответить')

rbtn_1 = QRadioButton('зелёного')
rbtn_2 = QRadioButton('красного')
rbtn_3 = QRadioButton('синего')
rbtn_4 = QRadioButton('белого')

RadioGroup = QGroupBox('ответы')

radio = QButtonGroup()
radio.addButton(rbtn_1)
radio.addButton(rbtn_2)
radio.addButton(rbtn_3)
radio.addButton(rbtn_4)

ansGroup = QGroupBox('Результат')
lb_result = QLabel('да/нет')

lb_correct = QLabel('Правильный ответ')

layout_res =QVBoxLayout()

layout_res.addWidget(lb_result, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_correct, alignment = (Qt.AlignHCenter), stretch = 2)

ansGroup.setLayout(layout_res)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroup.setLayout(layout_ans1)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))

layout_line2.addWidget(RadioGroup)
layout_line2.addWidget(ansGroup)

ansGroup.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch = 2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch = 2)
layout_card.addLayout(layout_line2, stretch = 7)
layout_card.addLayout(layout_line3, stretch = 2)

layout_card.addSpacing(5)

window.setLayout(layout_card)

def show_result():
    RadioGroup.hide()
    ansGroup.show()
    btn_OK.setText('Следуйщий вопрос')

def show_question():
    RadioGroup.show()
    ansGroup.hide()
    btn_OK.setText('Ответить')
    radio.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    radio.setExclusive(True)

def test():
    if "Ответить" == btn_OK.text():
        show_result()
    else:
        show_question()

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]



def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct("Правильно!")
        window.score+=1
        print('Статистика\n- Всего вопросов', window.total, '\n- Правильных ответов', window.score)
        print('Рейтинг:',window.score/window.total*100, "%")
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct("Неверно!")
            print('Рейтинг:',window.score/window.total*100, "%")

def next_question():
    window.total += 1
    print('Статистика\n- Всего вопросов', window.total, '\n- Правильных ответов', window.score)
    cur_question =randint(0,len(question_list)-1)
    q = question_list[cur_question]
    ask(q)
    

def click_OK():
    if btn_OK.text() == "Ответить":
        check_answer()
    else:
        next_question()

btn_OK.clicked.connect(click_OK)


window.show()
app.exec()