FROM alpine

RUN apk add --no-cache python3 py3-pip socat dos2unix

# 創建工作目錄
RUN mkdir -p /chal
WORKDIR /chal

# 複製當前目錄下的所有文件到容器的 /chal 目錄
COPY . .

# 轉換行結尾格式
RUN dos2unix /chal/init.sh

# 確保 init.sh 是可執行的
RUN chmod +x /chal/init.sh

# 開放 10000 端口
EXPOSE 10000

# 執行 init.sh
CMD ["./init.sh"]

