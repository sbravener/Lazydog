
# Easier way to add new blog entries

This site now includes a simple helper script in `tools/add_blog_post.py`.

## Easiest workflow

1. Save your new article source file as HTML on your computer.
2. Open a terminal in the site folder.
3. Run a command like this:

   ```bash
   python tools/add_blog_post.py      --title "How to review admin access without disrupting users"      --category "Microsoft 365 • Security"      --audience "All Industries"      --excerpt "A plain-language look at how businesses can reduce admin risk without creating support headaches."      --source-file post-31.html
   ```

4. The script will automatically:
   - create the new page inside `/blog`
   - add it to `/blog/index.html`
   - add it to `sitemap.xml`
   - skip duplicate titles already in the blog index

## Helpful notes

- Keep article titles unique.
- Use short excerpts for the blog listing.
- If you want to replace an article page, delete the existing page first and run the script again.
- The helper uses the paragraph text found in the source HTML file.

## If you prefer a copy-and-paste method

Use `blog/_template.html` as your starting page, duplicate it, then update:

- page title
- meta description
- hero heading
- article body
