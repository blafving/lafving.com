---
name: Attendance & Class Recording
org: Wharton School
date_start: 2022
date_end: 2024
accent: pink
status: maintained
skills:
  - "Vendor management"
  - "Product design"
  - "Stakeholder alignment"
outcomes:
  - "Successful deployment across Wharton MBA and undergraduate classes"
  - "Designed a custom absence-request feature that was adopted by vendor's production app"
  - "Two products launched from one initiative"
---

# Attendance & Class Recording

I led a multi-functional team whose goal it was to identify and onboard a new attendance solution for Wharton. The primary challenge was in integrating the new vendor with a motley of solutions that were developed in-house and communicating with key stakeholders, including Sr. Vice Dean of Education, Brian Bushee, as well as academic department chairs, and Wharton Computing Leadership. My role was somewhere in between project and product manager in terms of the skills required.

## Identifying the right vendor was easy, but integration was the challenge

In this case, we were able to narrow down our options quite quickly, and between two candidates it was a unanimous approval of one vendor. Even still, we were aware of two important feature gaps between the current application and theirs: Seating Chart and Video & Absence Requests. 

We had mitigation plans for each, but while Seating Chart only required user communication, Video & Absence Requests would require internal development. 

Wharton records the vast majority of classes, and some professors publish their recordings, so that students can review lectures on demand. The expectation around video availability was different if the student had not attended lecture. Some faculty generally did not make their videos public, UNLESS a student had submitted an absence request, and they would provide individual access. Others tried to use video requests as a separate feature entirely - sometimes releasing all videos in the week before exams, and others.  

## Designing the solution on the vendor's infrastructure

It was more intuitive that video requests would need to persist in-house as a separate service, as it really helped extend a Panopto, our video vendor. Absence requests, on the other hand, was a direct attendance issue and should be part of one attendance solution. 

We requested our chosen vendor to develop this feature for us, but they refused! Even discussing with stakeholders, the general consensus was that the mitigation plan was not ideal, but reasonable. I thought this would lead to an overcomplicated product and continue to burden our internal team. So I tried again. 

This time, I designed an absence requests feature based on the vendor's architecture. It utilized existing processes and features but did what we needed it to do. I presented the plan and worked with our multi-functional team to assess viability, and through initial skepticism received approval to discuss with the vendor. 

This time, they accepted and built the feature in two months and still keeping us well within budget. 

## Deployment

We deployed the new attendance solution alongside a standalone video requests LTI tool in Fall, 2024. It was perceived amongst faculty and Wharton Computing as a complete success. Internally, our teams had switched from a manual process to initialize attendance for each course, to a self-service application that faculty turn on and manage easily themselves. 

The internally developed video requests app was also received and used seamlessly. 

Service owners for both attendance and video requests are happy, and only minor modifications have been needed since launch.

Moreover, the absence requests feature we designed was pulled into the vendor's production app, and they typically include the feature demo in their initial sales calls. It was truly a win for everyone.