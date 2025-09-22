import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

name = "홍길동"
if name == "홍길동":
    print("안녕하세요")
    print(name)


    