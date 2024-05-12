from __future__ import annotations
import datetime

import pendulum
from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="dags_bash_operator",                         # Dag의 이름 (파일명과 동일하게 할 것!)
    schedule="0 0 * * *",                                   # 크론탭 스케쥴러 (분 시 일 월 요일)
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),     # 시작시간 설정 UTC : 글로벌 -> Asia/Seoul
    catchup=False,                                                  # 누락된 부분도 돌릴건지 설정 
    # dagrun_timeout=datetime.timedelta(minutes=60),                  # 옵션
    # tags=["example", "example2"],                                   # 카테고리와 동일
    # params={"example_key": "example_value"},                        # 아래 테스크에 공통적으로 쓸 파라미터 설정
) as dag:
# [START howto_operator_bash]
    bash_t1 = BashOperator(
        task_id="bash_t1",       # task에 나타나는 이름
        bash_command="echo whoami", # shell script 작성
    )
    # [END howto_operator_bash]
    bash_t2 = BashOperator(
        task_id="bash_t2",       # task에 나타나는 이름
        bash_command="echo $HOSTNAME", # shell script 작성
    )

    bash_t1 >> bash_t2