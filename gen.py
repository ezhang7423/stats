import pandas as pd


full = pd.read_csv("cs.csv", encoding="ISO-8859-1")
full = full[full[" Degree type and admission semester"].str.contains("PhD", na=False)]


def get_acceptance(stan):
    try:
        return round(
            (
                len(stan[stan[" Acception/rejection"] == "Accepted"].index)
                / len(stan.index)
            )
            * 100,
            2,
        )
    except ZeroDivisionError:
        return None


def get_school(school, full):
    return full[full["Institution"].str.contains(school, na=False)]


def get_yr(yr, full):
    return full[full[" Date posted"].str.contains(yr, na=False)]


interesting_years = ["2019", "2018", "2017"]
interesting_schools = [
    "Stanford University",
    "Carnegie Mellon University",
    "Massachusetts Institute Of Technology",
    "Berkeley",
    "Alberta",
    "Cambridge",
]

for school in interesting_schools:
    print(f"**{school}**\n")
    sel_school = get_school(school, full)
    for yr in interesting_years:
        ds = get_yr(yr, sel_school)

        if not (
            acceptance := f"{get_acceptance(ds)}% acceptance rate, {len(ds.index)} applicants"
        ):
            acceptance = "No data"

        print(f"{yr}: {acceptance}\n")
    print("\n\n\n")

print(
    "* This dataset is not representative of the entire population. It suffers from selection bias, and true acceptance rates are likely much lower"
)
