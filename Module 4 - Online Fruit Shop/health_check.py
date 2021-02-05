#!/usr/bin/env python3

import os
import shutil, psutil, socket
import email.message
import smtplib
from email_report import generate_basic, send


def check_cpu_usage():
  cpu_usage = psutil.cpu_percent(interval=0.1)
  return cpu_usage > 80


def check_disk_usage():
  total, used, free = shutil.disk_usage(os.path.expanduser("~"))
  return free/total < 0.2


def check_mem_usage():
  mem_mb = psutil.virtual_memory().available / (1024 ** 2)
  return mem_mb < 500


def check_localhost():
  localhost = socket.gethostbyname("localhost")
  return localhost != "127.0.0.1"


def main():
  sender = "automation@example.com"
  recipient = "<REPLACE_WITH_USERNAME>@example.com"
  body = "Please check your system and resolve the issue as soon as possible."
  subject = ""

  # check if CPU usage is over 80%
  if check_cpu_usage():
    subject = "Error - CPU usage is over 80%"

  # check if available disk space is lower than 20%
  if check_disk_usage():
    subject = "Error - Available disk space is less than 20%"

  # check if available memory is less than 500MB
  if check_mem_usage():
    subject = "Error - Available memory is less than 500MB"

  # check if hostname "localhost" cannot be resolved to "127.0.0.1"
  if check_localhost():
    subject = "Error - localhost cannot be resolved to 127.0.0.1"

  # if a check fails, email a report
  if subject != "":
    message = generate_basic(sender, recipient, subject, body)
    send(message)


if __name__ == "__main__":
  main()
