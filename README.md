# [genicsblog.com](https://genicsblog.com)

Theme files for genicsblog.com

**This is not a proper Jekyll theme**. This repo contains only the theme files that genicsblog.com's repo retrevies at GitHub action's runtime to build the site.

## [Licsense](https://github.com/genicsblog/theme-files/blob/main/LICENSE.md)

The project is licensed under the [MIT](https://github.com/genicsblog/theme-files/blob/main/LICENSE.md) license terms and expects you to preserve the attribution to the developer and contributors in the website footer on each page.

## Local setup

Install [docker](https://docs.docker.com/get-docker).

Run these commands in order to build and run the container:

```shell
docker build -t genics-theme .
docker run -p 4000:4000 genics-theme
```

The first build would take a few minutes, once done go to [localhost:4000](http://localhost:4000) to preview the site.

