# Nandan's Daily Job Alert Bot 🚀

This bot sends job listings to your email every day at 7:00 AM IST.

---

## ✅ What It Covers:
- Roles: Networking, QA, Automation, Python, GET, Trainee
- Experience: 1–3 years
- Locations: Bengaluru + Remote
- Companies: MNCs, Startups, Foreign
- Sources: Indeed, Naukri, LinkedIn, Google Jobs, Internshala, company portals

---

## 🛠 Setup Steps:

### 1. Create a GitHub Repository
- Go to https://github.com/new
- Name it `daily-job-alert`
- Leave it empty, then click "Create repository"

### 2. Upload Files
- Unzip this folder
- Go to repo → “Add file” → “Upload files”
- Upload: `nandan_job_alert.py`, `README.md`
- Commit the changes

### 3. Gmail App Password
- Enable 2FA at: https://myaccount.google.com/security
- Then: https://myaccount.google.com/apppasswords
- App: Mail, Device: GitHub → Generate → Copy 16-char password

### 4. Add GitHub Secrets
Go to:
- Settings → Secrets and variables → Actions
Add:

| Name        | Value                             |
|-------------|-----------------------------------|
| EMAIL_USER  | Your Gmail (e.g. nandanjs2018@gmail.com) |
| EMAIL_PASS  | Gmail app password                |
| EMAIL_TO    | Same Gmail or another recipient   |

### 5. Add Workflow File
- Create file: `.github/workflows/daily.yml`
- Paste:

```yaml
name: Daily Job Alert

on:
  schedule:
    - cron: '30 1 * * *'  # Runs 7 AM IST daily
  workflow_dispatch:

jobs:
  job-alert:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - run: python nandan_job_alert.py
        env:
          EMAIL_USER: ${{ secrets.EMAIL_USER }}
          EMAIL_PASS: ${{ secrets.EMAIL_PASS }}
          EMAIL_TO: ${{ secrets.EMAIL_TO }}
```

### 6. Run It Once
- Go to **Actions** → Select **Run workflow**
- Check your email!

Now your job alerts will run automatically every morning 🎉
