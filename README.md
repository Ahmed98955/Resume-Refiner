# Gemini-Powered-Local-AI-Agent

A powerful, colorful, and interactive CLI tool for enhancing your CV, matching it with jobs, and chatting with Gemini AI—all from your terminal with beautiful ASCII graphics.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Features & Benefits](#features--benefits)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Scripts Explained](#scripts-explained)
    - [CV Enhancer](#cv-enhancer)
    - [Job Matcher](#job-matcher)
    - [Gemini Chat](#gemini-chat)
    - [Main Menu](#main-menu)
- [Diagrams](#diagrams)
- [License](#license)

---

## Project Overview

**AI CV Assistant** is a smart, modular command-line assistant that helps you:
- Instantly enhance your CV with AI
- Match your CV to job descriptions and visualize your fit
- Compare multiple CVs/jobs with colorful charts
- Chat directly with Gemini AI from your terminal

All with a playful, modern CLI experience featuring ASCII art logos, progress bars, skill matrices, and more!

---

## Features & Benefits
- **CV Enhancement:** Instantly improve your CV with AI suggestions and formatting
- **Job Matching:** See how well your CV fits a job, with strengths, weaknesses, and improvement tips
- **Multi-CV/Job Comparison:** Compare several CVs or jobs at once with colored bar charts and tables
- **Gemini Chat:** Converse directly with Gemini AI for career advice or anything else
- **Beautiful CLI:** ASCII art, color highlights, animated progress bars, and interactive menus
- **Modular & Extensible:** Easy to add new features or customize the experience

---

## Project Structure

```text
D:/AI/ai_assistant/
│
├── main.py                # Main entrypoint (CLI menu)
│
├── modules/
│   ├── cv_enhancer.py     # Enhance your CV with AI
│   ├── job_matcher.py     # Match your CV to job descriptions
│   ├── gemini_chat.py     # Chat with Gemini AI
│   └── __init__.py        # Package marker
│
├── utils/
│   ├── gemini_api.py      # Gemini API integration
│   ├── cv_pdf_formatter.py# PDF conversion utilities
│   ├── pdf_reader.py      # PDF text extraction
│   └── __init__.py        # Package marker
│
├── requirements.txt       # Python dependencies
├── README.md              # This file
├── .env                   # Environment variables (not in git)
├── .gitignore             # Ignore rules for git
├── LICENSE                # Project license
└── [data/, outputs/, ...] # (Optional: data, outputs, etc.)
```

---

## Installation

1. **Install Python 3.10+**  
   Download from [python.org](https://www.python.org/downloads/).

2. **Clone this repository:**
   ```bash
   git clone https://github.com/Ahmed98955/Resume-Refiner/
   cd AI-CV-Assistant
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your environment variables:**
   - Copy `.env` or create a new one with your Gemini API key:
     ```env
     GEMINI_API_KEY=your-key-here
     ```

---

## Usage

Run the main menu:
```bash
python main.py
```

You will see a colorful menu to:
- Enhance your CV
- Match your CV with a job
- Chat with Gemini
- Exit

Each module provides an interactive, graphical CLI experience.

---

## Scripts Explained

### 1. CV Enhancer (`modules/cv_enhancer.py`)
- **Purpose:** Enhance your CV using Gemini AI.
- **How it works:**
  - Upload your CV (PDF or TXT)
  - The script extracts the text and sends it to Gemini AI
  - Gemini returns an improved CV and suggestions
  - You can edit, save, and visualize the results with charts and skill matrices

---

### 2. Job Matcher (`modules/job_matcher.py`)
- **Purpose:** Match your CV to a job description and visualize your fit.
- **How it works:**
  - Provide your CV and a job description
  - The script sends both to Gemini AI
  - Get a fit score, strengths, weaknesses, and improvement tips
  - Supports comparing multiple CVs/jobs at once with colored bar charts

---

### 3. Gemini Chat (`modules/gemini_chat.py`)
- **Purpose:** Chat directly with Gemini AI in your terminal.
- **How it works:**
  - Type messages and get instant AI replies
  - Great for career advice, Q&A, or general chat

---

### 4. Main Menu (`main.py`)
- **Purpose:** The entrypoint and navigation menu for all features.
- **How it works:**
  - Shows a big ASCII art logo and colorful menu
  - Lets you launch any module interactively

---

## Diagrams

### CV Enhancer Flow
<!-- IMAGE PLACEHOLDER: CV Enhancer Diagram -->

---

### Job Matcher Flow
<!-- IMAGE PLACEHOLDER: Job Matcher Diagram -->

---

### Gemini Chat Flow
<!-- IMAGE PLACEHOLDER: Gemini Chat Diagram -->

---

### Full Project Architecture
<!-- IMAGE PLACEHOLDER: Full Project Diagram -->

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.
