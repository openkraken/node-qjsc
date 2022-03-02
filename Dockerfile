# Build linux prebuild binary

# syntax=docker/dockerfile:1
FROM centos:centos7
RUN yum install centos-release-scl-rh -y
RUN yum install rh-nodejs12 -y
RUN yum install python3 -y
RUN yum install devtoolset-7 -y
