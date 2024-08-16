from ydata_profiling import ProfileReport

import pandas as pd

df = pd.read_csv(r"C:\Users\A4952\PycharmProjects\June_automation_batch1\files\Contact_info.csv")

print("contact info data df")
print(df)
Result = ProfileReport(df)
Result.to_file("profile_report.html")



