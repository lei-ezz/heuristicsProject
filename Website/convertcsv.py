import pandas as pd
df = pd.read_json("INSERT JSON OBJECT HERE")
df = df.loc[["local_time_rfc822", "weather", "temperature_string"],"current_observation"].T
df.to_csv("pywu.cache.csv")