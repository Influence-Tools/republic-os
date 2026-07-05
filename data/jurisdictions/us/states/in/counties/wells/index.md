---
type: Jurisdiction
title: "Wells County, IN"
classification: county
fips: "18179"
state: "IN"
demographics:
  population: 28420
  population_under_18: 7014
  population_18_64: 16107
  population_65_plus: 5299
  median_household_income: 71957
  poverty_rate: 7.16
  homeownership_rate: 75.62
  unemployment_rate: 2.61
  median_home_value: 197600
  gini_index: 0.4225
  vacancy_rate: 4.37
  race_white: 26309
  race_black: 283
  race_asian: 64
  race_native: 2
  hispanic: 1145
  bachelors_plus: 4955
districts:
  - to: "us/states/in/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/in/districts/senate/19"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/in/districts/house/79"
    rel: in-district
    area_weight: 0.9029
  - to: "us/states/in/districts/house/50"
    rel: in-district
    area_weight: 0.0969
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Wells County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 28420 |
| Under 18 | 7014 |
| 18–64 | 16107 |
| 65+ | 5299 |
| Median household income | 71957 |
| Poverty rate | 7.16 |
| Homeownership rate | 75.62 |
| Unemployment rate | 2.61 |
| Median home value | 197600 |
| Gini index | 0.4225 |
| Vacancy rate | 4.37 |
| White | 26309 |
| Black | 283 |
| Asian | 64 |
| Native | 2 |
| Hispanic/Latino | 1145 |
| Bachelor's or higher | 4955 |

## Districts

- [IN-03](/us/states/in/districts/03.md) — 100% (congressional)
- [IN Senate District 19](/us/states/in/districts/senate/19.md) — 100% (state senate)
- [IN House District 79](/us/states/in/districts/house/79.md) — 90% (state house)
- [IN House District 50](/us/states/in/districts/house/50.md) — 10% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
