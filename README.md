# Staff Engineer's Field Guide

This repository contains a comprehensive, community-driven field guide for Staff, Principal, and Distinguished Engineers. The content is curated to cover the essential topics for technical leadership, influence, and execution at senior levels.

## Structure

The guide is built using [MkDocs](https://www.mkdocs.org/) with the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme. The content is organized as follows:

-   `docs/`: Contains all the markdown files for the site.
    -   `field-guide/`: The core content of the Staff Engineer's Field Guide, organized into chapters such as Leadership, Engineering, and Execution.
    -   `appendix/`: Contains supplementary materials, including antipatterns, design patterns, and other resources.
-   `mkdocs.yml`: The main configuration file for the MkDocs site, including navigation and theme settings.

## Local Development

To build and serve the site locally, follow these steps:

1.  **Install Dependencies**: This project uses Poetry for dependency management. To install the necessary dependencies, run:

    ```bash
    make bootstrap
    ```

2.  **Serve the Site**: To start the local development server, run:

    ```bash
    make serve
    ```

    Then, open your browser and navigate to `http://127.0.0.1:8000` to view the site.

## Deployment

This site is automatically built and deployed to GitHub Pages on every push to the `main` branch using the GitHub Actions workflow defined in `.github/workflows/ci.yml`.