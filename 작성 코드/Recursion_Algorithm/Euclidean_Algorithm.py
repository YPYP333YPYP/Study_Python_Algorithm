# 최대 공약수를 구하는 함수

def gcd(x: int, y: int) -> int:
    
    if y == 0:
        return x
    else:
        print(x,y) # 과정을 보여주는 출력문
        return gcd(y, x % y)
        

if __name__ == '__main__':
   
    print(f'두 정숫값의 최대 공약수는 {gcd(22, 8)}입니다.')

""" 해설 : 유클리드 호제법은 주어진 두 수를 하나의 직사각형으로 만든다. 
    그리고 이 직사각형에서 가장 작은 정사각형이 만들어 지도록 반복하는데
    위 사례를 봤을 때 22 x 8 의 길이를 가진 직사각형에서 8 x 8 의 정사각형
    이 2개 만들어 진다. 이때 22 % 8 인 6의 길이를 가지는 직사각형이 만들어 지는데
    이는 8 x 6 의 길이를 가진다 이 과정을 반복하면 2 x 2 직사각형이 만들어 지고
    이때 우리는 22와 8의 최대공약수가 2인것을 알 수 있다.
    프로그래밍 상에서는 x,y를 각각 한변의 길이라 칭할때 
    (1) x > y , (2) x < y 의 경우가 있다. (2)의 경우에는 자연 스럽게 x % y 는 0이 나오고
    재귀 함수에서 y == 0이 됨으로 return x를 해줘 (1) 의 경우로 만들 수 있다
    그 다음부터는 x % y 는 정사각형이 만들어지고 남은 변의 길이가 되고 x는 원래 y였던 길이가 된다
    그렇게 재귀함수를 거쳐서 최대 공약수가 나올 수 있다.
"""