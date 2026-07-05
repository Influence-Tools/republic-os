---
type: Jurisdiction
title: "Wilcox County, AL"
classification: county
fips: "01131"
state: "AL"
demographics:
  population: 10172
  population_under_18: 2542
  population_18_64: 2967
  population_65_plus: 4663
  median_household_income: 40640
  poverty_rate: 28.2
  homeownership_rate: 77.41
  unemployment_rate: 11.76
  median_home_value: 98800
  gini_index: 0.5523
  vacancy_rate: 27.63
  race_white: 2801
  race_black: 7121
  race_asian: 1
  race_native: 3
  hispanic: 3
  bachelors_plus: 1314
districts:
  - to: "us/states/al/districts/07"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/al/districts/senate/23"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/al/districts/house/69"
    rel: in-district
    area_weight: 0.8587
  - to: "us/states/al/districts/house/68"
    rel: in-district
    area_weight: 0.141
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Wilcox County, AL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10172 |
| Under 18 | 2542 |
| 18–64 | 2967 |
| 65+ | 4663 |
| Median household income | 40640 |
| Poverty rate | 28.2 |
| Homeownership rate | 77.41 |
| Unemployment rate | 11.76 |
| Median home value | 98800 |
| Gini index | 0.5523 |
| Vacancy rate | 27.63 |
| White | 2801 |
| Black | 7121 |
| Asian | 1 |
| Native | 3 |
| Hispanic/Latino | 3 |
| Bachelor's or higher | 1314 |

## Districts

- [AL-07](/us/states/al/districts/07.md) — 100% (congressional)
- [AL Senate District 23](/us/states/al/districts/senate/23.md) — 100% (state senate)
- [AL House District 69](/us/states/al/districts/house/69.md) — 86% (state house)
- [AL House District 68](/us/states/al/districts/house/68.md) — 14% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
