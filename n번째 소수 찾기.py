## n번째 소수 찾기

a = int(input("n 번째의 소수를 출력하기 위한 정수 :"))
n = 1 # 번째부터
b = 2 # 부터

while True:

    for i in range (2, b): # b가 소수인지 체크함
        # b가 소수가 아닌 경우 n을 늘리지 않고 비교를 끝냄
        if b % i == 0:
            break

        # for문의 끝까지 온 경우=>b가 소수인 경우이므로 n을 1 늘림
        if i+1 == b:
            n += 1

    # n 번째 소수까지 찾은 경우 출력하고 끝냄
    if n == a:
        print("%d 번째 소수: %d" % (n, b))
        break

    # n번째 소수를 찾지 못한경우 b를 1씩 늘리고 반복    
    b += 1
