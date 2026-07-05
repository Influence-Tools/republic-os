---
type: Jurisdiction
title: "Scott County, MO"
classification: county
fips: "29201"
state: "MO"
demographics:
  population: 37933
  population_under_18: 9098
  population_18_64: 21736
  population_65_plus: 7099
  median_household_income: 62782
  poverty_rate: 12.81
  homeownership_rate: 71.1
  unemployment_rate: 2.85
  median_home_value: 154400
  gini_index: 0.4612
  vacancy_rate: 9.1
  race_white: 31009
  race_black: 3501
  race_asian: 33
  race_native: 8
  hispanic: 995
  bachelors_plus: 7546
districts:
  - to: "us/states/mo/districts/08"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/senate/27"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/mo/districts/house/148"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Scott County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 37933 |
| Under 18 | 9098 |
| 18–64 | 21736 |
| 65+ | 7099 |
| Median household income | 62782 |
| Poverty rate | 12.81 |
| Homeownership rate | 71.1 |
| Unemployment rate | 2.85 |
| Median home value | 154400 |
| Gini index | 0.4612 |
| Vacancy rate | 9.1 |
| White | 31009 |
| Black | 3501 |
| Asian | 33 |
| Native | 8 |
| Hispanic/Latino | 995 |
| Bachelor's or higher | 7546 |

## Districts

- [MO-08](/us/states/mo/districts/08.md) — 100% (congressional)
- [MO Senate District 27](/us/states/mo/districts/senate/27.md) — 100% (state senate)
- [MO House District 148](/us/states/mo/districts/house/148.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
