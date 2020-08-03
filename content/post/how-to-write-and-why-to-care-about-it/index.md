---
title: 'The importance of writing.'
subtitle: 'Quick tips on how to improve your writing and why you should care about it!'
summary: This blogpost covers a set of quick tips on how to improve your writing and why you should care about it!
authors: ["admin"]
tags: ["Setup"]
categories: []
date: "2020-07-23T00:00:00Z"
featured: false
draft: false
diagram: true

projects: []
---

Let's see if hugo can render some diagrams:

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

```mermaid
graph TD;
  A-->B;
  A-->C;
  B-->D;
  C-->D;
```

