# Lazy Dog Computing Website

This repository contains the full static website for Lazy Dog Computing.

## GitHub Pages deployment

### Option 1: Deploy from the repository root
1. Upload all files in this repository to the default branch.
2. In GitHub, open **Settings**.
3. Open **Pages**.
4. Under **Build and deployment**, choose:
   - **Source:** Deploy from a branch
   - **Branch:** main
   - **Folder:** / (root)
5. Save your changes.
6. Wait for GitHub Pages to publish the site.

### Option 2: Deploy using GitHub Actions
A workflow file is included in `.github/workflows/pages.yml`.

To use it:
1. Upload the full repository contents.
2. In **Settings > Pages**, set the source to **GitHub Actions**.
3. Push changes to the default branch.

## Included
- full website
- blog library
- service-area landing pages
- SEO files
- GTM / GA4 / Clarity tracking
- GitHub Pages support files

## Notes
- `.nojekyll` is included so GitHub Pages serves the site as-is.
- `404.html` is included.
- `CNAME` is included for custom domain use.
