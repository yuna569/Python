# -*- coding: utf-8 -*-
"""
Created on Thu May 12 16:36:08 2022

@author: yjeon
"""

def menu():
    print("""-----------------
1. 친구 리스트 출력
2. 친구 추가
3. 친구 삭제
4. 이름 변경
5. 종료
          """)
    c = int(input("메뉴를 선택하시오: "))
    return c

friend_list = []

while True:
    n = menu()
    if n>=1 and n<=5:
        if n == 1:
            print(friend_list)
        if n == 2:
            a = input("이름을 입력하시오: ")
            friend_list.append(a)
        if n == 3:
            a = input("이름을 입력하시오: ")
            if a in friend_list :
                friend_list.remove(a)
            else: 
                print(f"{a}는(은) 리스트에 없습니다.")
                continue
        if n == 4:
            a = input("변경 전 이름을 입력하시오: ")
            if a in friend_list :
                b = input("변경 후 이름을 입력하시오: ")
                i = friend_list.index(a)
                friend_list.remove(a)
                friend_list.insert(i, b)
            else:
                print(f"{a}는(은) 리스트에 없습니다.")
                continue
        if n == 5:
            break
    else:
        print("메뉴를 똑바로 보아라")
        continue