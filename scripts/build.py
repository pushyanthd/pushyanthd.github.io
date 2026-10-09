"""Generate a dependency-free portfolio from site.json and template.html."""
import html
import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "site.json").read_text())
esc = lambda value: html.escape(str(value), quote=True)
github = "https://github.com/" + data["github"]

def project_html(project, index):
    url = github + "/" + project["slug"]
    tags = "".join(f'<li>{esc(tag)}</li>' for tag in project["tags"])
    feature = project.get("featured", False)
    image = '''<figure class="project-image"><img src="assets/workbench.png" width="1440" height="1013" loading="lazy" alt="Document review workspace showing an invoice beside evidence-linked extracted fields"><figcaption>Recorded OCR demo on a fictional invoice.</figcaption></figure>''' if feature else ""
    return f'''<article class="project{' featured' if feature else ''}">
      <div class="project-copy"><div class="project-top"><span class="project-number">{index:02d}</span><span class="eyebrow">{esc(project['category'])}</span></div>
      <h3>{esc(project['title'])}</h3><p>{esc(project['description'])}</p>
      <ul class="tags" aria-label="Technologies">{tags}</ul>
      <div class="project-links"><a href="{esc(url)}">View repository</a><a href="{esc(url)}/blob/main/{esc(project['caseStudy'])}">Read project notes</a></div>
      <details><summary>Engineering details</summary><p>{esc(project['detail'])}</p><span class="project-status">{esc(project['status'])}</span></details></div>{image}
    </article>'''

if data["resume"]:
    resume_path = Path(data["resume"])
    if resume_path.is_absolute() or ".." in resume_path.parts or resume_path.suffix.lower() != ".pdf" or not (ROOT / resume_path).is_file():
        raise ValueError("resume must point to an existing PDF inside this portfolio")
    resume_action = f'<a class="button primary" href="{esc(data["resume"])}" download>Download resume</a>'
    resume_copy = "A closer look at my experience, education, and technical background."
    resume_status = "PDF resume"
else:
    resume_action = '<span class="resume-pending">PDF coming soon</span>'
    resume_copy = "My resume will be available here soon. In the meantime, explore my projects and engineering notes."
    resume_status = "Coming soon"

socials = f'<a class="button primary" href="{esc(github)}">Connect on GitHub</a>'
if data.get("linkedin"):
    parsed = urlparse(data["linkedin"])
    if parsed.scheme != "https" or parsed.hostname not in {"linkedin.com", "www.linkedin.com"}:
        raise ValueError("linkedin must be an HTTPS LinkedIn profile URL")
    socials += f'<a class="button secondary" href="{esc(data["linkedin"])}">LinkedIn</a>'
if data.get("email"):
    socials += f'<a class="button secondary" href="mailto:{esc(data["email"])}">Email me</a>'

values = {key: esc(data[key]) for key in ["name", "initials", "focus", "headline", "intro", "about"]}
values.update(github=esc(github), github_username=esc(data["github"]),
              linkedin=esc(data.get("linkedin", "https://www.linkedin.com/in/pushyanthd")),
              projects="\n".join(project_html(p, i) for i, p in enumerate(data["projects"], 1)),
              resume_action=resume_action, resume_copy=esc(resume_copy), resume_status=esc(resume_status), socials=socials,
              project_count=str(len(data["projects"])))
page = (ROOT / "template.html").read_text()
for key, value in values.items():
    page = page.replace("{{" + key + "}}", value)
if "{{" in page:
    raise ValueError("Unresolved template placeholder")
(ROOT / "index.html").write_text(page)
print(f"Built index.html with {len(data['projects'])} projects")
