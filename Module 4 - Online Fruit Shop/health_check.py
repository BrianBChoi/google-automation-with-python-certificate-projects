#!/usr/bin/env python3

import os
import shutil
import email.message
import smtplib
from email_report import generate_basic, send


if __name__ == "__main__":
  sender = "automation@example.com"
  recipient = "<REPLACE_WITH_USERNAME>@example.com"
  body = "Please check your system and resolve the issue as soon as possible."

  # check if CPU usage is over 80%
  # check if available disk space is lower than 20%
  total, used, free = shutil.disk_usage(os.path.expanduser("~"))
  if free/total < 0.2:
    subject = "Error - Available disk space is less than 20%"
    message = generate_basic(sender, recipient, subject, body)
    send(message)
  # check if available memory is less than 500MB
  # check if hostname "localhost" cannot be resolved to "127.0.0.1"
  # if a check fails, email a report
