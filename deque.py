# Deque 구현
a = []
while True:
    n = input("입력: ")
    # 앞에 추가
    if n == '11': 
        a.insert(0,input())
    
    # 뒤에 추가
    elif n == '91':
        a.append(input())
    
    # 앞에 삭제
    elif n == '19':
        a.pop(0)
    
    # 뒤에 삭제
    elif n == '99':
        a.pop()
    
    # 리스트 길이 반환
    elif n == 'length':
        print(len(a))
    
    # 전체 리스트 요소 출력
    elif n == 'all':
        print(a)
    
    # 리스트에 해당 요소가 있는지
    elif n == 'is':
        print(input() in a)
