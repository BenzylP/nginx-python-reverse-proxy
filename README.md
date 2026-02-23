# Nginx Reverse Proxy with a Python/Flask API
## Project Description
I upgraded my standard Linux web server into a dynamic, self-healing web application. Instead of just serving a static HTML page, I configured Nginx to act as a Reverse Proxy. It catches incoming web traffic and securely routes it to a custom Python backend application running locally on the server.

## What I Built & Learned
* Backend API (Python/Flask): I wrote a lightweight application that calculates and serves live server data (current date and time). It runs safely behind the firewall on Port 5000.
* Reverse Proxy (Nginx): I reconfigured the default Nginx routing rules. Now, when a user visits the main IP address on Port 80, Nginx intercepts the request, asks the Python app for the live data, and serves it back to the user seamlessly.
* Process Management (Systemd): To make the app production-ready, I wrote a custom Linux Systemd service (myapi.service). The operating system now runs my Python app entirely in the background and automatically restarts it if the server crashes or reboots.

## The Architecture
User Request -> Port 80 (Nginx Firewall/Proxy) -> Localhost Port 5000 (Python App) -> Response to User
