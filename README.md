# Pushyanth Damarapati — Portfolio

A responsive, dependency-free portfolio for GitHub Pages. Six project summaries reflect the latest local evidence for each project, including release candidates, evaluation results, and known limits. No paid hosting, analytics, API, custom domain, or external fonts are required to view the site.

## Preview

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Open http://127.0.0.1:8000. The committed `index.html` also opens directly in a browser.

## Update content

Edit `site.json`, then regenerate the page:

```sh
python3 scripts/build.py
```

The `focus` line describes the portfolio's engineering topics; it can be replaced with your preferred professional title. The current Leidos affiliation is shown without an inferred job title. Experience and education can be expanded when the resume is supplied. Optional `email` and `linkedin` fields add contact links when populated.

## Add the resume

1. Save your PDF as `assets/resume.pdf`.
2. Set `"resume": "assets/resume.pdf"` in `site.json`.
3. Run `python3 scripts/build.py`, then commit and push.

The resume placeholder becomes a working download link. Until then, no missing PDF link is rendered.

## Publish free on GitHub Pages

Use a public repository named `pushyanthd.github.io`. Push this directory to its `main` branch. In **Settings → Pages**, select **Deploy from a branch**, **main**, and **/(root)**, then save. The site will be at https://pushyanthd.github.io/ when GitHub finishes deployment. Publishing from the branch needs no custom workflow or paid service.

GitHub Pages documentation: https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site

## Assets and content

`assets/workbench.png` is a screenshot from the document intelligence repository, showing recorded OCR and a fictional development invoice. It illustrates the interface; it is not a live extraction or review-performance measurement. Project links point to source repositories and their engineering documentation. Project results and experimental limits are preserved in the expandable engineering details.
