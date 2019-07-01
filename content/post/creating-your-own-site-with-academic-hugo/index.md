---
title: 'Creating your own site with Academic Hugo'
subtitle: 'Finally an easy setup guide! Linux version.'
summary: This is a test post  & documentation on how to install academic hugo on a debian-based linux distro. 
authors:
- admin
tags:
- Setup
categories: []
date: "2019-06-30T20:56:00Z"
lastmod: "2019-06-30T20:56:00Z"
featured: false
draft: false

projects: []
---


The [Academic Theme] for [Hugo] allows you to easily create a website using [markdown] and/or [jupyter] files. This blog-post is just a personal test, but might be useful for beginners wanting to create their site. 

[Academic Theme]: https://sourcethemes.com/academic/
[Hugo]: https://gohugo.io/
[markdown]: https://en.wikipedia.org/wiki/Markdown
[jupyter]: https://jupyter.org/

## Setup

Go to the [academic-kickstart github page](https://github.com/sourcethemes/academic-kickstart) and fork the repositroy.


Now download the content with:


```commandline
$ mkdir my-site && \
    wget -O - https://github.com/github-username/academic-kickstart/tarball/master | \
    tar xz -C my-site --strip-components 1
```

**Replace** `my-site` with the name of the repository that will contain your site's code (optional) and `github-username` with your github username (e.g. `rhdzmota` in my case). 


Install hugo (select your version [here](https://github.com/gohugoio/hugo/releases)). For debian-based distributions: 

```commandline
$ sudo apt install wget && \
    wget -O hugo.deb 'https://github.com/gohugoio/hugo/releases/download/v0.55.6/hugo_extended_0.55.6_Linux-64bit.deb' && \
    sudo dpkg -i hugo.deb
```

**Note** that [academic version 4.3.1+ requires hugo-extended 0.55.6+](https://github.com/gcushen/hugo-academic/issues/1092).  

Verify your installation by running: `hugo version`. 

Now enter your site's directory and create the git-repository:

```commandline
$ cd my-site && \
    rm -rf themes/academic .gitmodules && 
    git init && git submodule add https://github.com/gcushen/hugo-academic themes/academic 
```

You should be able to preview the site with: `hugo serve -D`

For now on, feel free to configure your site. You can see a [live example here](https://academic-demo.netlify.com/) with the [github code here](https://github.com/gcushen/hugo-academic/tree/master/exampleSite). 

## Publishing with github pages

Add the following line anywhere on `config/_default/config.toml`:

```text
publishDir = "docs"
```

Now when running `hugo` con the commandline, a `docs` directory will appear. This directory contains a set of static files that can be directly published to github pages. 

Just configure your repository in github and push into master. More documentation [here](https://help.github.com/en/articles/configuring-a-publishing-source-for-github-pages). Integration with custom domains guide [here](https://help.github.com/en/articles/using-a-custom-domain-with-github-pages) and [here](https://dev.to/trentyang/how-to-setup-google-domain-for-github-pages-1p58).
