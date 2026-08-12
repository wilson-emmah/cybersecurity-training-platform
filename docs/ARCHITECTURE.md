# System Architecture

```text
Browser / Next.js
       |
       | REST + JWT
       v
Django REST Framework
       |
       +---- Accounts
       +---- Scenario Engine
       +---- Gamification
       +---- Reports
       +---- Notifications
       |
       v
PostgreSQL
```

## Safe simulation model

The system stores simulated scenario content as JSON. A user chooses one of the predefined responses. The backend compares the selected response with the scenario's expected response, records the attempt and updates the user's score.

No real-world phishing delivery, malware execution, credential harvesting or attack traffic is required.

## User flow

Register → Login → Dashboard → Training → Scenario → Decision → Backend evaluation → Score → Badge → Progress → Leaderboard

## Admin flow

Django superuser/admin role → Admin dashboard → Scenario library → Reports → User performance
