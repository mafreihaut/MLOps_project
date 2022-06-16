# Podcast Audio IAB Classification Project

The purpose of this project is to classify audio podcast files into categories into IAB Content Taxonomy Mappings.




To run the server locally , run the following command:

```python app.py```

Containerized version:


`docker build --tag mlops-project . `

`docker run -p 8000:8000 -t -i mlops-project`


navigate a web browser to http://127.0.0.1:5000/docs

From there you can upload a file to the server and it will return the IAB categories that the file is classified as.

## How the classification works

[![](https://mermaid.ink/img/pako:eNpVkMFuwjAMhl_Fypm-QA-ToAWNA9IE7NRysBK3jdTGWeJoMMS7L-3YAZ98-P7vt3xXmg2pUvUB_QDnunWQZ93s7Ejw6UdGQwa-rQwgA8H6Y3-BonjbNCdPpIcjae6dFcvukEUjdIEneE99b12_Q02XP-FmDkHVnOkqcA7oog7Wz7EnUC1A3fxQ4CIOLIUeMUbbWY0zBtyBzOHllP16AxU7IZdteGXH0w0O6H1ujU9jvRi3zZEkBbdc_1IM6AxUryXCCxfoK1EUChe1UhOFCa3JP7rP4lZlYqJWlXk11GEapVWte2Q0eYNCW2OFgyo7HCOtFCbh081pVUpI9A_VFvPLpyf1-AWia4aq)](https://mermaid-js.github.io/mermaid-live-editor/edit#pako:eNpVkMFuwjAMhl_Fypm-QA-ToAWNA9IE7NRysBK3jdTGWeJoMMS7L-3YAZ98-P7vt3xXmg2pUvUB_QDnunWQZ93s7Ejw6UdGQwa-rQwgA8H6Y3-BonjbNCdPpIcjae6dFcvukEUjdIEneE99b12_Q02XP-FmDkHVnOkqcA7oog7Wz7EnUC1A3fxQ4CIOLIUeMUbbWY0zBtyBzOHllP16AxU7IZdteGXH0w0O6H1ujU9jvRi3zZEkBbdc_1IM6AxUryXCCxfoK1EUChe1UhOFCa3JP7rP4lZlYqJWlXk11GEapVWte2Q0eYNCW2OFgyo7HCOtFCbh081pVUpI9A_VFvPLpyf1-AWia4aq)


# Models
https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-english
https://huggingface.co/facebook/bart-large-mnli



## Presentation Docs and Video


[Video Link](https://www.loom.com/share/dc94c719895444e5a0a0d1f8aea6025c)
[Slide Deck](https://docs.google.com/presentation/d/1edrufHzsZV60Y_nCZiuQsm0B6pZ2JWFeG2ZuEG6IxRo/edit?usp=sharing)
