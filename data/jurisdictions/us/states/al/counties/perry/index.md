---
type: Jurisdiction
title: "Perry County, AL"
classification: county
fips: "01105"
state: "AL"
demographics:
  population: 8031
  population_under_18: 2547
  population_18_64: 1818
  population_65_plus: 3666
  median_household_income: 37654
  poverty_rate: 31.36
  homeownership_rate: 77.53
  unemployment_rate: 16.46
  median_home_value: 86400
  gini_index: 0.3563
  vacancy_rate: 13.18
  race_white: 2236
  race_black: 5720
  race_asian: 5
  race_native: 0
  hispanic: 17
  bachelors_plus: 1164
districts:
  - to: "us/states/al/districts/07"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/al/districts/senate/23"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/al/districts/house/67"
    rel: in-district
    area_weight: 0.9195
  - to: "us/states/al/districts/house/68"
    rel: in-district
    area_weight: 0.0804
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Perry County, AL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8031 |
| Under 18 | 2547 |
| 18–64 | 1818 |
| 65+ | 3666 |
| Median household income | 37654 |
| Poverty rate | 31.36 |
| Homeownership rate | 77.53 |
| Unemployment rate | 16.46 |
| Median home value | 86400 |
| Gini index | 0.3563 |
| Vacancy rate | 13.18 |
| White | 2236 |
| Black | 5720 |
| Asian | 5 |
| Native | 0 |
| Hispanic/Latino | 17 |
| Bachelor's or higher | 1164 |

## Districts

- [AL-07](/us/states/al/districts/07.md) — 100% (congressional)
- [AL Senate District 23](/us/states/al/districts/senate/23.md) — 100% (state senate)
- [AL House District 67](/us/states/al/districts/house/67.md) — 92% (state house)
- [AL House District 68](/us/states/al/districts/house/68.md) — 8% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
