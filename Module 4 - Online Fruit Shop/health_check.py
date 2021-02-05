#!/usr/bin/env python3

import email.message
import smtplib
from email_report import generate_basic, send


if __name__ == "__main__":
  # check if CPU usage is over 80%
  # check if available disk space is lower than 20%
  # check if available memory is less than 500MB
  # check if hostname "localhost" cannot be resolved to "127.0.0.1"
  # if a check fails, email a report
