# Lazy Dog Computing – Website + Tracking Package

This package includes the full website plus the current production tracking setup on every HTML page.

## Current tracking stack

### Google Tag Manager
- Container ID: `GTM-M525FFRJ`
- Insertion points:
  - first script block inside `<head>`
  - noscript iframe immediately after `<body>`

### Google Analytics 4
- Measurement ID: `G-NG2PEF5DWV`
- Loaded immediately after the GTM head snippet

### Microsoft Clarity
- Project ID: `w5yaevmu4f`
- Loaded immediately after the GA4 code

## Page coverage

Tracking was applied across all website HTML files in this package, including:
- root pages
- blog index
- all blog posts
- vertical pages
- the blog template file

## How to use this package

1. Unzip the package.
2. Upload the website contents to your web host.
3. Keep the folder structure exactly as provided.
4. After deployment, open a few pages and verify:
   - GTM loads in page source near the top of `<head>`
   - GTM noscript iframe appears immediately after `<body>`
   - GA4 loads with `G-NG2PEF5DWV`
   - Clarity loads with `w5yaevmu4f`

## GTM sync guidance

This website already loads GTM and GA4 using the same `dataLayer`, so GTM and GA4 are aligned.

If you want GA4 to be managed entirely inside GTM later, use this order:
1. Keep the GTM snippets in the site.
2. In GTM, create a GA4 Configuration tag using measurement ID `G-NG2PEF5DWV`.
3. Trigger it on All Pages.
4. Publish the container.
5. After GTM-based GA4 is confirmed working, you may remove the direct GA4 snippet from the website if you want GTM-only management.

## Recommended verification steps

### GTM
- Use GTM Preview mode.
- Confirm container `GTM-M525FFRJ` is firing on all pages.

### GA4
- In Google Analytics, open Realtime.
- Visit the site.
- Confirm page views appear under property `G-NG2PEF5DWV`.

### Clarity
- Log into Clarity.
- Confirm sessions begin appearing for project `w5yaevmu4f`.

## Files updated in this package

A machine-readable list is included in `tracking-updated-files.json`.
