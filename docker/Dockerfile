# docker/Dockerfile — reproducible Verilog simulation environment
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

# --- Install system dependencies ---
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    make \
    python3 \
    python3-pip \
    git \
    wget \
    iverilog \
    verilator \
    yosys \
    gtkwave \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# --- Install Python packages (for test automation) ---
RUN pip3 install --no-cache-dir \
    cocotb \
    pytest \
    cocotb-test

# --- Create workspace directory ---
WORKDIR /workspace
COPY . /workspace

ENTRYPOINT ["/bin/bash"]

