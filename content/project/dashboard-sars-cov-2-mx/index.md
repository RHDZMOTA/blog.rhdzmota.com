---
title: Dashboard Sars-Cov-2
summary: Monitoring Sars-Cov-2 Outbreak in Jalisco, MX.
tags:
- Just for fun

# Optional external URL for project (replaces project detail page).
external_link: ""

date: "2022-01-30"

image: 
caption: 
focal_point: Smart

links:
- icon: twitter
  icon_pack: fab
  name: Follow
  url: https://twitter.com/rhdzmota
  url_code: "https://github.com/RHDZMOTA/sars-cov-2-mx"
  url_pdf: ""
  url_slides: ""
  url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: example
---

This is a simple dashboard tracker for new covid cases identified in Jalisco, Mexico.
The chart contains the following time-series:
* Historical confirmed cases.
* `ma_short`: 7-day moving average
* `ma_long`: 21-day moving average 

<iframe
src='https://share.streamlit.io/rhdzmota/sars-cov-2-mx/main/dashboard.py'
height="750"
width="100%">
</iframe>

This project consists of two parts: `data-retrieval`, `data-visualization`.
A python module called [sars_cov_2_mx][sars_cov_2_mx_module] was developed to share common abstractions among the two parts.

[sars_cov_2_mx_module]: https://github.com/RHDZMOTA/sars-cov-2-mx/tree/main/sars_cov_2_mx


**Data Retrieval**:
* The raw data is retrieved from an [official mexican source](https://datos.covid-19.conacyt.mx/#DownZCSV).
* A python process is executed in a cloud environment (Heroku) to download the latest data available an update a Github Gist.
  * Python script [here](https://github.com/RHDZMOTA/sars-cov-2-mx/blob/main/update_gist.py).
  * Github gist with latest findings [here](https://gist.github.com/RHDZMOTA/6c7c16c62d7cea9b3e63eb4dce8e2713).
  * Execution frequency: daily at 03:00 AM UTC
  
**Data Visualization**:
* The sars_cov_2_mx module contains utility python functions to download the latest data from the github gist ([here][get-latest-snapshot]).
* A simple interactive dashboard ([here][interactive-dashboard-source]) hosted in [streamlit][streamlit-app] facilitated visualizing the results. 

[get-latest-snapshot]: https://github.com/RHDZMOTA/sars-cov-2-mx/blob/main/sars_cov_2_mx/dataset.py
[interactive-dashboard-source]: https://github.com/RHDZMOTA/sars-cov-2-mx/blob/main/dashboard.py
[streamlit-app]: https://share.streamlit.io/rhdzmota/sars-cov-2-mx/main/dashboard.py

