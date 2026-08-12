# Logical Database Schema

## Users
Django `auth_user`
- id
- username
- email
- password hash
- is_staff
- is_active

## user_profiles
- id
- user_id
- role
- points
- level
- training_streak
- last_training_date

## scenarios
- id
- title
- category
- difficulty
- description
- content (JSON)
- points
- active
- created_at
- updated_at

## training_attempts
- id
- user_id
- scenario_id
- selected_answer
- correct
- points_earned
- created_at

## badges
- id
- name
- description
- icon
- required_points

## user_badges
- id
- user_id
- badge_id
- awarded_at

## notifications
- id
- user_id
- title
- message
- read
- created_at
