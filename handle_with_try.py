try:
    number_input_a = int(input("점수 입력>"))
    print("원의 반지름:",number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)
except:
    print("무엇가 잘못되었습니다.")