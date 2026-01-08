from django.conf import settings
from django.http import HttpResponse, Http404
from django.shortcuts import render

PROJECTS = [
    {
        "slug": "aws-django-deployment",
        "title": "AWS Django deployment baseline",
        "summary": "A small but carefully thought-out production setup for a personal website, focused on reliability rather than complexity.",
        "tags": ["AWS", "Django", "Nginx", "Gunicorn", "TLS", "Linux"],
        "problem": "I wanted to deploy my own website with sensible production defaults—HTTPS, predictable behavior, and low operational overhead—without overengineering.",
        "approach": "Configured Gunicorn behind Nginx, handled static files correctly, added HTTPS with certificates, and wired everything together using systemd. Set up GitHub Actions to make deployments repeatable and reduce friction when iterating.",
        "validation": "Manually tested reverse proxy behavior, HTTPS routing, static permissions, and restart behavior after failures using curl and browser-based checks.",
        "outcome": "A stable and maintainable deployment baseline that I now use as the foundation for my personal site and future projects."
    },
    {
        "slug": "data-driven-tooling",
        "title": "Internal research knowledge platform",
        "summary": "A centralized web-based tool to help researchers organize papers, models, and ideas in one place.",
        "tags": ["Python", "FastAPI", "Vue.js", "JWT", "SQLite"],
        "problem": "Researchers lacked a simple way to keep track of papers, models, and open questions across different projects and teams.",
        "approach": "Built a modular web application with a clear entity structure and tree-based navigation. Designed and implemented authentication from scratch using JWT access and refresh tokens, and exposed async APIs using FastAPI.",
        "validation": "Tested core flows manually and through sanity checks to avoid silent failures, especially around authentication and data consistency.",
        "outcome": "A working internal prototype that made it easier for researchers to find and relate their own tools and knowledge."
    },
    {
        "slug": "computer-vision",
        "title": "Computer vision model deployment (internship project)",
        "summary": "End-to-end deployment of a computer vision classification model during an applied AI internship.",
        "tags": ["Computer Vision", "Azure", "Databricks", "Model Deployment"],
        "problem": "A manufacturing use case required detecting defective screws using camera footage.",
        "approach": "Trained and validated a classification model provided through Azure ML and deployed it to edge devices using Azure tooling and agents.",
        "validation": "Evaluated the model using real footage from the production environment to verify correct behavior outside of static test data.",
        "outcome": "A deployed model that demonstrated how computer vision could reduce manual quality assurance effort."
    },
    {
        "slug": "time-series-analysis",
        "title": "Time series analysis and forecasting",
        "summary": "Hands-on implementation of classical time series models as part of advanced coursework.",
        "tags": ["Time Series", "Statistics", "Python", "ARIMA"],
        "problem": "Understand how classical time series models behave in practice, beyond theoretical definitions.",
        "approach": "Implemented AR, MA, ARIMA, and ARIMAX models from scratch, including stepwise model selection and diagnostics for heteroskedasticity.",
        "validation": "Compared model behavior across datasets and checked assumptions using residual analysis and standard statistical tests.",
        "outcome": "A much more grounded understanding of time series modeling and its limitations in real data."
    },
    {
        "slug": "computational-data-analysis",
        "title": "Computational data analysis projects",
        "summary": "Applied statistical modeling and unsupervised learning to real datasets as part of computational data analysis coursework.",
        "tags": ["Regression", "Regularization", "GMM", "Statistics", "Python"],
        "problem": "Explore how different statistical models behave when applied to noisy, real-world data.",
        "approach": "Built linear regression models with L1 and L2 regularization and tuned hyperparameters via grid search. In a separate project, applied Gaussian Mixture Models to physiological signals such as heart rate and blood pressure to explore relationships with emotional states.",
        "validation": "Evaluated model behavior through error metrics, parameter sensitivity, and qualitative inspection of learned clusters.",
        "outcome": "Practical experience translating statistical theory into working models and interpreting results with appropriate caution."
    },
    {
        "slug": "thesis-project",
        "title": "Learning Local Gibbs States from Noisy Shallow Quantum Circuits",
        "summary": "Computational research project exploring how noise affects thermal quantum states prepared by shallow circuits.",
        "tags": ["Python", "Quimb", "Tensor Networks", "Statistics"],
        "problem": "Understand how different noise mechanisms impact the structure of Gibbs states generated by local, shallow quantum circuits.",
        "approach": "Used tensor network methods via the Quimb library to simulate noisy quantum circuits and study their output states. Focused primarily on depolarizing noise, with discussion of amplitude damping.",
        "validation": "While full validation was not possible, I performed extensive sanity checks and consistency comparisons to build confidence in the observed behavior.",
        "outcome": "A 40-page master’s thesis and an original conjecture relating noise strength to thermal state structure."
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
