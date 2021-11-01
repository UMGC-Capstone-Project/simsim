  <!-- -v <path to config>:/config \ -->

docker build -t simsim:latest .

docker run \
    --name=simsim \
    -e TZ=America/Detroit \
    -p 8080:8080 \
    --restart unless-stopped \
    simsim:latest


```
 docker build -t simsim:0.1 .

  -v <path to config>:/config \

 docker run \
  --name=simsim \
  -e TZ=America/Detroit \
  -p 8080:8080 \
  --restart unless-stopped \
  simsim:latest




 docker build -t simsim:0.1 .

  -v <path to config>:/config \

 docker run \
  --name=simsim \
  -e TZ=America/Detroit \
  -p 8080:8080 \
  --restart unless-stopped \
  simsim:latest
```