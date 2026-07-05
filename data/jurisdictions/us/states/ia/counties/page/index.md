---
type: Jurisdiction
title: "Page County, IA"
classification: county
fips: "19145"
state: "IA"
demographics:
  population: 15131
  population_under_18: 2906
  population_18_64: 8561
  population_65_plus: 3664
  median_household_income: 57953
  poverty_rate: 13.76
  homeownership_rate: 70.54
  unemployment_rate: 5.01
  median_home_value: 125300
  gini_index: 0.4577
  vacancy_rate: 10.69
  race_white: 13840
  race_black: 259
  race_asian: 99
  race_native: 83
  hispanic: 505
  bachelors_plus: 2827
districts:
  - to: "us/states/ia/districts/03"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/senate/9"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/house/18"
    rel: in-district
    area_weight: 0.671
  - to: "us/states/ia/districts/house/17"
    rel: in-district
    area_weight: 0.329
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Page County, IA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 15131 |
| Under 18 | 2906 |
| 18–64 | 8561 |
| 65+ | 3664 |
| Median household income | 57953 |
| Poverty rate | 13.76 |
| Homeownership rate | 70.54 |
| Unemployment rate | 5.01 |
| Median home value | 125300 |
| Gini index | 0.4577 |
| Vacancy rate | 10.69 |
| White | 13840 |
| Black | 259 |
| Asian | 99 |
| Native | 83 |
| Hispanic/Latino | 505 |
| Bachelor's or higher | 2827 |

## Districts

- [IA-03](/us/states/ia/districts/03.md) — 100% (congressional)
- [IA Senate District 9](/us/states/ia/districts/senate/9.md) — 100% (state senate)
- [IA House District 18](/us/states/ia/districts/house/18.md) — 67% (state house)
- [IA House District 17](/us/states/ia/districts/house/17.md) — 33% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
