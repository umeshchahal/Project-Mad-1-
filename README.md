# Project-Mad-1-

7  vedio for the Project 

Project: Vehicle Parking App (MAD-I)

The project is divided into 0th milestone, Core Requirements (6 Milestones ) and Recommended Functionalities & Optional Enhancements (6 Milestones ).
All core milestones can be completed in any order. 
Recommended and optional enhancements should only be started after the core milestones are done.
Each milestone includes a Git commit message. When completed, use the provided commit message and push your updates to GitHub.

Milestone 0: GitHub Repository Setup (Mandatory)
✅ Expected Time: 1 day
📊 Completion Progress: 5%

Create a private GitHub repository.
Add a README.md with a short project description.
Set up .gitignore to exclude unnecessary files, if required. ( not compulsory)
Commit and push the initial setup to the repository.
Refer to the git tracker document to add MADI-cs2003 as your collaborator, so that we can track your project.
Github Adding Collaborator Video: Adding Github Collaborator using VSCode and WSL
Git Commit Message: Milestone-0 VP-MAD-1


Core Requirements (6 Milestones)
Milestone: Database Models and Schema Setup
✅ Expected Time: 5-7 days
📊 Completion Progress: 18%

Create models for User, Admin (predefined), Parking Lot, Parking Spot, Reservation.
Establish relationships between tables.
Ensure the database is programmatically created through a python script/file.
Git Commit Message: Milestone-VP DB-Relationship


Milestone: Authentication and Role-Based Access
✅ Expected Time: 5 days
📊 Completion Progress: 10%

Implement User registration and login with required fields (username (email), password, full name, etc.).
Create an Admin login (Admin is predefined, no registration allowed).
Redirect to role-specific dashboards after login.
Git Commit Message: Milestone-VP Auth-RBAC


Milestone: Admin Dashboard and Lot/Spot Management
✅ Expected Time: 7-9 days
📊 Completion Progress: 23%

Admin functionalities:

Create/edit/delete parking lots.
View parking lot details and spot status.
Automatically create parking spots based on the maximum capacity of the lot.
View parking spots details.
Admin should see a list of all users and their details. (username, spot used etc.)
Git Commit Message: Milestone-VP Admin-Dashboard-Management


Milestone: User Dashboard and Reservation/Parking System
✅ Expected Time: 7 days
📊 Completion Progress: 17%

User functionalities:

View available parking lots.
Auto-allocation/Reservation of the first available spot.
Occupy a spot (update status - note timestamp)
Release a spot (update status - note timestamp).
Track timestamps for reservation and View parking history.
Git Commit Message: Milestone-VP User-Dashboard-Management


Milestone: Reservation/Parking History and Summary
✅ Expected Time: 5 days
📊 Completion Progress: 12%

Store and display reservation history for each user.
Show duration of each parking.
Admin view of all parking records.
Git Commit Message: Milestone-VP Summary-Users-Admin


Milestone: Slot Time Calculation and Parking Cost
✅ Expected Time: 4 days
📊 Completion Progress: 15%

Calculate total cost based on time difference and lot price per unit time.
Store and display parking cost in summary.
Git Commit Message: Milestone-VP Cost-Calculation


Recommended/Optional Enhancements  (6 Milestones)
Milestone: Search functionality for Admin
✅ Expected Time: 2 days

Create a field in the admin dashboard that allows the admin to search for a user, spot etc. to see if a spot is vacant or occupied.
Git Commit Message: Milestone-VP Search-Implemented


Milestone: API Integration
✅ Expected Time: 7 days

Create JSON-based APIs for lots, spots, and reservations.
Optional: Use Flask-Restful or manual controllers.
Git Commit Message: Milestone-VP Created-API


Milestone: Charts and Visualization
✅ Expected Time: 5 days

Use Chart.js or similar for showing user parking history and admin summaries.
Git Commit Message: Milestone-VP Charts


Milestone: Frontend and Backend Validation
✅ Expected Time: 5 days

Add form validation using HTML5 or JS.
Add backend validations in Flask routes.
Git Commit Message: Milestone-VP Validation


Milestone: Responsive UI and Styling
✅ Expected Time: 5 days

Add styling using Bootstrap.
Ensure mobile/tablet/pc responsiveness.
Git Commit Message: Milestone-VP Responsive-UI


Milestone: Flask Login Integration and Security
✅ Expected Time: 5-7 days

Integrate Flask-Login or Flask-Security.
Restrict routes and protect sessions.
Git Commit Message: Milestone-VP Flask-Integration


Final Submission
Milestone: Final Project Submission
✅ Expected Time: 2 days
📊 After, Completion Progress: 100%

Submit ZIP with code + 3-5 page report.
Submit a 3-10 minute demo video (Google Drive with access to anyone with the link).
Include a video presentation link in your pdf report.
Include a declaration of percentage of AI used in your app, in the pdf report ( if used.)
Git Commit Message: Milestone-VP Final-Submission


Tracking Progress
To track progress, you should:

Use Git commits for each milestone.
Test functionality after completing each milestone.
Log issues encountered and their resolutions in a README.md or GitHub Issues section.
Timeline Overview
Project Completion Overview
Milestone

Average Time Estimate

Split (%)

Progress (%)

GitHub Setup

1 day

5%

5%

Database Setup

5-7 days

18%

23%

Authentication

5 days

10%

33%

Admin Dashboard

7-9 days

23%

56%

User Dashboard

7 days

17%

73%

Parking History

5 days

12%

85%

Slot Calculation/Cost

4 days

15%

100%


Extra Work Overview
Milestone

Average Time Estimate

Search

2 days

API Integration

7 days

Charts and Visualization

5 days

Frontend and Backend Validation

5 days

Responsive UI and Styling

5 days

Flask Login Integration and Security

5-7 days

Final Submission Overview
Milestone

Average Time Estimate

Final Project Submission Details

2 days

