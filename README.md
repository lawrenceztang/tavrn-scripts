# Law Firm Intake Transcription Generator with OpenAI

This script generates realistic transcriptions for law firm intake calls using OpenAI's GPT models, with half being cases that should be accepted and half that should be declined.

## Overview

Law firms need to capture critical information through call transcription, send engagement letters for signature, and determine whether a matter is worth pursuing. This tool uses OpenAI's API to generate highly realistic and varied training data based on proven templates.

## Features

- **AI-Powered Generation**: Uses OpenAI's o3 to create unique, realistic transcriptions
- **Template-Based**: Built on proven accept/decline templates that ensure quality and consistency
- **Realistic Conversations**: AI-generated transcriptions follow natural conversation patterns between intake staff and prospective clients
- **Balanced Dataset**: Produces equal numbers of cases that should be accepted vs. declined
- **Graceful Fallback**: If OpenAI API is unavailable, automatically falls back to template-based generation
- **Multiple Case Types**: Covers various practice areas including:
  - Car accidents
  - Slip and fall incidents
  - Medical malpractice
  - Workers' compensation
  - Product liability
  - Wrongful death
  - Premises liability
  - Dog bite cases
  - Motorcycle accidents

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

**Note**: If you don't have OpenAI installed, the script will automatically use fallback templates.

### 2. Set OpenAI API Key (Optional)

For AI-powered generation, you'll need an OpenAI API key from [OpenAI's website](https://platform.openai.com/api-keys).

Set your API key as an environment variable:

```bash
export OPENAI_API_KEY='your-api-key-here'
```

Or on Windows:
```cmd
set OPENAI_API_KEY=your-api-key-here
```

## Usage

### Generate Full Dataset

Run the script to generate 20 transcriptions (10 accept, 10 decline):

```bash
python3 create_transcriptions.py
```

The script will:
1. Use AI to generate unique transcriptions
2. Create individual `.txt` files organized in separate folders:
   - `transcriptions/accept/01_car_accident.txt`
   - `transcriptions/decline/02_slip_and_fall.txt`

## How It Works

### Base Templates

The script uses two proven base templates:

**Accept Template**: Features a recent incident with clear fault, witnesses, police report, significant injuries, medical documentation, and insurance company issues.

**Decline Template**: Features an older incident where the client admits fault, has minimal documentation, delayed medical treatment, and other factors that make the case unviable.