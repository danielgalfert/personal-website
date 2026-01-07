from django.conf import settings
from django.http import HttpResponse, Http404
from django.shortcuts import render

PROJECTS = [
    {
        "slug": "aws-django-deployment",
        "title": "AWS Django deployment baseline",
        "summary": "A production-ready setup: Gunicorn, Nginx, TLS, static handling, and operational stability on a small instance.",
        "tags": ["AWS", "Django", "Nginx", "Gunicorn", "TLS"],
        "problem": "Deploy a personal website with strong defaults: HTTPS, and minimal operational overhead.",
        "approach": "Configured Gunicorn behind Nginx, set up Github Actions for easier incremental testing, hardened static serving, added HTTPS, and ensured restart/recovery behavior via systemd. Kept the stack simple and observable.",
        "validation": "Verified reverse proxy behavior, local/remote curl checks, correct static permissions, and consistent routing over HTTPS.",
        "outcome": "A stable, maintainable deployment baseline suitable for extension (projects, CV, content)."
    },
    {
        "slug": "data-driven-tooling",
        "title": "Research & analytical tooling",
        "summary": "Centralized web-based knowledge tool",
        "tags": ["Python", "FastAPI", "Vue.js"],
        "problem": "Researchers needed a tool to store papers, models, academically interesting questions etc.",
        "approach": "Built modular web-based tool with a tree structure navigation that related the different entity models",
        "validation": "Reproducible runs, sanity checks, and lightweight tests for critical components; focused on avoiding silent failure modes.",
        "outcome": "A practical tool that made researchers lives easier."
    },
    {
        "slug": "computer-vision",
        "title": "Deployment of computer vision model",
        "summary": "Deployed a computer vision model using Databricks and AzureDevOps.",
        "tags": ["Modeling", "Validation", "Azure", "Databricks"],
        "problem": "A company needed to detect whether their screws were defective.",
        "approach": "Designed, trained, validated and deployed a computer vision model.",
        "validation": "Tested the model with actual live footage.",
        "outcome": "A model that helped saved thousands of dollar in quality assurance."
    },
    {
        "slug": "thesis-project",
        "title": "Learning Local Gibbs States from Noisy Shallow Quantum Circuits",
        "summary": "Studying properties of certain quantum states and simulating them with tensor networks.",
        "tags": ["Numpy", "Scipy", "numpy", "statistics"],
        "problem": "Evaluate the properties of noisy quantum circuits.",
        "approach": "Used the tensor network library 'quimb' to approximate the outputs of said circuits and create a conjecture.",
        "validation": "Was not able to validate the conjecture, but found strong evidence.",
        "outcome": "Academic report of findings."
    },
]

def home(request):
    featured_projects = PROJECTS[:3]
    ctx = {
        "featured_projects": featured_projects,
        "seo": {
            "title": "Daniel G. Alfert",
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
