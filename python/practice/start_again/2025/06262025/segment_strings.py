#   https://www.google.com/search?q=You+are+given+four+words+-+apple%2C+pear%2C+pier%2C+and+pie.+Can+this+be+completely+segmented%3F+If+yes%2C+then+how%3F+using+python%C2%A0&client=safari&sca_esv=ccb8066356fd07b7&rls=en&sxsrf=AE3TifOrIqHFtncYwtw9ShKIXYAfR9aBIg%3A1750786899982&ei=U-NaaOXWO7Wqur8PxYangQ8&ved=0ahUKEwilzIC6zYqOAxU1le4BHUXDKfAQ4dUDCBE&uact=5&oq=You+are+given+four+words+-+apple%2C+pear%2C+pier%2C+and+pie.+Can+this+be+completely+segmented%3F+If+yes%2C+then+how%3F+using+python%C2%A0&gs_lp=Egxnd3Mtd2l6LXNlcnAieVlvdSBhcmUgZ2l2ZW4gZm91ciB3b3JkcyAtIGFwcGxlLCBwZWFyLCBwaWVyLCBhbmQgcGllLiBDYW4gdGhpcyBiZSBjb21wbGV0ZWx5IHNlZ21lbnRlZD8gSWYgeWVzLCB0aGVuIGhvdz8gdXNpbmcgcHl0aG9uwqAyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEcyChAAGLADGNYEGEdI0ztQ2hRY2ThwAngBkAEAmAEAoAEAqgEAuAEDyAEA-AEC-AEBmAICoAJDmAMAiAYBkAYIkgcBMqAHALIHALgHAMIHBzMtMS4wLjHIBz0&sclient=gws-wiz-serp

import nltk
from nltk.tokenize import word_tokenize

words = "apple pear pier pie "
tokens = word_tokenize(words)
print (tokens)