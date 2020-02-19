FROM node:alpine

MAINTAINER zhangmengjie "zhangmengjie@gmail.com"

RUN wget https://github.com/mobz/elasticsearch-head/archive/master.zip && unzip master.zip && rm -rf master.zip && cd elasticsearch-head-master && npm install

WORKDIR /elasticsearch-head-master

CMD ["npm", "run", "start"]