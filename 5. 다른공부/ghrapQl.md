###### 그래프 QL

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
      -
      ~~~
          {
          cust{
              CUST_NO
            }
          }
      ~~~

###### GQL vs REST
  1. REST
      - Representational State TransFer
      - 자원의 이름을 구분하여 해당 자원의 상태를 주고 받는 것
      - HTTP URL을 통해 자원을 명시,
      - HTTP Method(post, get, put, delete)를 통하여 자원에 대한 CRUD Operation을 적용하는 것을 말한다.
        - 장점
            1. Http 프로토콜의 인프라를 그대로 사용하기 때문에 별도의 인프라를 구축할 필요가 없다.
            2.
