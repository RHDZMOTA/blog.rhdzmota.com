# Blog Register

Status options:
* Defining
* Research
* Drafting
* Writing
* IndividualReview
* PeerReview
* Editing
* Ready
* Published


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

## [DOCS-0](https://hackmd.io/5Q-MyBg3QKSKch9Th634qw)
* Status: Published
* Title: Blog Register
* URL: https://hackmd.io/5Q-MyBg3QKSKch9Th634qw

## [DOCS-1](https://hackmd.io/2JlcI0DLSdGCGpmCdMcLOA)
* Status: Published
* Title: Creating your own site with Academic Hugo
* URL: https://hackmd.io/2JlcI0DLSdGCGpmCdMcLOA
