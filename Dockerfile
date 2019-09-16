FROM centos:centos7

RUN yum -y update; yum clean all
RUN yum -y install epel-release; yum clean all
RUN yum -y install https://centos7.iuscommunity.org/ius-release.rpm; yum clean all
RUN yum -y install python36u python36u-devel python36u-pip; yum clean all

WORKDIR /usr/src/app
COPY job_api ./job_api
COPY requirements.txt ./
RUN python3.6 -m pip install -r ./requirements.txt
RUN python3.6 -m pip install gunicorn
RUN python3.6 -m spacy download en_core_web_lg
ENTRYPOINT ["gunicorn", "--workers=1", "-b", "0.0.0.0:80", "job_api:application"]
EXPOSE 80