# AI Playtest Feedback Pipeline

AI-powered workflow that automates playtest feedback analysis using Python, OpenAI, Zapier, Google Forms, and Google Sheets.

---

## 🌐 Live Demo

**Website:** [Live Website](https://tideboundgames.lovable.app/)

**Case Study:** [Google Slides Presentation](https://docs.google.com/presentation/d/18fAqJl6uFvYU-09LYNv7RpCYiSEJvcIxCjbUF4Py1Gc/edit?usp=sharing)

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


1. Google Forms responses are stored in Google Sheets.
2. Zapier retrieves the latest responses.
3. **QuestionResponseFormatter.py** converts the raw spreadsheet data into structured `{Question: Response}` JSON.
4. Gemini AI analyzes the formatted responses.
5. A summarized report of bugs, suggestions, and overall player feedback is generated.

## Technologies

- Zapier
- Python
- Google Forms
- Google Sheets
- Gemini AI

## Sample JSON

```json
{
  "How fun was the game?": "Very fun",
  "What was confusing?": "The inventory",
  "Would you play again?": "Yes"
}
```

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
