import sys 
import random  

# range(10), 返回的是一个range对象，表示一个整数序列，从0到9


chars = '\|/'

def draw(rows, columns):
    for _ in range(rows):
        print(''.join(random.choice(chars) for _ in range(columns)))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit("Usage: art.py rows columns")
    draw(int(sys.argv[1]), int(sys.argv[2]))