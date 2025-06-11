# Usage Examples

This document provides examples of how to use the Law Firm Intake Transcription Generator.

## Basic Usage

### Generate Default Dataset (20 transcriptions)

```bash
python3 create_transcriptions.py
```

This will create:
- 10 accept cases in `transcriptions/accept/`
- 10 decline cases in `transcriptions/decline/`

### Test OpenAI Integration

```bash
python3 demo_with_openai.py
```

This will test the OpenAI connection and generate sample cases.

## With OpenAI API Key

### Set API Key and Generate

```bash
export OPENAI_API_KEY='your-api-key-here'
python3 create_transcriptions.py
```

This will use AI to generate unique, varied transcriptions.

### Windows Users

```cmd
set OPENAI_API_KEY=your-api-key-here
python3 create_transcriptions.py
```

## Customizing the Script

### Modify Number of Transcriptions

Edit `create_transcriptions.py` and change:

```python
# Generate 40 transcriptions instead of 20
num_transcriptions = 40
```

### Add New Case Types

Edit the `case_types` list:

```python
self.case_types = [
    "car_accident", "slip_and_fall", "medical_malpractice",
    "workers_compensation", "product_liability", "wrongful_death", 
    "dog_bite", "premises_liability", "motorcycle_accident",
    "construction_accident",  # Add new case type
    "nursing_home_abuse"      # Add another new case type
]
```

### Modify OpenAI Parameters

Edit the `chat.completions.create()` calls:

```python
response = self.openai_client.chat.completions.create(
    model="gpt-4",  # Use GPT-4 instead of GPT-3.5-turbo
    messages=[...],
    max_tokens=2000,  # Increase token limit
    temperature=0.8   # Increase creativity
)
```

## Expected Output Structure

```
transcriptions/
├── accept/
│   ├── 01_car_accident.txt
│   ├── 02_slip_and_fall.txt
│   ├── 03_medical_malpractice.txt
│   └── ...
└── decline/
    ├── 01_workers_compensation.txt
    ├── 02_product_liability.txt
    ├── 03_wrongful_death.txt
    └── ...
```

## Sample Generated Content

### Accept Case Example
```
Speaker 0: Good morning, Mira Law Firm. This is Jennifer speaking...
Speaker 1: Hi, my name is Sarah Johnson. I was in a car accident...
[Clear fault, witnesses, good documentation, significant injuries]
```

### Decline Case Example
```
Speaker 0: Mira Law Firm, this is Rachel. How can I help you?
Speaker 1: Hi, I'm Michael Brown. I had a slip and fall...
[Old incident, poor documentation, statute of limitations issues]
```

## Troubleshooting Common Issues

### OpenAI Not Available
- Script automatically falls back to templates
- No action needed, generation continues

### API Key Issues
- Check key is set correctly: `echo $OPENAI_API_KEY`
- Verify account has credits
- Test with demo script first

### Permission Errors
- Ensure write permissions in current directory
- Script creates `transcriptions/` folder automatically

## Integration with Other Tools

### Use with Machine Learning
```python
import os
import glob

# Load all accept cases
accept_files = glob.glob('transcriptions/accept/*.txt')
accept_data = []
for file in accept_files:
    with open(file, 'r') as f:
        accept_data.append(f.read())

# Load all decline cases  
decline_files = glob.glob('transcriptions/decline/*.txt')
decline_data = []
for file in decline_files:
    with open(file, 'r') as f:
        decline_data.append(f.read())

# Now you have labeled training data
```

### Batch Processing
```bash
# Generate multiple datasets
for i in {1..5}; do
    mkdir -p "dataset_$i"
    cd "dataset_$i"
    python3 ../create_transcriptions.py
    cd ..
done
``` 