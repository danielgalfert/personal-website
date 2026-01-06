from django.conf import settings
from django.http import HttpResponse, Http404
from django.shortcuts import render

# Simple in-memory data (replace with DB later if you want)
PROJECTS = [
    {
        "slug": "aws-django-deployment",
        "title": "AWS Django deployment baseline",
        "summary": "A production-ready setup: Gunicorn, Nginx, TLS, static handling, and operational stability on a small instance.",
        "tags": ["AWS", "Django", "Nginx", "Gunicorn", "TLS"],
        "problem": "Deploy a personal website with strong defaults: HTTPS, stable process management, correct static handling, and minimal operational overhead.",
        "approach": "Configured Gunicorn behind Nginx, hardened static serving, added HTTPS, and ensured restart/recovery behavior via systemd. Kept the stack simple and observable.",
        "validation": "Verified reverse proxy behavior, local/remote curl checks, correct static permissions, and consistent routing over HTTPS.",
        "outcome": "A stable, maintainable deployment baseline suitable for extension (projects, CV, content) without re-architecting."
    },
    {
        "slug": "data-driven-tooling",
        "title": "Research & analytical tooling",
        "summary": "Python-based tooling supporting data-intensive workflows with an emphasis on reproducibility, validation discipline, and handover-ready documentation.",
        "tags": ["Python", "Tooling", "Reproducibility"],
        "problem": "Support complex workflows where correctness and clarity matter, and where results must be reproducible and explainable.",
        "approach": "Built modular analysis utilities and automation scripts with clear interfaces, explicit assumptions, and documented usage patterns.",
        "validation": "Reproducible runs, sanity checks, and lightweight tests for critical components; focused on avoiding silent failure modes.",
        "outcome": "A practical toolbox that improves iteration speed while maintaining rigor and traceability."
    },
    {
        "slug": "model-evaluation-discipline",
        "title": "Evaluation discipline for modeling systems",
        "summary": "A pragmatic framework for validating models and analytics systems: assumptions, baselines, sensitivity checks, and measurable claims.",
        "tags": ["Modeling", "Validation", "Statistics"],
        "problem": "Avoid over-claiming results and ensure improvements are real, not artifacts of leakage, noise, or poor baselines.",
        "approach": "Defined evaluation steps: baselines, ablations, sensitivity analysis, and explicit uncertainty where appropriate.",
        "validation": "Cross-checks across datasets/splits, stress tests of assumptions, and failure-mode exploration.",
        "outcome": "More trustworthy conclusions and systems that perform reliably under real-world variance."
    },
]

def home(request):
    featured_projects = PROJECTS[:3]
    ctx = {
        "featured_projects": featured_projects,
        "seo": {
            "title": "Daniel G. Alfert — Data-driven systems and engineering",
            "description": "Generalist software engineer with quantitative depth. Backend, data-driven systems, modeling, and production reliability.",
            "canonical": f"{settings.SITE_URL}/",
        },
    }
    return render(request, "home.html", ctx)

def about(request):
    return render(request, "about.html", {
        "seo": {
            "title": "About — Daniel G. Alfert",
            "description": "Background and approach: engineering discipline, quantitative reasoning, and pragmatic rigor.",
            "canonical": f"{settings.SITE_URL}/about/",
        }
    })

def contact(request):
    return render(request, "contact.html", {
        "seo": {
            "title": "Contact — Daniel G. Alfert",
            "description": "Contact details and professional profiles.",
            "canonical": f"{settings.SITE_URL}/contact/",
        }
    })

def cv(request):
    return render(request, "cv.html", {
        "seo": {
            "title": "CV — Daniel G. Alfert",
            "description": "Curriculum Vitae (PDF) and professional overview.",
            "canonical": f"{settings.SITE_URL}/cv/",
        }
    })

def projects_index(request):
    return render(request, "projects/index.html", {
        "projects": PROJECTS,
        "seo": {
            "title": "Projects — Daniel G. Alfert",
            "description": "Case studies and proof of work: objective, approach, validation, and outcome.",
            "canonical": f"{settings.SITE_URL}/projects/",
        }
    })

def project_detail(request, slug: str):
    project = next((p for p in PROJECTS if p["slug"] == slug), None)
    if not project:
        raise Http404("Project not found")

    return render(request, "projects/detail.html", {
        "project": project,
        "seo": {
            "title": f"{project['title']} — Daniel G. Alfert",
            "description": project["summary"],
            "canonical": f"{settings.SITE_URL}/projects/{slug}/",
        }
    })

def robots_txt(request):
    lines = [
        "User-agent: *",
        "Allow: /",
        f"Sitemap: {settings.SITE_URL}/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
