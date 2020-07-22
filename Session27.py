"""
    Matplotlib and Web Scrapping
"""

import matplotlib.pyplot as plt
languages = ["Python", "Java", "C++", "Dart", "JavaScript"]
jobs = [80, 70, 90, 30, 78]

plt.pie(jobs, labels=languages)
plt.legend()

plt.show()