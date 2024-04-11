#!/usr/bin/env python3
import os
import pty
import time
import tty
import select
import random
import json

def create_virtual_terminal():
    master_fd, slave_fd = pty.openpty()
    tty.setraw(master_fd)
    return master_fd, slave_fd

def write_to_terminal(fd, data):
    os.write(fd, data.encode())

def read_from_terminal(fd):
    try:
        r, _, _ = select.select([fd], [], [], 0.1)
        if r:
            return os.read(fd, 1024).decode()
    except OSError:
        pass
    return ''

def read_loop(fd):
    while True:
        terminal_output = read_from_terminal(fd)
        while terminal_output:
            print(terminal_output, end='')
            terminal_output = read_from_terminal(fd)

def write_loop(fd):
    delay = 5
    while True:
        x = { "tempair":  str(round(random.uniform(20, 30),2)),
              "humidity":  str(round(random.uniform(50, 60),2)),
            #   "light":  (String)light;
            #   "flow":  (String)flow;
            #   "co2":  (String)co2;
            #   "tempwet":  (String)tempwet;
            #   "ec":  (String)ec;
            #   "ph":  (String)ph;
            #   "moisture":  (String)moisture;
         }
        data = json.dumps(x) + '\n'
        write_to_terminal(fd, data)
        print(data)
        time.sleep(delay)

if __name__ == "__main__":
    master_fd, slave_fd = create_virtual_terminal()
    stty = os.ttyname(slave_fd)
    print(f"Virtual terminal created: {stty}\nPress Ctrl+C to exit.")
    try:
        # read_loop(master_fd)
        write_loop(master_fd)
    except KeyboardInterrupt:
        pass
    finally:
        os.close(master_fd)
        os.close(slave_fd)
