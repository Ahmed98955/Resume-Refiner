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
    - [CV Enhancer](#cv-enhancer.py)
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


---

### Job Matcher Flow
<!-- IMAGE PLACEHOLDER: Job Matcher Diagram -->
<img width="2048" height="2048" alt="Gemini_Generated_Image_5bldi75bldi75bld" src="https://github.com/user-attachments/assets/fb4353a0-186c-4be6-a946-e468d573bbe6" />
## Proposed Diagram for CV Enhancer Module:

### Title:
`CV Enhancer Module Flow`

### Main Components (in boxes or rectangles):

* `User`
* `main.py` (Entry Point)
* `CV Enhancer (cv_enhancer.py)`
    * (Smaller text below: `Main Logic, User Interaction, Display Results`)
* `CV File (PDF/TXT)`
* `utils/pdf_reader.py`
    * (Smaller text below: `Extract Text from PDF`)
* `utils/gemini_api.py`
    * (Smaller text below: `AI Processing, Prompt Building`)
* `Enhanced CV & Analysis` (Output from Gemini)
* `Improved CV` (Displayed Output)
* `Suggestions` (Displayed Output)
* `Graphical Elements (Charts, Bars)` (Displayed Output)
* `Edit/Save` (User Option)
* `utils/cv_pdf_formatter.py`
    * (Smaller text below: `Convert to PDF`)

### Arrows (Flow of Operations and Data):

* `User` → (Launches) → `main.py`
* `main.py` → (Invokes) → `CV Enhancer (cv_enhancer.py)`
* `CV Enhancer (cv_enhancer.py)` → (Requests) → `CV File (PDF/TXT)`
* `CV File (PDF/TXT)` → (If PDF) → `utils/pdf_reader.py`
* `utils/pdf_reader.py` → (Extracted Text) → `CV Enhancer (cv_enhancer.py)`
* `CV Enhancer (cv_enhancer.py)` → (Sends Content) → `utils/gemini_api.py`
* `utils/gemini_api.py` → (Returns) → `Enhanced CV & Analysis`
* `Enhanced CV & Analysis` → (Processed and Displayed by) → `CV Enhancer (cv_enhancer.py)`
* `CV Enhancer (cv_enhancer.py)` → (Displays) → `Improved CV`, `Suggestions`, `Graphical Elements (Charts, Bars)`
* `Improved CV` → (User can) → `Edit/Save`
* `Edit/Save` → (If PDF save chosen) → `utils/cv_pdf_formatter.py`

---
### job Macher flow
<img width="2048" height="2048" alt="Gemini_Generated_Image_6uj94o6uj94o6uj9" src="https://github.com/user-attachments/assets/9fad6b9f-f779-419b-80ad-0909fa31275b" />
## Job Matcher Module: Detailed Explanation

### What is the Job Matcher?
The Job Matcher is an interactive command-line interface (CLI) tool designed to compare your CV with a specific job description. Its primary function is to assess your compatibility with the job, highlight your strengths and weaknesses, and present the results graphically with colors.

### How the Job Matcher Works (Step by Step):

1.  **Starting from the Main Menu**
    * The user selects "Job Matcher" from the main menu (`main.py`).
    * The script `modules/job_matcher.py` is invoked.

2.  **Data Input**
    * The program prompts the user to enter the path to their CV file (supports PDF or TXT).
    * It then asks the user to paste or input the text of the target job description.

3.  **Reading and Preparing Data**
    * If the file is PDF: Text is extracted using helper functions (`utils/pdf_reader.py`).
    * If the file is TXT: It's read directly as plain text.
    * The data is validated and prepared for submission.

4.  **Sending Data to Gemini AI**
    * A smart prompt containing the CV text and job description is constructed.
    * This prompt is sent to the Gemini API via a function in `utils/gemini_api.py`.
    * Gemini AI analyzes the CV against the job description and returns:
        * Match Score
        * Strengths
        * Weaknesses
        * Suggestions for improvement

5.  **Graphical Display of Results**
    * Results are displayed in the terminal in an engaging manner:
        * Colored Match Score Bar
        * Pie Chart for skill coverage
        * Skill Matrix Table with colored strengths/weaknesses
        * Textual list of strengths, weaknesses, and suggestions for improvement
        * Celebratory ASCII art if the match is high

6.  **Support for Multi-CV/Job Comparison**
    * Users can input multiple CVs or multiple job descriptions for comparison in one go.
    * Results are displayed in a colored comparison table with a horizontal bar chart showing the best matches.

7.  **User Interaction**
    * Users can retry the process, compare other files, or return to the main menu at any time.

### Core Components of the Job Matcher:

* `job_matcher.py`: Contains all logic for user interaction, file reading, prompt building, result display, and graphical elements.
* `utils/gemini_api.py`: Responsible for sending and receiving data from Gemini AI.
* `utils/pdf_reader.py`: For reading CV text from PDF files.
* `colorama`: For displaying colors in the terminal.
* `Helper Functions for Graphics`: E.g., functions for drawing bars, pie charts, colored tables, etc.

### How It Connects to Other Project Parts:

* It is invoked from the main menu (`main.py`).
* It uses functions from `utils/gemini_api.py` and `utils/pdf_reader.py` (and other helper utilities).
* It shares the same graphical result display style with other scripts (e.g., CV Enhancer) for consistency.

### Benefits for Users:

* Instantly and intelligently determine the suitability of your CV for any job.
* Receive detailed and actionable analysis to improve your career opportunities.
* Compare multiple CVs or jobs simultaneously.
* Enjoy a fun and easy-to-use experience through the terminal with graphics and colors.


---


### Gemini Chat Flow
<img width="2048" height="2048" alt="12131" src="https://github.com/user-attachments/assets/94dcd641-357c-4fa2-a2d9-f4c622f03993" />

## Gemini Chat Module: Detailed Explanation

### What is Gemini Chat?
Gemini Chat is an interactive command-line interface (CLI) chatbot tool that allows you to communicate directly with Google's Gemini AI model. You can type any question, inquiry, or text request, and Gemini will respond instantly within your terminal.

### How Gemini Chat Works (Step by Step):

1.  **Launch from Main Menu**
    * The user selects "Gemini Chat" from the main menu (`main.py`).
    * The script `modules/gemini_chat.py` is executed.

2.  **Welcome Interface**
    * A colored ASCII logo specific to Gemini is displayed, along with an engaging welcome message.

3.  **Start Conversation**
    * The program prompts you to type your message or question (any text: job inquiry, advice, information, etc.).
    * You can continue sending messages one after another, and Gemini will respond each time.

4.  **Sending and Receiving Messages**
    * Every message you type is sent to the Gemini API via `utils/gemini_api.py`.
    * The response from Gemini is received and displayed directly in the terminal.

5.  **End Conversation**
    * You can type "exit" or "quit" at any time to leave the chat mode and return to the main menu.

### Core Components of Gemini Chat:

* `gemini_chat.py`: Contains the logic for user interaction (message input, response display, ending the conversation).
* `utils/gemini_api.py`: Responsible for sending messages to the Gemini API and receiving responses.
* `colorama`: For displaying colors in messages and the welcome interface.
* `main.py`: Invokes this script when "Gemini Chat" is selected from the menu.

### How It Connects to Other Project Parts:

* It is called from the main menu (`main.py`).
* It uses the same Gemini AI communication functions as other scripts (`job_matcher`, `cv_enhancer`).
* Its graphical interface is unified with the rest of the project's parts (colored logo, welcome message).

### Benefits for Users:

* You can consult Gemini AI on any topic (professional, technical, advice, etc.) directly and quickly.
* No need for any external browser or application; everything happens through the terminal.
* An enjoyable and easy-to-use experience with a colorful and attractive interface.


---

### Full Project Architecture
<img width="2048" height="2048" alt="123" src="https://github.com/user-attachments/assets/f942e151-76a4-493c-9b73-2f2dbbb12044" />


---

## License

This project is licensed under the MIT License. See the LICENSE file for details.
