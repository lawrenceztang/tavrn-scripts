#!/usr/bin/env python3
"""
Law Firm Intake Transcription Generator with OpenAI

This script generates realistic transcriptions for law firm intake calls using OpenAI API,
with half being cases that should be accepted and half that should be declined.
"""

import random
import os
from datetime import datetime, timedelta
from typing import Dict

# Try to import OpenAI, but make it optional
try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False
    OpenAI = None

class TranscriptionGenerator:
    def __init__(self, api_key: str = None):
        self.case_types = [
            "car_accident", "slip_and_fall", "medical_malpractice",
            "workers_compensation", "product_liability", "wrongful_death", 
            "dog_bite", "premises_liability", "motorcycle_accident"
        ]
        
        # Initialize OpenAI client only if available
        self.openai_client = None
        if OPENAI_AVAILABLE:
            try:
                if api_key:
                    self.openai_client = OpenAI(api_key=api_key)
                else:
                    # Try to get from environment variable
                    self.openai_client = OpenAI()  # Will use OPENAI_API_KEY env var
            except Exception as e:
                print(f"Warning: Could not initialize OpenAI client: {e}")
                self.openai_client = None

    def generate_personal_info(self) -> Dict[str, str]:
        """Generate random personal information for clients"""
        first_names = ["Michael", "Sarah", "David", "Jennifer", "Robert", "Lisa", "James", "Maria", 
                      "John", "Amanda", "Christopher", "Jessica", "Daniel", "Ashley", "Matthew", "Emily"]
        last_names = ["Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez",
                     "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor"]
        
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        
        # Generate phone number
        area_codes = ["415", "510", "650", "408", "925", "707", "831", "209"]
        phone = f"({random.choice(area_codes)}) 555-{random.randint(1000, 9999)}"
        
        # Generate email
        email_domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "proton.me"]
        email = f"{first_name.lower()}.{last_name.lower()}@{random.choice(email_domains)}"
        
        return {
            "first_name": first_name,
            "last_name": last_name,
            "full_name": f"{first_name} {last_name}",
            "phone": phone,
            "email": email
        }

    base_accept_transcription = """Speaker 0: Good afternoon. Thank you for calling Mira Law Firm. This is Sally. May I have your full name, please?

Speaker 1: Hi. My name is Michael Thompson.

Speaker 0: Thank you, Mr. Thompson. What's the best phone number to reach you?

Speaker 1: Sure. It's (415) 555-0137.

Speaker 0: And an email address?

Speaker 1: MThompson@gmail.com.

Speaker 0: Great. For verification, could you give me your date of birth?

Speaker 1: May 14th, 1984.

Speaker 0: Thanks. Now, can you briefly describe what happened that led to your injury?

Speaker 1: On March 15th, 2025, I slipped on a puddle in the produce aisle at Green Grocer Market on Mission Street. There were no warning signs.

Speaker 0: I'm sorry to hear that. What injuries did you sustain?

Speaker 1: Mostly my lower back and right hip. I felt a sharp pain right away.

Speaker 0: Did you receive medical treatment?

Speaker 1: Yes. I went to St. Francis Memorial Hospital (inaudible) that afternoon and had X-rays. They later referred me to Dr. Emily Reyes, a physical therapy specialist.

Speaker 0: Understood. Are you still treating?

Speaker 1: Yes. I've had three PT sessions so far and another scheduled next week.

Speaker 0: Do you have health insurance?

Speaker 1: I do. Blue Cross PPO, policy number BCP-7264-91.

Speaker 0: And did you miss any work because of the incident?

Speaker 1: I missed five days and used up my sick leave.

Speaker 0: What is your employer's name and your position?

Speaker 1: I'm a project manager at Bay Area Construction.

Speaker 0: Thanks. On a scale of one to 10, what's your pain level today?

Speaker 1: I'm a project manager at Bay Area Construction.

Speaker 0: Got it. We're almost done. May I get the grocery store's address if you have it?

Speaker 1: It's 1234 Mission Street, San Francisco, California 94110.

Speaker 0: Perfect. We'll review your case right away. The next step is to send you a HIPAA release and contingency fee agreement for electronic signature so we can obtain your records and move forward. Does that sound okay?

Speaker 1: Yes, that's fine.

Speaker 0: Great. You'll receive an email with further instructions within the next few minutes. If you have any questions, reply to those messages or call me at the number in your caller ID. Anything else I can help with today?

Speaker 1: No, that covers it. Thank you for your help.

Speaker 0: You're welcome, Mr. Thompson. Take care, and we'll be in touch soon."""

    base_decline_transcription = """Speaker 0: Mira Intake, Maya speaking. How can I help?

Speaker 1: Hi, I'm Marcus Bell. I was in a crash a couple weeks ago and my back's still hurting. Wanted to see if I have a case.

Speaker 0: I'm sorry to hear that, Marcus. Can you tell me what happened?

Speaker 1: Sure. On May 6th around 7:00 PM, I merged onto Highway 78 too quickly and clipped a delivery van with my left rear quarter panel. I spun, but stopped in the shoulder. Damage looks minor. Bumper's scratched and the taillight's cracked.

Speaker 0: Did police come to the scene?

Speaker 1: Yeah. They filed a report. Numbers 25050692.

Speaker 0: Were paramedics called?

Speaker 1: No. I felt shaky, but thought I was okay. The next day my lower back tightened up. I finally saw urgent care five days later. They said muscle strain and gave me muscle relaxers.

Speaker 0: Understood. Any followup treatment?

Speaker 1: Two chiropractic visits so far. Pain's about a five out of 10, spikes to seven if I sit too long.

Speaker 0: Have you missed work?

Speaker 1: Just half-days for the chiro. I'm a warehouse supervisor at Northstar Logistics.

Speaker 0: Thank you. Any prior back issues we should note?

Speaker 1: I slipped a disc two years ago, but it was healed. This pain feels different.

Speaker 0: Got it. Do you recall the delivery company or their insurer?

Speaker 1: Van had a Flash Cart logo. Officer gave me their policy number, but I don't have it handy.

Speaker 0: No worries. You can email it later. Last thing, what's the best contact number and email for you?

Speaker 1: Phone 404-555-7731. Email M-B-E-L-L78@proton.me.

Speaker 0: Perfect. Marcus, we should be able to follow up within 48 hours to discuss next steps.

Speaker 1: Sounds good. Thanks."""

    def generate_accept_transcription(self, case_type: str) -> str:
        """Generate a transcription for a case that should be accepted using OpenAI"""
        client_info = self.generate_personal_info()
        incident_date = (datetime.now() - timedelta(days=random.randint(7, 45))).strftime("%B %d, %Y")
        prompt = f"""Based on the following example for a law firm intake call that should be ACCEPTED, create a new realistic transcription for a {case_type.replace('_', ' ')} case.

EXAMPLE:
{self.base_accept_transcription}

REQUIREMENTS:
- Change the client name to: {client_info['full_name']}
- Change the phone to: {client_info['phone']}
- Change the email to: {client_info['email']}
- Change the incident date to: {incident_date}
- Adapt the case details to be specific to a {case_type.replace('_', ' ')} case
- Keep the same conversation structure and professional tone
- Make the conversation natural and realistic
- Keep the same Speaker 0/Speaker 1 format

Factors to consider for accepting or declining a case could include potential settlement value, likelihood of a settlement, severity of injuries sustained etc.

Generate only the transcription dialogue for a case which should be ACCEPTED, no additional text."""

        try:
            response = self.openai_client.chat.completions.create(
                model="o3",
                messages=[
                    {"role": "system", "content": "You are an expert at creating realistic law firm intake call transcriptions. Generate only the dialogue in the exact format requested."},
                    {"role": "user", "content": prompt}
                ],
                temperature=1
            )
            
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"Error generating accept transcription: {e}")

    def generate_decline_transcription(self, case_type: str) -> str:
        """Generate a transcription for a case that should be declined using OpenAI"""
        client_info = self.generate_personal_info()
        incident_date = (datetime.now() - timedelta(days=random.randint(60, 800))).strftime("%B %d, %Y")
        
        prompt = f"""Based on the following example for a law firm intake call that should be DECLINED, create a new realistic transcription for a {case_type.replace('_', ' ')} case.

EXAMPLE:
{self.base_decline_transcription}

REQUIREMENTS:
- Change the client name to: {client_info['full_name']}
- Change the phone to: {client_info['phone']}
- Change the email to: {client_info['email']}
- Change the incident date to: {incident_date}
- Adapt the case details to be specific to a {case_type.replace('_', ' ')} case
- Keep the same conversation structure and professional tone
- Make the conversation natural and realistic
- Keep the same Speaker 0/Speaker 1 format

Factors to consider for accepting or declining a case could include potential settlement value, likelihood of a settlement, severity of injuries sustained etc.

Generate only the transcription dialogue for a case which should be DECLINED, no additional text."""

        try:
            response = self.openai_client.chat.completions.create(
                model="o3",
                messages=[
                    {"role": "system", "content": "You are an expert at creating realistic law firm intake call transcriptions. Generate only the dialogue in the exact format requested."},
                    {"role": "user", "content": prompt}
                ],
                temperature=1
            )
            
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"Error generating decline transcription: {e}")
            # Fallback to template-based generation
            return self._fallback_decline_transcription(case_type, client_info, incident_date, reason)

    def generate_transcriptions(self, num_transcriptions: int = 20) -> None:
        """Generate the specified number of transcriptions, half accepted and half declined"""
        if not os.path.exists('transcriptions'):
            os.makedirs('transcriptions')
        
        # Create separate folders for accept and decline cases
        accept_dir = 'transcriptions/accept'
        decline_dir = 'transcriptions/decline'
        
        if not os.path.exists(accept_dir):
            os.makedirs(accept_dir)
        if not os.path.exists(decline_dir):
            os.makedirs(decline_dir)
        
        num_accept = num_transcriptions // 2
        num_decline = num_transcriptions - num_accept
        
        # Generate accepted cases
        for i in range(num_accept):
            case_type = random.choice(self.case_types)
            print(f"Generating accepted case {i+1}/{num_accept}: {case_type}")
            transcription = self.generate_accept_transcription(case_type)
            
            filename = f"{accept_dir}/{i+1:02d}_{case_type}.txt"
            with open(filename, 'w') as f:
                f.write(transcription)
            print(f"✓ Generated accepted case: {filename}")
        
        # Generate declined cases
        for i in range(num_decline):
            case_type = random.choice(self.case_types)
            print(f"Generating declined case {i+1}/{num_decline}: {case_type}")
            transcription = self.generate_decline_transcription(case_type)
            
            filename = f"{decline_dir}/{i+1:02d}_{case_type}.txt"
            with open(filename, 'w') as f:
                f.write(transcription)
            print(f"✓ Generated declined case: {filename}")
        
        print(f"\nGenerated {num_transcriptions} total transcriptions:")
        print(f"- {num_accept} cases to accept (in {accept_dir}/)")
        print(f"- {num_decline} cases to decline (in {decline_dir}/)")

def main():
    """Main function to run the transcription generator"""
    print("Law Firm Intake Transcription Generator with OpenAI")
    print("=" * 60)
    
    # Check for OpenAI API key
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("⚠️  OPENAI_API_KEY environment variable not found.")
        print("Please set your OpenAI API key:")
        print("export OPENAI_API_KEY='your-api-key-here'")
        return

    generator = TranscriptionGenerator()
    
    # Generate 20 transcriptions by default (10 accept, 10 decline)
    num_transcriptions = 20
    
    print(f"\nGenerating {num_transcriptions} law firm intake transcriptions...")
    print("=" * 60)
    
    generator.generate_transcriptions(num_transcriptions)
      

if __name__ == "__main__":
    main()
