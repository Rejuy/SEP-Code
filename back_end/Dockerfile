FROM python:3.8

# RUN echo 'python3.8'

RUN mkdir /code
WORKDIR /code
ADD requirements.txt .
RUN pip install pip -U -i https://pypi.tuna.tsinghua.edu.cn/simple && pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple