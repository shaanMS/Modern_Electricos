# Modern Electricos ⚡

**Advanced Instance-Based Multi-Tenant Django SaaS Boilerplate for Electrical Services & Franchise Networks**  
**One codebase → Unlimited branded franchise websites** (e.g. PowerPro Lucknow, Spark Delhi, Volt Mumbai) — fully dynamic, secure, performant, and scalable.


Current version: Prototype → MVP-ready with production cleanup pending



[![Django 5.2](https://img.shields.io/badge/Django-5.2-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Status: In Development](https://img.shields.io/badge/Status-In%20Development-orange?style=for-the-badge)](https://github.com/shaanMS/Modern_Electricos)

## ✨ What Has Been Implemented (Done Features – Feb 2026)

- **Core Multi-Tenancy Architecture** (Instance-Based – No subdomains)  
  Single `AppInstance` model per franchise/city  
  Dynamic loading of title, hero subtitle, tagline, services (JSONField), ads carousel (JSON), certifications, project counters, contact info, business hours, show_ad_section toggle

![PowerPro Homepage Screenshot](https://github.com/shaanMS/Modern_Electricos/raw/main/screenshots/Screenshot%202026-02-15%20at%2013-56-58%20PowerPro%20Electrical%20Services%20Pvt.%20Ltd.%20Professional%20Electrical%20Solutions.png)  
*(Your live homepage demo: PowerPro branding, hero section, emergency CTA, counters, services overview)*

- **Secure Instance Switching & Binding**  
  Signed tokens generated on load (`secureInstanceTokenServices.py`)  
  httponly cookie (`app_instance`) with SameSite=Lax, 24-hour expiry  
  Constant-time comparison for validation

![App Instance Token Flow](https://github.com/shaanMS/Modern_Electricos/raw/main/screenshots/app_instance_token.png)  
![Token Header Debug](https://github.com/shaanMS/Modern_Electricos/raw/main/screenshots/token_header.png)  
*(Token generation & header debug views showing secure binding)*

- **Dynamic Homepage & Franchise Access**  
  `home/views.py` → Default + UUID-based switching  
  `@cache_page(300)` + conditional views (ETag + Last-Modified)

![Franchise Instance Access](https://github.com/shaanMS/Modern_Electricos/raw/main/screenshots/instance_based_franchise_access.png)  
*(Example of loading different franchise via UUID – custom branding applied)*

- **Professional Enquiry / Quote System**  
  `enquiry/models.py` → Anti-duplicate hash, GIN indexes, full logging

- **Custom Django Admin**  
  Enhanced list view for App Instances

![Admin Panel Instances List](https://github.com/shaanMS/Modern_Electricos/raw/main/screenshots/instances%20in%20admin%20panel.png)  
*(Your admin screen: Managing multiple PowerPro instances with filters & toggles)*

- **Performance & Debug Views**  
  Caching headers, developer options

![Debug View Headers & Caching](https://github.com/shaanMS/Modern_Electricos/raw/main/screenshots/debug%20view%20headers%20caching.png)  
![Developer Options Debug](https://github.com/shaanMS/Modern_Electricos/raw/main/screenshots/deveoper%20options%20debug%20views%20of%20app.png)  
*(Network/debug views showing caching, headers, and app instance cookie flow)*

## 🛠️ Tech Stack & Key Files

- Django 5.2  
- PostgreSQL (JSONB, GIN indexes, UUID)  
- Custom: Token signing, caching decorators, conditional views  
- Key locations:  
  - `home/appInstanceData.py` → AppInstance model  
  - `home/views.py` → Rendering + token logic  
  - `home/secureInstanceTokenServices.py` → Token utils  
  - `enquiry/models.py` → Anti-spam enquiry  
  - `templates/index.html` → Main dynamic page

## 🚀 Quick Local Setup

```bash
git clone https://github.com/shaanMS/Modern_Electricos.git
cd Modern_Electricos

# Virtualenv (Windows)
python -m venv venv
venv\Scripts\activate

pip install django psycopg2-binary

python manage.py migrate
python manage.py createsuperuser

<<<<<<< HEAD
python manage.py runserver 0.0.0.0:9996
=======
# Run (your port from screenshots)
python manage.py runserver 0.0.0.0:9996
>>>>>>> d7c04ac69f380df5dd5e8f0bc7fff5edbd1b8668
