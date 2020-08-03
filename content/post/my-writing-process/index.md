---
title: 'My writing process'
subtitle: 'Documenting my writing process.'
summary: To be defined.
authors: ["admin"]
tags: ["Setup"]
categories: []
date: "2019-06-30T20:56:00Z"
lastmod: "2019-06-30T20:56:00Z"
featured: false
draft: false
commentable: true
projects: []

---

This is a work in progress.

```mermaid
stateDiagram
    Defining --> Research
    Research --> Drafting
    Research --> Writing
    Drafting --> Writing
    Drafting --> Research
    Writing --> IndividualReview
    Writing --> Drafting
    IndividualReview --> PeerReview
    IndividualReview --> Research
    IndividualReview --> Drafting
    IndividualReview --> Writing
    PeerReview --> Ready
    PeerReview --> Research
    PeerReview --> Editing
    Editing --> Ready
    Editing --> Writing
    Editing --> Research
    Ready --> Published
    Published --> Editing
    
```
