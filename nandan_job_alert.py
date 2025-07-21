import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def search_indeed_jobs():
    job_keywords = [
        "networking engineer", "automation test engineer", "qa engineer",
        "graduate engineer trainee", "GET", "python automation engineer"
    ]
    location = "Bengaluru"
    results = []

    headers = {"User-Agent": "Mozilla/5.0"}
    for keyword in job_keywords:
        keyword_query = "+".join(keyword.split())
        url = f"https://www.indeed.com/jobs?q={keyword_query}&l={location}&fromage=1"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        for div in soup.find_all(name="a", attrs={"data-hide-spinner": "true"}):
            title = div.text.strip()
            link = "https://www.indeed.com" + div.get("href")
            if title and link:
                results.append(f"{title}\n{link}\n")

    return results

def send_email(jobs):
    email_user = os.getenv("EMAIL_USER")
    email_pass = os.getenv("EMAIL_PASS")
    email_to = os.getenv("EMAIL_TO")

    if not jobs:
        jobs = ["No new jobs found today."]

    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Job Alert – Daily Listings"
    msg["From"] = email_user
    msg["To"] = email_to

    html_jobs = "<br><br>".join(jobs)
    body = MIMEText(html_jobs, "html")
    msg.attach(body)

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(email_user, email_pass)
        server.sendmail(email_user, email_to, msg.as_string())

def main():
    jobs = search_indeed_jobs()
    send_email(jobs)

if __name__ == "__main__":
    main()
