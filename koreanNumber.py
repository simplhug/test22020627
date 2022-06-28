def korean_number(num):
    d = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: '오', 6: '육', 7: '칠', 8: '팔', 9: '구'}
    return d[num]

if __name__ == '__main__':
    a = input()
    print(korean_number(int(a)))
