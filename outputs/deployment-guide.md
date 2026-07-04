# HealthStat AI Deployment Guide

HealthStat AI is a static browser application. It does not require a backend server, database, API key, or build step.

## Recommended Deployment Option: Netlify

1. Create a GitHub repository for the project.
2. Upload the full project folder.
3. Sign in to Netlify.
4. Choose "Add new site" and connect the GitHub repository.
5. Set the publish directory to:

```text
outputs
```

6. Leave the build command empty.
7. Deploy the site.

The included `netlify.toml` file already tells Netlify to publish the `outputs` folder.

## Vercel Deployment

1. Create a GitHub repository for the project.
2. Upload the full project folder.
3. Sign in to Vercel.
4. Import the GitHub repository.
5. Use the default static project settings.
6. Deploy.

The included `vercel.json` routes the root URL to the main HealthStat AI HTML file.

## GitHub Pages Deployment

GitHub Pages usually serves from the repository root or a `/docs` folder. For GitHub Pages, use one of these approaches:

- Move the contents of `outputs` to the repository root, or
- Rename `outputs` to `docs`, then configure GitHub Pages to publish from `/docs`.

## Local Preview

Open this file directly in a browser:

```text
outputs/healthstat-ai-multidataset.html
```

Or open:

```text
outputs/index.html
```

## Deployment Checklist

- The home page shows the research and educational use disclaimer.
- The demo buttons load all four healthcare datasets.
- The model cards display validation metrics.
- The risk simulator returns a probability and explanation.
- The report page includes model validation notes.
- The README explains the limitations clearly.

## Suggested Portfolio Description

HealthStat AI is a static healthcare analytics platform that adapts to multiple healthcare datasets, detects target variables automatically, performs exploratory analysis, trains an in-browser logistic regression model, ranks risk factors, and generates validation-aware reports for educational and analytical use.
