FROM debian:stable-slim

# variable store
ENV CONAN_UPLOAD_CUSTOM 0
ARG WDIR="/s0nhbuild"

# install basic packages
RUN \
    apt update \
    && \
    apt install -y \
                build-essential \
                nghttp2 \
                libnghttp2-dev \
                curl \
                git \
                gcc \
                libssl-dev \
                python \
                python3 \
                python3-pip \
                make \
                zip \
                sudo \
                bc \
    && \
    apt autoremove -y

# place sources from host to container
COPY . $WDIR
WORKDIR $WDIR

# install pip packages
RUN python3 -m pip install -r requirements.txt

# launch app
CMD [ "/bin/bash" ]
