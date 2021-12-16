###### 그래프 QL Study

---

###### GraphQL?
  - GraphQL은 페이스북에서 만든 쿼리 언어
  - 아직 GraphQl API를 Open API로 공개하지는 않았으나 인기가 높은 편이다.
  ![Gitlab](https://cdn.discordapp.com/attachments/911905192407101463/920306566731800606/unknown.png)


###### GraphQL?
  - (SQL)Stucted Query Language와 마찬가지로 쿼리 언어이다.
  - SQL과 GQL의 언어적 구조 차이가 존재한다.
  - SQL은 DB 시스템에서 데이터를 가져오는 목적이라면 GQL은 웹 클라이언트가 데이터를 서버로 부터 가져오는 것에 목적을 가진다.
  - 문장은 SQL은 백앤드 시스템에서 작성해서 호출한다면 GQL은 클라이언트 시스템에서 작성하여 호출한다.
  - GQL

###### GQL vs SQL
  1. SQL
      - SELECT CUST_NO FROM CUST_MST_TB;

  2. GQL

      ~~~
          {
          cust{
              CUST_NO
            }
          }
      ~~~

###### REST
  1. REST
      - Representational State TransFer
      - 자원의 이름을 구분하여 해당 자원의 상태를 주고 받는 것
      - HTTP URL을 통해 자원을 명시,
      - HTTP Method(post, get, put, delete)를 통하여 자원에 대한 CRUD Operation을 적용하는 것을 말한다.
        - 장점
            1. Http 프로토콜의 인프라를 그대로 사용하기 때문에 별도의 인프라를 구축할 필요가 없다.
            2. Http 표준 프로토콜에 따르는 모든 플랫폼에서 사용이 가능
            3. 서버와 클라이언트의 역할을 분리

        - 단점
            1. 사용가능한 메소드가 4개이다.
            2. 표준이 존재하지 않음


   2. REST API
        - REST 기반으로 서비스를 구현  
        - HTTP 표준을 기반으로 구현하기 때문에 HTTP 지원하는 프로그램 언어로 클라이언트, 서버를 구현 가능하다.


###### GraphQl 구조
  - 쿼리
    ~~~
      {
        cust{
          name
        }
      }
    ~~~

  - 응답 데이터
      ~~~
        "data" : {
          "cust" : {
            "name" : "sg-moomin"
          }
        }
      ~~~
   - 느낌표를 이용하면 필수 값을 표현한다.



###### 오퍼레이션 네임 쿼리
  - DB에서 프로시저 개념과 유사
  - 오퍼레이션 네임 쿼리를 이용하면 한번에 인터넷 네트워크 왕복으로 모든 데이터를 가져올 수 있다.

###### 리졸버(resolver)
  - GQL에서는 데이터를 가져오는 구체적인 과정을 직접 구현해야 한다.
  - GQL에서 데이터를 가져오는 구체적인 과정을 resolver가 담당한다.
  - GQL쿼리에는 각각의 필드마다 함수가 하나씩 존재하는데 해당 함수들을 리졸버라고 한다.
  ~~~
  ex) async (parent, args, context, info) => {
  }
  ~~~
  - parent : 부모 리졸버가 리턴한 객체
  - args : 쿼리에서 입력으로 넣은 인자
  - context : 모든 리졸버에게 전달되며 주로 미들웨어를 통해 입력된 값이 들어 있음
  - info : 스키마 정보와 더불어 현재 쿼리의 특정 필드 정보를 가짐

###### 인트로스펙션(resolver)
  - 기존 방식(서버-클라이언트)  
      - API 명세서를 주고 받는 절차가 필요함(현재 회사 업무와 동일)
      - API 명세서 업데이트가 잘 안되는 오차 및 전달하는 타이밍이 오류 발생하는 경우가 다수임
      - REST 방식의 API 명세서 공유 문제를 해결한 것이 GQl의 인트로스펙션 기능
      - ##### 서버 자체에서 스키마로 실시간으로 정보를 공유할 수 있도록 함
      - ##### 이는 스키마 정보만 알면 연동 규격서가 필요 없어짐
      - ##### 인트로스펙션 쿼리가 따로 존재하지만 GQL 라이브러리에 쿼리용 IDE를 제공함

###### 별칭(Aliases)
  - 별칭을 사용하는 경우가 있는데 별칭을 사용하는 경우 필드의 결과의 이름을 원하는 이름으로 바꿀 수 있다.
  ![Gitlab](https://cdn.discordapp.com/attachments/911905192407101463/921043324259934298/unknown.png)
  - hero 필드는 충돌이 났지만 별칭(empireHero, jediHero)을 지정할 수 있다.


###### Fragments
  - GQL을 호출해올 경우 쿼리의 속도는 천차 만별인데 이 때 필드를 한번 이상 반복해야 하는 경우가 생긴다.
  - 이 때 Fragments를 이용하여 재사용 가능한 단위를 묶으주면 된다.
  ~~~~
    {
      "data": {
        "leftHome": {
          "name": "퇴사",
          "appearsIn": [
            "집",
            "야근",
            "sgMoomin"
          ],
          "friends": [
            {
              "name": "가나 초콜릿"
            },
            {
              "name": "초콜릿 존맛탱"
            },
            {
              "name": "쉬림프 파스타"
            },
            {
              "name": "떡볶이 존맛탱구"
            }
          ]
        },
        "rightHome": {
          "name": "취직",
          "appearsIn": [
            "회사",
            "정시출근",
            "rominPic"
          ],
          "friends": [
            {
              "name": "코딩업무"
            },
            {
              "name": "데이터 보정"
            },
            {
              "name": "할렐루야"
            }
          ]
        }
      }
    }

  ~~~~

  - 위의 필드를 보면 내용이 반복되는 것을 볼 수 있는데 아래와 같이 함축할 수 있다.

  ~~~
  {
    leftHome: hero(episode: sgMoomin) {
      ...comparisonFields
    }
    rightHome: hero(episode: rominPic) {
      ...comparisonFields
    }
  }

  fragment comparisonFields on Character {
    name
    appearsIn
    friends {
      name
    }
  ~~~

  - 즉 프래그먼트의 개념은 복잡한 애플리케이션 데이터 요구사항을 더 작게 분할하기 위해 자주 사용합니다.

-------------

###### 참고자료

  - https://graphql.org/
  - https://tech.kakao.com/2019/08/01/graphql-basic/
