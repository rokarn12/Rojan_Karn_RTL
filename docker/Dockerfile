FROM ubuntu:22.04

# Prevent timezone prompt
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    build-essential \
    python3 \
    python3-pip \
    git \
    wget \
    make \
    iverilog \
    verilator \
    yosys \
    gtkwave \
    vim \
    bash \
    && pip3 install cocotb \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

