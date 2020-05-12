## Purpose of study

- 동일하고 협의된 문제를 각자 풀고, 정해진 기간내 서로의 코드를 리뷰한다.
- 리뷰를 통해 자신과 달랐던 점, 좋았던 풀이에 대한 스스로 고민과 공부의 시간을 가진다. 

- 양보다는 정해진 문제를 가지고 질적 공부에 집중할 수 있도록 한다.



## Rules of study

> 스터디에 참여하는 멤버들은 아래의 규칙을 엄수한다.

1. 정해진 시간을 엄수하여 커밋한다.
2. 정해진 시간을 엄수하여 코드리뷰를 작성하도록 한다.
3. 코드의 효율성, 시간복잡도을 언급할 때 `빅오표기법`으로 표기한다.
   - 단순히 `빠르다`, `괜찮다` 라는 표현은 지양한다.

4. 문제의 선별에 대한 협의는 모두가 참여한다.



## Selection criteria

> 모든 문제는 [BOJ백준온라인저지](https://www.acmicpc.net/)의 내용을 바탕으로 한다.
>
> [Solved.ac](https://solved.ac/) 는 정답율로만 문제의 난이도를 평가하기 어려워, BOJ랭커들이 각 문제의 난이도를 매겨뒀다.
>
> [Solved.ac](https://solved.ac/) 의 선별한 문제의 난이도 :  `Bronze` < `Silver` <  `Gold ` <  `Platinum` <  `Diamond` <  `Ruby`
>
> 위 기준을 바탕으로 `Gold` 이상의 난이도를 가진 문제만 선별한다.

- Issue를 통해 매주 문제를 확인해주세요.



## Pull request Convention

> 포함되어야 할 내용

- 문제에서의 시간복잡도
- 어떤 로직이 핵심이었나?
- 또 다른 풀이가 있을까?

**문제를 모두 풀지 못하더라도 괜찮습니다. 대신 어떻게 풀어야겠다는 논리적 사고방식을 기술해주세요.**

## Language

- 언어제한은 없습니다.



## Cycle

- 한 사이클은 `7일` 을 기준으로 한다.
- `5~6일` 은 문제풀이후 PR,  `1~2일` 은 코드리뷰, 다음과제 선별에 할당하도록한다.



## File naming

> 저장소에 올라가는 파일은 아래의 형식에 맞춘다.

**예시** 

- 폴더 : 1WEEK
- 폴더 안에 담길 내용
  - 1000-leeshinyook.cpp, 1000-leeshinyook.py

## Comments

> 다른사람이 짠 코드를 한 눈에 알아보기 쉽지않다. 
>
> 반드시, 코드마다 주석을 달아주세요.

- 예

~~~c++
// 피보나치수열
#include <iostream>

#define FASTSTD ios::sync_with_stdio(0)
#define FASTCIN cin.tie(0)
using namespace std;

int main() {
    FASTSTD;
    FASTCIN;
    int dp[51]; 
    dp[0] = 1; 
    dp[1] = 1;// 1 일때,
    dp[2] = 3;// 2 일때,
    for(int i = 3; i < 51; i++) {
        dp[i] = (dp[i - 1] + dp[i - 2] + 1) % 1000000007; // 피보나치수의 점화식
    } // 메모이제이션
    int n;
    cin >> n;
    cout << dp[n];
    return 0;
} 
~~~
