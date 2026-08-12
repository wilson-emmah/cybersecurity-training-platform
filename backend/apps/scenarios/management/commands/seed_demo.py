from django.core.management.base import BaseCommand
from apps.scenarios.models import Scenario
from apps.gamification.models import Badge

SCENARIOS = [
    {
        "title": "Suspicious Invoice Email", "category": "phishing", "difficulty": "beginner",
        "description": "Inspect a simulated invoice email and identify whether it is safe.",
        "points": 20, "content": {
            "from": "billing@paypa1-security.example",
            "subject": "Urgent: Payment verification required",
            "body": "Your account will be suspended today. Click the link below to verify your payment.",
            "options": [
                {"id": "report", "label": "Report as phishing"},
                {"id": "open", "label": "Open the link"},
                {"id": "reply", "label": "Reply with account details"}],
            "correct_answer": "report",
            "explanation": "The sender domain is suspicious and the message creates urgency to pressure the recipient."
        }
    },
    {
        "title": "Suspicious Login URL", "category": "url", "difficulty": "beginner",
        "description": "Choose the safest response to a suspicious login link.",
        "points": 15, "content": {
            "url": "https://secure-login.example-account.verify.example",
            "options": [
                {"id": "visit", "label": "Visit the URL"},
                {"id": "ignore", "label": "Ignore/report it and open the official site manually"},
                {"id": "share", "label": "Share it with a friend"}],
            "correct_answer": "ignore",
            "explanation": "The URL contains deceptive subdomains. Use the known official website instead."
        }
    },
    {
        "title": "Password Security Check", "category": "password", "difficulty": "beginner",
        "description": "Select the strongest password practice.",
        "points": 10, "content": {
            "options": [
                {"id": "reuse", "label": "Use the same password everywhere"},
                {"id": "short", "label": "Use a short memorable password"},
                {"id": "unique", "label": "Use a long unique password with MFA"}],
            "correct_answer": "unique",
            "explanation": "Long unique passwords combined with multi-factor authentication reduce account compromise risk."
        }
    },
    {
        "title": "Unexpected Attachment", "category": "malware", "difficulty": "intermediate",
        "description": "A simulated coworker message contains an unexpected executable attachment.",
        "points": 25, "content": {
            "from": "colleague@example.com", "attachment": "Invoice_2026.exe",
            "body": "Please open this invoice immediately.",
            "options": [
                {"id": "open", "label": "Open the attachment"},
                {"id": "verify", "label": "Verify with the sender through a separate trusted channel"},
                {"id": "forward", "label": "Forward it to colleagues"}],
            "correct_answer": "verify",
            "explanation": "Unexpected executable attachments should be verified before opening."
        }
    },
    {
        "title": "Impersonated IT Support", "category": "social", "difficulty": "intermediate",
        "description": "A simulated caller claims to be IT support and requests your password.",
        "points": 25, "content": {
            "options": [
                {"id": "give", "label": "Give the password"},
                {"id": "verify", "label": "End the conversation and contact IT using the official support channel"},
                {"id": "ignore", "label": "Continue chatting but do not share anything"}],
            "correct_answer": "verify",
            "explanation": "Legitimate support should not require you to disclose your password. Verify requests independently."
        }
    }
]

BADGES = [
    ("First Steps", "Complete enough training to begin your cybersecurity journey.", "🚀", 10),
    ("Phishing Hunter", "Earn 50 points.", "🎣", 50),
    ("Cyber Defender", "Earn 100 points.", "🛡️", 100),
    ("Security Expert", "Earn 250 points.", "🏆", 250),
]

class Command(BaseCommand):
    help = "Load safe demo scenarios and badges"

    def handle(self, *args, **kwargs):
        for item in SCENARIOS:
            Scenario.objects.update_or_create(title=item["title"], defaults=item)
        for name, description, icon, required_points in BADGES:
            Badge.objects.update_or_create(name=name, defaults={
                "description": description,
                "icon": icon,
                "required_points": required_points
            })
        self.stdout.write(self.style.SUCCESS("Demo scenarios and badges loaded."))
