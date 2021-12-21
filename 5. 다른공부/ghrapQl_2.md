###### 그래프 QL Study

---

###### Operation Name?
  - 이 전 학습까지는 query를 만들 떄 키워드와 쿼리 이름을 생략하는 축약형 구문으로 만들어왔다.
  - 그렇지만 해당 축약형 코드는 모호하게 될 수 있기 때문에 프로덕션 앱에서는 덜 모호하게 만드는 것이 중요하다.
  - Operation Name 작업은 다중 작업 문서에서만 필요하지만 디버깅 및 서버 측 로깅에 매우 유용하므로 사용을 권장합니다.

  ~~~
    [Query]  
    query sgmoominAndTistory {
      tistory {
        name
        moomin {
          name
        }
      }
    }
  ~~~


  ~~~
    [Result]
    {
      "data" : {
        "tistory" : {
          "name" : "R2-D2",
          "moomin" : [
          {
            "name": "romin_pic"
          }
          {
            "name": "rooney"
          }
          ]
        }
      }
    }
  ~~~  

  - 위와 같이 사용하는 경우에 내용 해독에는 어려울 수 있으나 코드베이스에서 쿼리를 식별하는 것이 더 쉽고 이는 프래그먼트 이름과 함께 서버 측에서 다양한 GraphQL 요청을 식별하는데 유용한 디버깅 도구가 될 수 있습니다.


###### Variables?
  - 쿼리 문자열에서 모든 인수를 작성했지만 실제로는 동적 프로그래밍으로 구성해야 합니다.
  - 그 이유는 GraphQl에는 전용형식으로 직렬화 해야 하기 때문입니다.
  - GraphQl에는 쿼리에서 동적 값을 인수분해하여 별도의 사전으로 전달하는 방법이 있는데 해당 값을 Variables라고 합니다.

  ~~~
    [Query]  
    query sgmoominAndTistory($episode: Episode) {
      tistory(episode: $episode) {
        name
        moomin {
          name
        }
      }
    }

    [Variables]
    {
      "episode": "sg-mo"
    }
  ~~~


  ~~~
    [Result]
    {
      "data" : {
        "tistory" : {
          "name" : "R2-D2",
          "moomin" : [
          {
            "name": "romin_pic"
          }
          {
            "name": "rooney"
          }
          ]
        }
      }
    }
  ~~~  

  - 위와 같이 만든다면 쿼리의 인수가 동적으로 표현이 가능하고 다른 변수도 전달이 가능합니다.



###### 
-------------

###### 참고자료

  - https://graphql.org/
  - https://tech.kakao.com/2019/08/01/graphql-basic/
