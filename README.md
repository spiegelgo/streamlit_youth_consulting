# streamlit_youth_consulting

## 기획의도
**지역별 청소년 고민 상담 유형 통계** 정보를 이용하여<br/><br/>

**상담 유형별** 최소값 최대값의 **지역**<br/>
**지역별** 최소값 최대값 의 **상담유형**<br/>
**전국별** 최소값 최대값의 **상담유형** 등의 데이터를 알아보자<br/><br/>

## 데이터셋 정보
해당 데이터는 [문화 빅데이터 플랫폼](https://www.bigdata-culture.kr/bigdata/user/data_market/detail.do?id=6aa14c34-4866-4a3f-9223-09c12d58ad4b, '문화 빅데이터 플랫폼')에서 받았고, <br/>
**지역별 상담 유형 통계 정보(2019)와 (2020)** 모두 같은 데이터였기 때문에<br/>
**지역별 상담 유형 통계 정보(2019)**만 사용됐으며<br/>
해당 데이터의 합계 데이터와 전체상담수 **데이터가 알맞지않아**<br/>
**삭제 후**에 남아있는 데이터들을 sum으로 **다시 채워넣었음**<br/><br/>

## 개발 과정
+ 먼저 기획의도에 따라 순서를 정함<br/>
1. 전체 데이터프레임을 보여줄 것, describe는 굳이?<br/>
2. 멀티셀렉트로 상담유형을 선택 할수 있게 할 것<br/>
3. 선택한 상담유형을 지역을 기준으로 데이터프레임과 bar차트와 pie차트 보여줄 것<br/>
4. 멀티셀렉트로 지역을 선택할 수 있게 할 것<br/>
5. 선택한 지역을 상담유형을 기준으로 데이터프레임과 bar차트와 pie차트 보여줄 것<br/>
    
+ 1. 데이터프레임<br/>
    + 먼저 컬럼명 수정, 알맞지않은 데이터들 수정 등<br/>
    + **재가공한 데이터프레임**을 **유저에게** 보여주고<br/><br/>
+ 2. 멀티셀렉트 상담유형<br/>
    + **지역**컬럼과 **합계** 컬럼을 **제외한 컬럼**을 **선택**하게끔 하여 진행<br/>
+ 3. 선택한 상담유형<br/>
    + **상담유형**을 **선택**하면 해당 상담유형의 **지역별 데이터**를<br/>
    + **Bar차트와 Pie차트**로 나타냄<br/>
    + **2개 이상 선택시** 따로 따로 **각각 2개씩**<br/>
    + 그리고 **상담수를 합산**한 **지역별 데이터** 나타나게 만들어짐<br/>
    + 이때 합산데이터가 위에 있는것이 보기 좋을것같아<br/>
    + 1개를 선택했을때는 보이지않지만<br/>
    + **2개 이상 선택시**에만 **상단**에 나타나게 함<br/>
+ 4. 멀티셀렉트 지역<br/>
    + **지역**컬럼의 **밸류값**을 **선택**하게끔 진행<br/>
+ 5. 선택한 지역<br/>
    + **지역**을 **선택**하면 해당 지역의 **상담유형별 데이터**를
    + **Bar차트와 Pie차트**로 나타내고<br/>
    + **2개 이상 선택시** 각 **지역을 합산**하여 보여줌<br/><br/>

## 추가 정보
이때 Bar차트와 Pie차트는 **인터랙티브 차트**이기때문에<br/>
줌인,줌아웃은 물론이고 막대나 파이의 조각을 마우스로 갖다대면<br/>
그 **크기의 숫자**를 나타내며<br/>
Pie차트의경우 **범례(legend)**에서 각각의 조각을 나타내는 이름을 누르면<br/>
그 **데이터를 빼고 보는것**도 가능하여 자기가 **보고싶은 데이터**를 **선택** 할 수 있다<br/><br/>

## 테스트 과정
이번 프로젝트에서는 테스트과정중에<br/>
데이터가 알맞지 않은 내용이 있다는것을 알게 되어<br/>
뒤늦게 데이터를 재가공한것을 제외하면<br/>
스무스하게 진행되었기때문에 이외의 문제는 없었다<br/>
<br/>

[만들어진 웹 사이트](http://ec2-3-39-253-5.ap-northeast-2.compute.amazonaws.com:8503)<br/><br/>