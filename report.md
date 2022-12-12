1. 정렬
파이썬에는 sorted 및 sort라는 정렬 함수가 기본적으로 내장되어 있다. 이 함수들은 리스트, 딕셔너리, 집합 등의 데이터 타입을 입력값으로 받고, 데이터 타입에 상관없이 항상 리스트 형태로 데이터를 정렬한 결과를 반환하는 것이 특징이다.
또한, 이 함수들은 최악의 경우에도 0(N*log N : 선형 로그형 빅-오(데이터의 수가 2배로 늘 때, 연산횟수는 2배 조금 넘게 증가하는 알고리즘))의 시간 복잡도를 보장한다는 것이 특징이다.

1_1. sorted 함수
sorted 함수는 정렬된 결과값을 입력값에 바로 반영하지 않는 것이 특징이다. 즉, sorted 함수를 활용해 입력값을 정렬한 결과를 얻을 수 있지만, 결과값을 입력값에 따로 할당하지 않는 이상 입력값은 정렬되지 않는다.

소스 코드
list = [5, 8, 1, 2, 9, 3, 7, 6]
print(“sorted data: ”, sorted(list)

출력 결과
sorted data: [1, 2, 3, 5, 6, 7, 8, 9]

1_2. sort 함수
sorted 함수와 다르게, sort 함수는 따로 입려값에 정렬 함수 결과값을 반환하지 않더라도 입력값을 정렬해 주는 함수이다.

소스 코드
list = [5, 8, 1, 2, 9, 3, 7, 6]
list.sort()
print(“sort data :”, list)

출력 결과
sort data: [1, 2, 3, 5, 6, 7, 8, 9]

위와 같이 sort 함수를 사용하면 입력값 자체가 정렬된 값으로 자동 변경된 것을 확인할 수 있다.

1_3. key 매개변수 활용한 정렬 기준 설정
sorted 및 sort 함수는 key 매개변수를 활용하여 정렬 기준을 설정할 수 있다. key 매개변수에는 하나의 함수가 입력되어야 하며 해당 함수가 정렬의 기준이 된다.

lambda 함수에는 콜론(:)을 기준으로 좌측에 입력 파라미터를, 우측에 return 할 값을 입력해 주면 된다.
ex) value = lambda(x:x**2)
	print(value(7)) # 49 출력

소스 코드
list = [('Smith', 95), ('John', 78), ('Paul', 87), ('Jack', 61), ('Ryan', 97)]
res = sorted(list, key = lambda x : x[1])
print(res)

출력 결과
[('Jack', 61), ('John', 78), ('Paul', 87), ('Smith', 95), ('Ryan', 97)]

위와 같이 리스트 내 튜플별 두 번째 데이터(숫자형 데이터)를 기준으로 리스트 내 원소가 정렬된 것을 볼 수 있다.

1_4. 내림차순 정렬
파이썬의 리스트의 정렬함수에 sort와 sorted가 있듯이, 역순 정렬에는 reverse와 reversed가 있다.
공통적으로 두 함수 모두 배열에 대한 역순정렬 기능을 제공해준다.

sort(reverse=True), sorted(reverse=True) / reverse(), reversed() 차이
reverse = True 옵션을 사용한 sort와 sorted는 오름차순 정렬 후 역순, 즉 “내림차순”으로 정렬되는 것이고, reverse()와 reversed()는 정ㄹㄹ 과정 없이 순수 배열을 반대로 뒤집는 것이다.

2. 탐색
탐색은 컴퓨터 프로그래밍에서 가장 일반적인 일이며, 탐색을 위한 수 많은 알고리즘이 존재한다.
리스트가 정렬되어있다고 할 때, 이진 탐색(Binary Search)이 선형 탐색(Linear Search)보다 효율적으로 요소를 찾을 수 있다.

2_1. 선형 탐색(Linear Search)
키(Key)라는 요소를 가지고 순차적으로 리스트의 각 요소들을 비교하는 접근법이다.
키(Key)가 찾고자 하는 요소와 일치할 때까지 수행을 진행하고, 없다면 모든 요소들을 비교하고 나서야 끝이 난다.

소스 코드
def linearsearch(list,key):
    for i in range(len(list)):
        if key == list[i]:
	    return i
    return –1

list = [1, 4, 4, 2, 5, -3, 6, 2]
i = linearsearch(list,4)
j = linearsearch(list,-4)
k = linearsearch(list, -3)
print(“i= ”,i, “j= ”,j, “k= ”,k)

출력 결과
i=1, j=-1, k=5

선형 탐색 함수는 리스트의 각 요소를 하나씩 키(key)와 비교해서 평균적으로 이 알고리즘은 탐색이 완료되기 전에 절반 이상 리스트를 탐색한다. 그로 인해 리스트 요소의 수가 커지면 커질수록 선형  탐색의 시간은 증가한다.

2_2. 이진 탐색(Binary Search)
이진 탐색은 정렬된 리스트의 중간부터 비교해나가는 접근법이다. 즉 리스트를 반으로 나눠 검색한다. 이진 탐색에는 아래와 같은 세가지 경우의 수가 있다.

- 만약 키(key)가 리스트의 중간 요소보다 작을 경우, 리스트의 중간 이전까지만 탐색한다.
- 만약 키(key)가 리스트의 중간 요소와 일치한다면(찾고자 하는 요소가 중간요소라면), 탐색은 끝이 난다.
- 만약 키(key)가 리스트의 중간 요소보다 클 경우, 리스트의 중간 이후만 탐색한다.

정렬된 데이터 집합을 검색하는 경우에는 이진 탐색을 주로 사용하는데, 순차 탐색에 비해서 엄청난 성능으로 데이터를 검색할 수 있다. 이진 탐색은 전체를 반씩 잘라내서 한쪽을 버리는 방식을 사용한다.

이진 탐색 구현
검색할 범위를 1/2씩 반복해서 분할하는 기법을 분할 정복(Divide and Conquer)라고 한다.

소스 코드
def binsearch(list, x):
    start = 0
    end = len(list) -1

    while (start <= end) :
        mid = (start + end) //2
	if list[mid] == x:
	    return mid
	elif list[mid] < x:
	    start = mid + 1
	else :
	    end = mid – 1
    return –1

2_3. 이진 탐색 예제
1. 처음에 모든 심사대는 비어있습니다. 한 심사대에서는 동시에 한 명만 심사를 할 수 있고 가장 앞에 서 있는 사람은 비어 있는 심사대로 가서 심사를 받을 수 있다.
2. 하지만 더 빨리 끝나는 심사대가 있으면 기다렸다가 그곳으로 가서 심사를 받을 수도 있다.

풀이) 1.이분 탐색의 대상(범위) = 심사하는데 걸리는 시간
     2. 심사 시 최소 시간 = 0, 심사 시 최대 시간 = 가장 오래 걸리는 심사대에서 모든 사람들이 심사를 할 경우
    3. 위 조건에 맞게 범위를 줄여나가며 탐색

소스 코드
def solution(n, times):
    start = 1
    end = max(times) * n
    answer = end
    while start <= end : 
        mid = (start + end)//2
        total = sum(map(lambda x : mid//x, times))
        if total < n : 
            start = mid + 1
        else : 
            answer = min(answer, mid)
            end = mid - 1
    return answer
