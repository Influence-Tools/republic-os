---
type: Jurisdiction
title: "Pickens County, AL"
classification: county
fips: "01107"
state: "AL"
demographics:
  population: 18721
  population_under_18: 4137
  population_18_64: 6037
  population_65_plus: 8547
  median_household_income: 46274
  poverty_rate: 20.0
  homeownership_rate: 75.81
  unemployment_rate: 4.72
  median_home_value: 123900
  gini_index: 0.4751
  vacancy_rate: 22.51
  race_white: 10468
  race_black: 7663
  race_asian: 10
  race_native: 61
  hispanic: 666
  bachelors_plus: 2439
districts:
  - to: "us/states/al/districts/07"
    rel: in-district
    area_weight: 0.9984
  - to: "us/states/al/districts/senate/21"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/al/districts/house/61"
    rel: in-district
    area_weight: 0.6098
  - to: "us/states/al/districts/house/71"
    rel: in-district
    area_weight: 0.3896
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Pickens County, AL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 18721 |
| Under 18 | 4137 |
| 18–64 | 6037 |
| 65+ | 8547 |
| Median household income | 46274 |
| Poverty rate | 20.0 |
| Homeownership rate | 75.81 |
| Unemployment rate | 4.72 |
| Median home value | 123900 |
| Gini index | 0.4751 |
| Vacancy rate | 22.51 |
| White | 10468 |
| Black | 7663 |
| Asian | 10 |
| Native | 61 |
| Hispanic/Latino | 666 |
| Bachelor's or higher | 2439 |

## Districts

- [AL-07](/us/states/al/districts/07.md) — 100% (congressional)
- [AL Senate District 21](/us/states/al/districts/senate/21.md) — 100% (state senate)
- [AL House District 61](/us/states/al/districts/house/61.md) — 61% (state house)
- [AL House District 71](/us/states/al/districts/house/71.md) — 39% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
