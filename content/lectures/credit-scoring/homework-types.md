---
title: Homework Types
linktitle: Homework Types
toc: true
type: docs
date: "2019-08-01T00:00:00+01:00"
draft: false
menu:
  credit-scoring:
    parent: II Resources
    weight: 1003

---

{{% alert warning %}}
Academic fraud, plagiarism, or any other form of academic dishonesty will result on the invalidation of the related homework. 
{{% /alert %}}

{{% toc %}}

## Code 

A coding homework represents a complete and functional application solving a particular problem or implementing a business logic. The students should follow the coding best practices of the language being used.

Style guide by language: 

* [Python style guide](https://www.python.org/dev/peps/pep-0008/)
* [Scala style guide - EPFL](https://docs.scala-lang.org/style/)
* [Scala style guide - Databricks](https://github.com/databricks/scala-style-guide)

Formatting tools:

* [Black for Python](https://github.com/psf/black)
* [Scalariform code formatter](https://github.com/scala-ide/scalariform)

A complete code-homework should contain both in-code documentation, documentation files, and tests. 

* Total points: **25**

## Essay

The number of words in the essay should satisfy the following constraint:

$$700 \leq words \leq 1000$$

Students should follow the "five-paragraph essay" format, which consists of three principal components: 

* **Introduction** - The principal purpose of the introduction is to expose the *thesis statement* explicitly. An effective introductory paragraph usually begins with a hook to grab the reader's attention. This might be a personal anecdote, relevant statistics, or a quote. After that, the writer should move on to a clear, one-sentence thesis statement.
* **Body** - A good essay usually contains roughly three body paragraphs. The first sentence of these paragraphs is known as the *topic sentence* and should provide an argument in favor of the thesis. Body paragraphs make use of examples, supporting evidence, statistics, and citations. To ensure continuity, you might want to use a "transition phrase" to connect different paragraphs (e.g., "moreover", "on the other hand", "by contrast", "furthermore").
* **Conclusion** - This paragraph should start with a "concluding transition" and briefly recap on the main arguments of the essay. Lastly, it should restate the thesis statement. 

You can read more recommendations [here](https://www.internationalstudent.com/essay_writing/essay_tips/).

Consider the following [aesthetic hints](https://jordanbpeterson.com/docs/230/Hints%20on%20writing.pdf):

- [x] Are your sentences elegant and careful? 
- [x] Have you chosen each word properly? 
- [x] Does the sentence say what it is supposed to say? 
- [x] Do your paragraphs constitute the elaboration of a single idea? 
- [x] Are they sufficiently comprehensive and concise?
- [x] Does the essay succeed as a unit? 
- [x] Does it make an identifiable and intelligent statement? 

The grading of the essay is simple: 

|                            | +3                                                                    | +1.5                                            | +0                           |
|----------------------------|-----------------------------------------------------------------------|-------------------------------------------------|------------------------------|
| Intro and thesis statement | Clear and concise; directly related to the topic; Engaging hook.      | Clear but slightly unrelated; mediocre hook.    | Vague and unclear.           |
| Body and topic sentences   | Main argument of paragraph is identifiable and in the first sentence. | Hard to distinguish main argument               | Vague and unclear.           |
| Supporting evidence        | Use of evidence, examples, citations, etc.                            | Regular use of supporting evidence.             | Little to none usage.        |
| Conclusion                 | Correct transition; recap of main arguments; restates the thesis.     | Slightly unaligned with the rest of the essay.  | Fails to provide closure.    |
| Grammar                    | Free of grammatical errors.                                           | Few grammatical errors.                         | Frequent grammatical errors. |

Total points: **15**

Grammar examination includes, but is not limited to: 

* Spelling, punctuation, and syntax. 
* Correct use of sentences (e.g., no sentence fragments or run-on sentences). 
* Consistent verb tense usage. 

If you are interested in improving your writing skills, consider reading: 

* The [Grammarly blog](https://www.grammarly.com/blog/). Contains relevant posts such as [the top 10 grammatical mistakes] and [15 easy steps to improve writing]. 
*  The [10-step process for stronger writing] from BigThink.  

[Grammarly blog]: https://www.grammarly.com/blog/
[the top 10 grammatical mistakes]: https://www.grammarly.com/blog/grammatical-errors/
[15 easy steps to improve writing]: https://www.grammarly.com/blog/how-to-improve-writing-skills/
[10-step process for stronger writing]: https://bigthink.com/personal-growth/jordan-petersons-ten-step-process-for-stronger-writing


## Report

The data-analysis reports must be done using Python in [rmarkdown](https://bookdown.org/yihui/rmarkdown/) or [jupyter notebook / lab](https://jupyter.org/). The final deliverable should be a PDF file with the related source (.Rmd or .ipynb). 

The minimum structure of the report should include: 

1. **Executive summary** - Explain the problem, the dataset, and your findings. 
2. **Body** - The body contains the development and technical aspects of the report. It's usually "question oriented". The following sections are expected:
    * **Data** - Description of the data source, format, and shape. For each relevant variable, the type should be identified. How does the data quality looks? Does it includes some missing values?
    * **Univariable analysis** - Analyze the distribution of the target variable. Does the target variable follows a normal distribution? Should we apply a custom transformation? 
    * **Multivariable analysis** - Identify the relevant variables in the dataset. This can be done by a correlation analysis. Visualize results (e.g., correlation matrix, scatterplot, box-plots). What's the distribution of the related variables? What variables do you think can be used as predictors? 
3. **Conclusions** - Closing paragraph that contains the most relevant insights of the exploratory analysis.
4. **Appendix** - Any other resource not directly related to the main analysis but of further interest. This might include: 
    * A more in-depth description of a technical procedure. 
    * Detailed output of a process. 
    * Mathematical demonstrations. 
    * Supporting code. 

|                       | +2                                                            | +1                                            | +0                                         |
|-----------------------|---------------------------------------------------------------|-----------------------------------------------|--------------------------------------------|
| Report structure      | Follows the minimal structure.                                | NA                                            | Missing structure.                         |
| Data visualization    | Correct visualization and formatting.                         | Correct visualization but lack of formatting. | Confusing visualization.                   |
| Technical proficiency | Statistical proficiency; efficient coding and good practices. | Correct but inefficient implementation.       | Wrong implementation.                      |
| Analytical reasoning  | Outstanding analysis; excellent written communication skills. | Mediocre written communication and analysis.  | Fails to demonstrate analytical reasoning. |
| Grammar               | Free of grammatical errors.                                   | Few grammatical errors.                       | Frequent grammatical errors.               |

Total points: **10**

If you are interested in improving your data-analysis skills, consider reading some [kaggle kernels]. Particularly this [comprehensive data exploration with Python].

[kaggle kernels]: https://www.kaggle.com/kernels?sortBy=voteCount&group=everyone&pageSize=20
[comprehensive data exploration with Python]: https://www.kaggle.com/pmarcelino/comprehensive-data-exploration-with-python

## Exercise

Total points: **10**

The final score is proportional to the number of correct answers. Should be delivered via github. 

## Data Entry

Total points: **5** 

Data entries will be evaluated as binary.
