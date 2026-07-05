---
type: Jurisdiction
title: "Franklin County, IA"
classification: county
fips: "19069"
state: "IA"
demographics:
  population: 9956
  population_under_18: 2396
  population_18_64: 5413
  population_65_plus: 2147
  median_household_income: 59894
  poverty_rate: 13.6
  homeownership_rate: 72.42
  unemployment_rate: 3.79
  median_home_value: 124100
  gini_index: 0.4561
  vacancy_rate: 9.86
  race_white: 8336
  race_black: 67
  race_asian: 36
  race_native: 29
  hispanic: 1642
  bachelors_plus: 1665
districts:
  - to: "us/states/ia/districts/04"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ia/districts/senate/28"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/house/55"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Franklin County, IA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9956 |
| Under 18 | 2396 |
| 18–64 | 5413 |
| 65+ | 2147 |
| Median household income | 59894 |
| Poverty rate | 13.6 |
| Homeownership rate | 72.42 |
| Unemployment rate | 3.79 |
| Median home value | 124100 |
| Gini index | 0.4561 |
| Vacancy rate | 9.86 |
| White | 8336 |
| Black | 67 |
| Asian | 36 |
| Native | 29 |
| Hispanic/Latino | 1642 |
| Bachelor's or higher | 1665 |

## Districts

- [IA-04](/us/states/ia/districts/04.md) — 100% (congressional)
- [IA Senate District 28](/us/states/ia/districts/senate/28.md) — 100% (state senate)
- [IA House District 55](/us/states/ia/districts/house/55.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
