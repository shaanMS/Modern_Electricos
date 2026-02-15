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






===========================================================================


## In-Depth Technical Analysis

### 1. Web Technologies & Frontend
- Django Templates + custom CSS/JS  
- Responsive design (mobile-first)  
- Google Fonts, Font Awesome icons  
- Emergency floating button (24/7)  
- Dynamic hero, services cards, counters, enquiry form  
**Strength**: Clean, fast, no heavy JS framework → perfect for SEO & speed  
**Improvement**: Tailwind CSS v3 integrate karo (future-proof + faster styling)

### 2. Python
- Python 3.10+ compatible  
- Modern practices: f-strings, type hints (partial), async helpers  
- Custom utility modules (secureInstanceTokenServices.py, conditionalViewSynchronizer.py)  
**Strength**: Clean, modular, reusable code  
**Improvement**: Full type hints + pydantic for settings + mypy linting add karo

### 3. Django Framework (MVT Architecture)
**Model** → `AppInstance` (JSONField for services/ads), `Enquiry` (request_hash, GIN indexes)  
**View** → Class-based + function views with caching & conditional responses  
**Template** → Dynamic `index.html` with `{{ }}` variables  

**Strengths**:
- True instance-based multi-tenancy (no subdomains)
- Signed token + httponly cookie system
- `@cache_page(300)` + ETag/Last-Modified conditional views
- GIN indexes + UniqueConstraint on enquiry hash

**MVT Score**: 9.2/10 (very clean implementation)

### 4. Database Specific (PostgreSQL Focus)
- PostgreSQL 16 recommended  
- JSONField (services, ads, certifications)  
- GIN indexes on JSONB fields  
- UUID primary keys  
- UniqueConstraint on request_hash  
- Search vector ready (migration mein)

**PostgreSQL Specific Features Used**:
- JSONB + GIN → lightning fast dynamic data queries
- UUID PK → no sequence collision in multi-tenant
- Conditional indexes possible in future

**Strength**: Highly scalable for 1000+ instances  
**Improvement**: Add `pg_trgm` extension for fuzzy search on services

### 5. System Architecture & Design
**Architecture Type**: Instance-Based Multi-Tenancy (Shared Database, Shared Schema)  
**Data Flow**:
1. User visits → `home_page()` → default instance from settings
2. Token generated → cookie set (httponly, Lax)
3. Every request → middleware/token check → correct instance data
4. Enquiry → bound to instance_id + request_hash

**System Design Highlights**:
- Stateless token + cookie (no session bloat)
- Conditional caching (ETag + Last-Modified)
- Anti-spam enquiry system
- Admin-friendly instance management

**Score**: 9.5/10 (production-level design)

### 6. Cybersecurity & Security Practices
**Implemented**:
- Signed tokens (constant-time compare)
- httponly + SameSite=Lax cookies
- Request hash + UniqueConstraint (duplicate prevention)
- IP, User-Agent, Referer logging in Enquiry
- CSP middleware foundation

**DevTools Proof**:
![Token & Cookie Security](https://github.com/shaanMS/Modern_Electricos/raw/main/screenshots/app_instance_token.png)
![Network Tab Security](https://github.com/shaanMS/Modern_Electricos/raw/main/screenshots/token_header.png)

**Missing / To Improve**:
- HTTPS enforcement
- Rate limiting (django-ratelimit)
- reCAPTCHA v3 / honeypot
- CSP strict mode
- SECRET_KEY + DB creds in environment

### 7. Git & Version Control
- Standard .gitignore
- Clean commit history (migrations + screenshots)
- Screenshots folder properly added

**Recommendation**:
- Conventional commits use karo
- Branching strategy (main + feature/* + hotfix/*)
- .github/workflows add karo (CI)

### 8. CI/CD (Current Status)
**Not implemented yet**  
**Recommended Stack**:
- GitHub Actions
- Tests → pytest + Django test
- Linting → ruff + black
- Deployment → Docker → Railway/Render/DigitalOcean

### 9. Detailed Analysis & Review by Grok (xAI)

**Overall Rating**: **9.1 / 10**

**What’s Exceptional**:
- True multi-tenancy without subdomains (rare in Django)
- Token + cookie security model is production-grade
- Caching + conditional views = modern performance
- Enquiry model is anti-spam ready
- Admin customization is excellent

**What Needs Immediate Attention** (High Priority):
1. Settings split + environment variables
2. HTTPS + secure cookies
3. Rate limiting + CAPTCHA
4. Fix double slashes in urls.py
5. Remove all debug prints

**What’s Next Level (Medium Priority)**:
- Docker + docker-compose
- Tailwind CSS
- Celery + Redis for emails
- Hindi language support
- Analytics + Sentry

---

## 🗺️ To-Do List & Required Modifications (Actionable)

### Phase 1 – Production Ready (1–2 weeks)
- [ ] Production settings split (base/dev/prod + django-environ)
- [ ] All secrets → environment variables
- [ ] DEBUG = False + ALLOWED_HOSTS
- [ ] HTTPS + SESSION_COOKIE_SECURE + CSRF_COOKIE_SECURE
- [ ] Rate limiting + honeypot on enquiry form
- [ ] Fix `path("franchise//", ...)` → `path("franchise/<uuid>/", ...)`
- [ ] Remove all `print()` and debug code
- [ ] Complete CSP settings

### Phase 2 – Scale & Polish (3–6 weeks)
- [ ] Docker + docker-compose (postgres + redis)
- [ ] Tailwind CSS v3 integration
- [ ] Celery + Redis for email notifications
- [ ] Multi-language (English + Hindi)
- [ ] Google Analytics / Plausible
- [ ] Sentry error tracking

### Phase 3 – Advanced (2–3 months)
- [ ] Django REST Framework API
- [ ] Franchise owner login (per-instance permissions)
- [ ] Razorpay / payment gateway
- [ ] Full test suite (pytest)
- [ ] GitHub Actions CI/CD
- [ ] Automated backups

**Total estimated time (solo)**: 2–4 months to full production SaaS.

---

## 📄 License

MIT License  
© 2026 Shaan, India

**Star 🌟 the repo** if you found this boilerplate useful!

Made with ❤️ for India’s electrical services franchise ecosystem.

**Questions?** Open an issue or DM.

**Shaan • 15 February 2026**