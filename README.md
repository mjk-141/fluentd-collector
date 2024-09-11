# fluentd-collector
## 1-1. 전체 컨테이너 구성(워크플로우)
![fluentd-collector](https://github.com/user-attachments/assets/8942989d-e3a9-4619-93fe-da3b1a342bcb)
- 로그 보낼 서버(파이썬, 스프링, 아파치 등등) → fluentd → aggregator(선택사항) → elasticsearch → kibana

![fluentd-info](./assets/fluentd-info.png)
