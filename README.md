# [RHDZMOTA](https://rhdzmota.com) Site

This site is build with the [Academic Theme] for [Hugo]. 

[Academic Theme]: https://themes.gohugo.io/academic/
[Hugo]: https://gohugo.io/

## Setup

Use [this blogpost](https://rhdzmota.com/post/creating-your-own-site-with-academic-hugo/) to install Academic Hugo into your local system. Or just copy and paste: 

```commandline
$ sudo apt install wget && \
    wget -O hugo.deb 'https://github.com/gohugoio/hugo/releases/download/v0.55.6/hugo_extended_0.55.6_Linux-64bit.deb' && \
    sudo dpkg -i hugo.deb
```

Clone this repository with submodules: 

```commandline
$ git clone --recurse-submodules git@github.com:RHDZMOTA/rhdzmota-site.git
```

Test with a local development server:

```commandline
$ hugo serve
```

## Publishing

The `docs/` directory contains the static content to publish into github pages. It's configured as a git submodule. You can rebuild the site by running: 

```commandline
$ hugo
```

Or use the build script with: `bash build.sh`

Add/commit changes and upload the content by just pushing into master in both the base-project and the submodule. 

```commandline
$ git push --recurse-submodules=on-demand master
```
