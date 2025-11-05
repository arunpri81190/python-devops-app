🛠️ Python DevOps App with CI/CD Pipeline
🚀 Overview
This project demonstrates a complete CI/CD pipeline using GitHub, Jenkins, Docker, and a Flask web app. Every code push to GitHub automatically triggers Jenkins to rebuild and redeploy the Docker container, serving the latest version of the app.
🔗 Tech Stack
•	GitHub – Source code repository
•	Jenkins – CI/CD automation
•	Docker – Containerization
•	Flask – Python web framework
•	Ngrok – Public tunnel for local Jenkins
•  🔄 CI/CD Workflow
graph TD 
A[GitHub Push] --> B[GitHub Webhook] 
B --> C[Jenkins Job Triggered] 
C --> D[Pull Latest Code] 
D --> E[Pull Docker Image] 
E --> F[Stop & Remove Old Container] 
F --> G[Run New Container] 
G --> H[Flask App Live]
 
📦 Docker Build Steps
docker pull arun3511/python-devops-app:latest docker stop python-devops-app || true docker rm python-devops-app || true docker run -d -p 5000:5000 --name python-devops-app arun3511/python-devops-app:latest 

🌐 Webhook Setup
•	Ngrok URL: https://wapperjawed-adriana-bronzelike.ngrok-free.dev
•	Payload URL: https://wapperjawed-adriana-bronzelike.ngrok-free.dev/github-webhook/
•	Content type: application/json
•	Trigger: Push events only
✅ Output Confirmation
•	Browser: http://localhost:5000
•	Expected Message: Webhook initialized: Jenkins is ready to build on push!, Assessment completed!!!
✅ Webhook initialized: Jenkins is ready to build on push! 
•	Jenkins Console Log:
Flask app starting... GitHub webhook initialized — waiting for push events... 
📸 Screenshots (Add these to your repo)
•	Jenkins build console
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/708cac82-dc2e-480a-878d-ec6db844392a" />

•	GitHub webhook settings
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/43047401-298b-4fd2-8057-f7ee9e2a9fcb" />

•	Flask app in browser
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/8fae8111-5e4d-46c6-ae70-e0aabf9c9b7f" />

🧠 What I Learned
•	Setting up Jenkins for GitHub integration
•	Automating Docker container lifecycle
•	Using webhooks for real-time CI/CD
•	Debugging branch and build errors
•	Documenting and visualizing DevOps pipelines
