# Law Firm Intake Transcription Generator

This script uses OpenAI to generate realistic law firm intake call transcriptions—half are cases that should be **accepted**, half **declined**.

## Features

- **AI-Generated Dialogues**: Natural conversations between intake staff and prospective clients.
- **Case Diversity**: Covers a range of personal injury types:
  - Car accidents
  - Slip and fall
  - Medical malpractice
  - Workers’ comp
  - Product liability
  - Wrongful death
  - Premises liability
  - Dog bites
  - Motorcycle accidents
- **Structured Output**: Saves `.txt` files under:
  - `transcriptions/accept/`
  - `transcriptions/decline/`

## Setup

### 1. Install Dependencies
```
pip install -r requirements.txt
```

### 2. Set OpenAI API Key
Get your key from OpenAI and set it:
```
export OPENAI_API_KEY='your-api-key-here'  # macOS/Linux
set OPENAI_API_KEY=your-api-key-here       # Windows
```
## Usage
To generate 20 transcriptions (10 accepted, 10 declined):
```
python3 create_transcriptions.py
```
