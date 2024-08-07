import pandas as pd
from ydata_profiling import ProfileReport #while installing "ydata-profiling"

df = pd.read_csv(r"C:\Users\ichan\PycharmProjects\June_automation_batch5\files\Contact_info.csv")
print("contact info data df:")
print(df)

Result = ProfileReport(df)
Result.to_file("profile_report.html")

