#.Q. 리스트 L과 그 안에서 찾으려 하는 원소 x가 인자로 주어질 때, x와 같은 값을 가지는 원소의 인덱스를 리턴하는 함수 solution()을 완성하세요. 만약 리스트 L 안에 x와 같은 값을 가지는 원소가 존재하지 않는 경우에는 -1을 리턴합니다. 리스트 L은 자연수 원소들로 이루어져 있으며, 크기 순으로 정렬되어 있다고 가정합니다. 또한, 동일한 원소는 두번 이상 나타나지 않습니다.

# 풀이 : 1. 리스트 L은 자연수로 이루어져 있으며, 크기 순으로 정렬되어있다. -> 이진 탐색(Binary Search)을 이용한다.
        # 이진 탐색을 이용하여 중간값을 지정하고 x의 인자의 크기를 비교하여 원하는 값을 찾아낼 수 있게 한다.

def solution(L, x):
    start = 0
    end = len(L) -1

    while start <= end:
        middle = (start+end) //2
        if L[middle] == x:
            return middle
        elif L[middle] > x:
            end = middle -1
        else:
            start = middle +1
    return -1

if __name__ == "__main__":
    print(solution(L = [2, 3, 5, 6, 9, 11, 15],x=17))
