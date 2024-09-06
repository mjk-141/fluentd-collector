import logging
import os
import time

# 로그 생성
logger = logging.getLogger()

# 로그의 출력 기준 설정
logger.setLevel(logging.INFO)

# log 출력 형식
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# log를 console에 출력
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

# log를 파일에 출력
log_file = os.path.join('/app/logs', 'error.log')
file_handler = logging.FileHandler(log_file)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

cnt = 0
while True:
    cnt += 1
    if cnt % 5:
        logger.warning(f'{cnt}번째 에러가 발생했습니다.')
    elif cnt % 7:
        logger.error(f'{cnt}번째 에러가 발생했습니다.')
    else:
        logger.info(f'{cnt}번째 에러가 발생했습니다.')
    time.sleep(1)
