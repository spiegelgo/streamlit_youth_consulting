# streamlit_youth_consulting
 
지역별 상담 유형 통계 정보를 이용하여<br/><br/>

상담 유형별 최소값 최대값의 지역<br/>
지역별 최소값 최대값 의 상담유형<br/>
전국별 최소값 최대값의 상담유형 등의 데이터를 알아보자<br/><br/>

해당 데이터는 [문화 빅데이터 플랫폼](
https://www.bigdata-culture.kr/bigdata/user/data_market/detail.do?id=6aa14c34-4866-4a3f-9223-09c12d58ad4b, '문화 빅데이터 플랫폼')<br/>
에서 받았으며 2019와 2020 모두 같은 데이터였기 때문에 2019만 사용됐으며<br/>
해당 데이터의 합계 데이터와 전체상담수 데이터가 알맞지않아<br/>
삭제 후에 남아있는 데이터들을 sum으로 다시 채워넣었음<br/><br/>

먼저 컬럼명 수정, 알맞지않은 데이터들 수정 등<br/>
재가공한 데이터프레임을 유저에게 보여주고<br/><br/>

상담유형을 선택하면 해당 상담유형의 지역별 데이터를<br/>
Bar차트와 Pie차트로 나타냄<br/>
2개 이상 선택시 따로따로 각각 2개씩 나타나게 만들어짐<br/><br/>

그리고 이번에는 지역을 선택하면 해당 지역의 상담유형별 데이터를
Bar차트와 Pie차트로 나타내고<br/>
2개 이상 선택시 합산하여 보여줌<br/><br/>

이때 Bar차트와 Pie차트는 인터랙티브 차트이기때문에<br/>
줌인,줌아웃은 물론이고 막대나 파이의 조각을 마우스로 갖다대면<br/>
그 크기의 숫자를 나타내며<br/>
Pie차트의경우 범례(legend)에서 각각의 조각을 나타내는 이름을 누르면<br/>
그 데이터를 빼고 보는것도 가능하여 자기가 보고싶은 데이터를 선택 할 수 있다<br/>
