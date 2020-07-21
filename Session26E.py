import matplotlib.pyplot as plt

# ages = [21, 22, 23, 4, 5, 6, 77, 8, 21, 10, 31, 32, 66, 54, 90]
# bins = 10
# plt.hist(ages, bins)
# plt.show()

# languages = ["python", "java", "c++", "dart", "javascript"]
# jobs = [70, 80, 88, 12, 90]
#
# plt.barh(languages, jobs, align="center", alpha=0.3)
# plt.show()

years = [2016, 2017, 2018, 2019, 2020]
jobs_in_java = [90, 80, 67, 54, 22]
jobs_in_python = [80, 70, 55, 66, 90]
plt.bar(years, jobs_in_java, 0.60, color='c', label="Java")
plt.bar(years, jobs_in_python, 0.30, color='g', label="Python")

plt.legend()
plt.show()


