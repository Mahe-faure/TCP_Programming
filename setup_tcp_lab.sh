#!/bin/bash

setup_tcp_server() {
    echo "Setting up TCP server on port 12345 using netcat..."
    echo "Hello from Client 1" | nc -l 12345
}

setup_tcp_client1() {
    echo "Setting up TCP client 1..."
    echo "Hello from Client 1" | nc localhost 12345
}

setup_tcp_client2() {
    echo "Setting up TCP client 2..."
    echo "Hello from Client 2" | nc localhost 12345
}

test_latency() {
  echo "Testing latency to localhost..."
  ping -c 4 localhost
}

test_bandwidth() {
  echo "Testing bandwidth using iperf3..."
  iperf3 -c localhost
}

measure_transfer_rate() {
    start_time=$(date + %s%N)
    setup_tcp_client1 &
    setup_tcp_client2 &
    end_time=$(date + %s%N)
    elapsed_time=$((end_time - start_time))
    elapsed_time_in_seconds=$(echo "scale=9; $elapsed_time / 1000000000" | bc)
    echo "Data tranfer time: $elapsed_time_in_seconds seconds"
}

install_xinetd() {
    echo "Intalling xinetd..."
    sudo apt update
    sudo apt install -y xinetd
}

main() {
    echo "Starting the lab session setup..."

    setup_tcp_server &
    sleep 2

    measure_transfer_rate

    test_latency &
    test_bandwidth &

    echo "Lab session setup complete"
}

main