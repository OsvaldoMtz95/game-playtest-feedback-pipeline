# AI Playtest Feedback Pipeline

AI-powered workflow that automates playtest feedback analysis using Python, OpenAI, Zapier, Google Forms, and Google Sheets.

---

## 🌐 Live Demo

**Website:** [Live Website](YOUR_WEBSITE_LINK)

**Case Study:** [Google Slides Presentation](https://tideboundgames.lovable.app/)

---

## Overview

This project automates the collection, organization, analysis, and reporting of player feedback submitted after game playtests. Survey responses are transformed into structured JSON, analyzed with AI, reviewed through a human approval step, and automatically delivered to the development team as a concise QA report.

---

## Problem

Manual review of player feedback was repetitive, time-consuming, and made it difficult to consistently identify recurring bugs, gameplay issues, and feature requests before the next playtest.

---

## Solution

Built an end-to-end automation pipeline that collects Google Form responses, converts them into structured JSON using Python, analyzes the feedback with OpenAI through Zapier, requests human approval, and automatically emails a prioritized report to the development team.

---

## Workflow

1. Players submit feedback through a Google Form.
2. Responses are automatically stored in Google Sheets.
3. A Python script converts the responses into structured JSON.
4. Zapier sends the JSON to OpenAI for analysis.
5. AI generates a summarized QA report with development priorities.
6. A human approval step reviews the report.
7. The approved report is automatically emailed to the development team.

---

## Technologies

- Python
- OpenAI API
- Zapier
- Google Forms
- Google Sheets
- JSON

---

## Results

- Reduced playtest review time by an estimated **80–90%**.
- Automated generation of standardized QA reports.
- Improved visibility into recurring bugs and feature requests.
- Added human approval before report delivery.
