# Podcast Audio IAB Classification Project

The purpose of this project is to classify audio podcast files into categories based on their IAB Content Taxonomy Mappings.


At this phase of the project there is an locally runnable FastAPI server that can be used to classify audio files.

To run the server, run the following command:

```python app.py```

navigate a web browser to http://127.0.0.1:5000/docs

From there you can upload a file to the server and it will return the IAB categories that the file is classified as.

## How the classification works

[![](https://mermaid.ink/img/pako:eNpVkMFuwjAMhl_Fypm-QA-ToAWNA9IE7NRysBK3jdTGWeJoMMS7L-3YAZ98-P7vt3xXmg2pUvUB_QDnunWQZ93s7Ejw6UdGQwa-rQwgA8H6Y3-BonjbNCdPpIcjae6dFcvukEUjdIEneE99b12_Q02XP-FmDkHVnOkqcA7oog7Wz7EnUC1A3fxQ4CIOLIUeMUbbWY0zBtyBzOHllP16AxU7IZdteGXH0w0O6H1ujU9jvRi3zZEkBbdc_1IM6AxUryXCCxfoK1EUChe1UhOFCa3JP7rP4lZlYqJWlXk11GEapVWte2Q0eYNCW2OFgyo7HCOtFCbh081pVUpI9A_VFvPLpyf1-AWia4aq)](https://mermaid-js.github.io/mermaid-live-editor/edit#pako:eNpVkMFuwjAMhl_Fypm-QA-ToAWNA9IE7NRysBK3jdTGWeJoMMS7L-3YAZ98-P7vt3xXmg2pUvUB_QDnunWQZ93s7Ejw6UdGQwa-rQwgA8H6Y3-BonjbNCdPpIcjae6dFcvukEUjdIEneE99b12_Q02XP-FmDkHVnOkqcA7oog7Wz7EnUC1A3fxQ4CIOLIUeMUbbWY0zBtyBzOHllP16AxU7IZdteGXH0w0O6H1ujU9jvRi3zZEkBbdc_1IM6AxUryXCCxfoK1EUChe1UhOFCa3JP7rP4lZlYqJWlXk11GEapVWte2Q0eYNCW2OFgyo7HCOtFCbh081pVUpI9A_VFvPLpyf1-AWia4aq)


# Models
https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-english
https://huggingface.co/facebook/bart-large-mnli



## Project Roadmap

[![](https://mermaid.ink/img/pako:eNp1kkFPwkAQhf_KZM9sQiuo6cWD0IRDE6IkxqSXsTvASrvb7E6NaPzvjlSICMyh6XZfvzdvMp-q8oZUplbomEsHUmy5JhjDE9EG5sG_UsXw4NE02PYKg0y5Dw0ywLOULgo9mfR3UdTWu_7vpP9WoHWwwLjR-t47lhMF-4E7HToDE2prv23IMRwqw2QA6TBN9XCsk9EAbswOdsYlPXGZvgswEBQSroZc_GDROWfdCgritTdx5zv3MdoXCTtr2poO_tneNk0OtjDLc9D6mKWl8zeqfQvNL3XpA3SRArAH44HXNp7HHQW4OgmQB5kTTKXHmWMKS6zo7l9vtxdgoxPYPFCUbP285dD-AV3r4egCaHzalXVYw8J31ZriEST5E61_7ksNVEOyKtbIln3-3JWK1zLsUmXyajBsSlW6L9F17c9iTY1lH1S2xDrSQGHH_nHrKpVx6GgvmlhcBWx-VV_fg5TWvw)](https://mermaid-js.github.io/mermaid-live-editor/edit#pako:eNp1kkFPwkAQhf_KZM9sQiuo6cWD0IRDE6IkxqSXsTvASrvb7E6NaPzvjlSICMyh6XZfvzdvMp-q8oZUplbomEsHUmy5JhjDE9EG5sG_UsXw4NE02PYKg0y5Dw0ywLOULgo9mfR3UdTWu_7vpP9WoHWwwLjR-t47lhMF-4E7HToDE2prv23IMRwqw2QA6TBN9XCsk9EAbswOdsYlPXGZvgswEBQSroZc_GDROWfdCgritTdx5zv3MdoXCTtr2poO_tneNk0OtjDLc9D6mKWl8zeqfQvNL3XpA3SRArAH44HXNp7HHQW4OgmQB5kTTKXHmWMKS6zo7l9vtxdgoxPYPFCUbP285dD-AV3r4egCaHzalXVYw8J31ZriEST5E61_7ksNVEOyKtbIln3-3JWK1zLsUmXyajBsSlW6L9F17c9iTY1lH1S2xDrSQGHH_nHrKpVx6GgvmlhcBWx-VV_fg5TWvw)


## Presentation Docs
https://docs.google.com/presentation/d/1VxMr3nuUtQlQ4S4fsYC4vXuh_YMCxvSsG3ag85-qhsA/edit?usp=sharing
