---
name: Lecture Recall
org: Wharton School
date_start: 2023
date_end: Present
accent: cyan
status: active
skills:
  - "AWS Bedrock"
  - "RAG / Vector DB"
  - "Prompt engineering"
  - "Python"
  - "InfoSec negotiation"
outcomes:
  - "Second author on Custom GPTs for higher education"
  - "First hybrid RAG architecture in higher education"
  - "v1.0 delivering Fall 2026"
connected_to:
  - type: idea
    slug: slow-down-chatbot-build
  - type: idea
    slug: bedrock-for-pms
---

# Lecture Recall

In Summer, 2024, Pete Fader, perhaps the best Marketing Professor in the world, asked if we could build a custom chatbot for his course, Applied Probability Models in Marketing. The course is quant-heavy material, and to pass the course, much less get an "A," students need to review constantly. At that time, they could review 1) lecture videos, 2) course notes, or 3) ask a Teaching Assistant. Remove the TA option due to time constraints, and students were left with two relatively inefficient ways to study (by today's standards).

## First try: AWS GenAI Innovation Center

At the time, the idea of Retrieval Augmented Generation was pretty new and not well supported. We didn't even know whether performance would be / could be good enough for students to find it useful. We asked AWS if their GenAI Innovation Center would be interested in building the initial proof of concept. And they were! 

AWS built out our first prototype in about 8 weeks, and Pete immediately tested in his classes. While the web app did not meet our quality standards, it did show a lot of promise.  

## Second Try: OpenAI EDU and a Custom GPT
Meanwhile, WEMBA Vice Dean Richard Waterman was also interested in a custom course chatbot, so while Pete tested the prototype, we started work on our second try with Richard. 

Wharton was just onboarding OpenAI EDU for all MBA and WEMBA students, as well as faculty and staff. ChatGPT had this interesting feature called Custom GPTs, which allowed ChatGPT to use api calls and use the response in its answer. The Custom GPT approach was less stable, but it solved a lot of problems for us. OpenAI was a clear leader AND they had already designed the interface - with features like file uploads and custom instructions. 

Choosing the Custom GPT hybrid architecture significantly reduced our scope, which helped us identify new, gamechanging features on the backend. These included:
- Direct links to the on-demand videos for each chunk, so students would be able to review the response and then clickthrough to immediately validate the chatbot's response
- Semantic chunking (Shawn Zamechek came back from vacation with this idea, and the difference was immediately discernable)
- Course index on the metadata, so students could say, "What did Pete say about spikes in the second session?"

Shawn Zamechek built out a prototype in just a few weeks that would serve as an intermediary between API calls, video ingestion, and our vector store. And the result definitely seemed like a win to us. We launched for Richard's Statistics course in Fall, and this approach was immediately validated by student approval and usage - particularly around exam periods.

## Beta and Scaling
Since 2024 Fall, faculty and students have driven demand for Lecture Recall organically. Around 20 faculty use Lecture Recall, and we haven't lost any faculty so far. We are currently building a more scalable version, so that we can continue to satisfy demand. Wish us luck in Fall 2026! 

Richard recently published a paper on [Custom GPTs for Higher Ed](https://onlinelibrary.wiley.com/doi/10.1002/sta4.70109) and named me as second author.