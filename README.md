# Static HTML Instagram Clone

This project is a **static front-end clone of Instagram**, built as part
of a learning exercise to practice HTML, CSS, and basic web templating.\
It demonstrates different ways to structure and serve static content,
preparing for later dynamic Flask-based implementations.

## Quick start

```console
$ python3 -m venv env/
$ source env/bin/activate
```

------------------------------------------------------------------------

## Features

-   **Hand-coded Static HTML**
    -   Prebuilt HTML pages simulating Instagram profiles and feeds
    -   Includes sample user directories (`/users/username/index.html`)
-   **Static Assets**
    -   CSS styling (`style.css`)
    -   Placeholder images and uploaded photos (`uploads/`)
    -   Branding assets (`logo.png`)
-   **Progression Structure**
    -   `handcoded_html/` → raw HTML pages
    -   `hello/` → minimal template + JSON config
    -   `hello_css/` → HTML + CSS styling
    -   `insta485/` → more complete static Instagram site structure with
        CSS, images, uploads
-   **Executable Scripts**
    -   `bin/insta485run` -- script to serve content
    -   `bin/insta485test` -- script to test setup

------------------------------------------------------------------------

## Repository Structure

    static-html-instagram-main/
    ├── bin/                         # Run/test scripts
    │   ├── insta485run
    │   └── insta485test
    ├── handcoded_html/              # Fully static version (HTML + CSS + uploads)
    │   ├── index.html
    │   ├── css/style.css
    │   ├── images/logo.png
    │   ├── uploads/*.jpg
    │   └── users/<username>/index.html
    ├── hello/                       # Minimal demo app with config.json
    ├── hello_css/                   # Demo with CSS styling
    ├── insta485/                     # More structured Instagram static clone
    │   ├── static/css/style.css
    │   ├── static/images/logo.png
    │   ├── static/uploads/*.jpg
    │   └── config.json
    ├── requirements.txt             # Dependencies (if extended to Python/Flask)
    ├── pyproject.toml               # Project metadata
    └── old__main__.py               # Legacy script (unused)

------------------------------------------------------------------------

## Setup

### Option 1 -- View static HTML directly

Open the files under `handcoded_html/` or `insta485/` in your browser.

Example:

    handcoded_html/index.html

### Option 2 -- Run with helper script

Use the provided run script:

``` bash
bin/insta485run
```

This will serve the static site locally so you can browse it like a web
app.

------------------------------------------------------------------------

## Usage

-   Navigate between static pages as if browsing Instagram
-   Explore `/users/username/` directories for mock profile pages
-   Inspect CSS in `static/css/style.css` or
    `handcoded_html/css/style.css`

------------------------------------------------------------------------

This project serves as a **starter** for later courses/projects
where: - Static HTML is replaced with Flask + Jinja templates - JSON
configs are used for dynamic data - Full stack functionality (posts,
likes, comments) is implemented


