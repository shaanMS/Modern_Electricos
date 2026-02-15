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

- **Secure Instance Switching & Binding**  
  Signed tokens generated on load (`secureInstanceTokenServices.py`)  
  httponly cookie (`app_instance`) with SameSite=Lax, 24-hour expiry  
  Constant-time comparison for validation  
  Cookie + token prevents cross-instance data leakage

- **Dynamic Homepage Rendering**  
  `home/views.py` → `home_page()` loads default instance from settings.APP_INSTANCE_ID  
  `instance_page(franchise_uuid)` for switching  
  `@cache_page(300)` + conditional views (ETag + Last-Modified) for performance  
  Services loop, ads section, enquiry form integration

- **Professional Enquiry / Quote System**  
  `enquiry/models.py` → `Enquiry` model with UUID PK, request_hash (anti-duplicate UniqueConstraint)  
  Multi-select services (JSONField), priority, budget range, preferred date, project details  
  Logs: IP, User-Agent, Referer, bound instance_id  
  GIN indexes on searchable fields for fast queries

- **Custom Django Admin**  
  Enhanced `AppInstance` admin: list display (title, tagline, version, last updated, show_ad_section)  
  Filters, search, actions ready  
  Dark/teal theme compatible

- **Frontend Basics**  
  Responsive template (`templates/index.html`)  
  Emergency floating button (24/7 phone)  
  Counters (e.g. 2567 projects, 20 years)  
  Google Fonts + icons integration  
  Enquiry form with CSRF + submit handling

- **Performance & Modern Practices**  
  Conditional view synchronizer  
  Async helpers (unused yet)  
  CSP middleware foundation  
  PostgreSQL JSONB + GIN for dynamic data

<grok-card data-id="524131" data-type="image_card" data-plain-type="render_searched_image"  data-arg-size="LARGE" ></grok-card>



<grok-card data-id="81f5ca" data-type="image_card" data-plain-type="render_searched_image"  data-arg-size="LARGE" ></grok-card>


*(Homepage hero examples – electrician working, emergency CTA, modern layout matching PowerPro style)*

<grok-card data-id="7237c2" data-type="image_card" data-plain-type="render_searched_image"  data-arg-size="LARGE" ></grok-card>



<grok-card data-id="683dad" data-type="image_card" data-plain-type="render_searched_image"  data-arg-size="LARGE" ></grok-card>


*(Enquiry form inspirations – clean fields, service select, priority, budget, date picker)*

<grok-card data-id="50230a" data-type="image_card" data-plain-type="render_searched_image"  data-arg-size="LARGE" ></grok-card>



<grok-card data-id="e7f728" data-type="image_card" data-plain-type="render_searched_image"  data-arg-size="LARGE" ></grok-card>


*(Django admin custom views – list of instances, filters, teal/dark theme)*

## 📸 Current Screenshots & Visuals (From DevTools & Local Runs)

- Homepage: PowerPro branding, hero, counters, emergency button, services overview  
- Enquiry Form: Full quote request with multi-select, priority, budget dropdown  
- Admin Panel: App Instances list with custom columns & filters  
- Network Tab: `app_instance` cookie set via signed token (httponly, secure flow)  
- Electrical Service Imagery: Technician repairing panels, EV charger installs, solar setups

<grok-card data-id="508943" data-type="image_card" data-plain-type="render_searched_image"  data-arg-size="LARGE" ></grok-card>


*(DevTools cookie/token flow example – secure binding)*

<grok-card data-id="0ba5f8" data-type="image_card" data-plain-type="render_searched_image"  data-arg-size="LARGE" ></grok-card>



<grok-card data-id="af9857" data-type="image_card" data-plain-type="render_searched_image"  data-arg-size="LARGE" ></grok-card>


*(Professional electrical work – wiring, EV charger, safety focus)*

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

# Setup DB (local PostgreSQL or sqlite for quick test)
python manage.py migrate
python manage.py createsuperuser

# Run (your port from screenshots)
python manage.py runserver 0.0.0.0:9996
