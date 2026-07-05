---
type: Jurisdiction
title: "Webb County, TX"
classification: county
fips: "48479"
state: "TX"
demographics:
  population: 269294
  population_under_18: 84189
  population_18_64: 157364
  population_65_plus: 27741
  median_household_income: 63058
  poverty_rate: 21.31
  homeownership_rate: 64.68
  unemployment_rate: 5.49
  median_home_value: 189900
  gini_index: 0.4528
  vacancy_rate: 7.72
  race_white: 55703
  race_black: 1282
  race_asian: 1339
  race_native: 909
  hispanic: 255830
  bachelors_plus: 42656
districts:
  - to: "us/states/tx/districts/28"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/tx/districts/senate/21"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/80"
    rel: in-district
    area_weight: 0.8606
  - to: "us/states/tx/districts/house/42"
    rel: in-district
    area_weight: 0.1392
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Webb County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 269294 |
| Under 18 | 84189 |
| 18–64 | 157364 |
| 65+ | 27741 |
| Median household income | 63058 |
| Poverty rate | 21.31 |
| Homeownership rate | 64.68 |
| Unemployment rate | 5.49 |
| Median home value | 189900 |
| Gini index | 0.4528 |
| Vacancy rate | 7.72 |
| White | 55703 |
| Black | 1282 |
| Asian | 1339 |
| Native | 909 |
| Hispanic/Latino | 255830 |
| Bachelor's or higher | 42656 |

## Districts

- [TX-28](/us/states/tx/districts/28.md) — 100% (congressional)
- [TX Senate District 21](/us/states/tx/districts/senate/21.md) — 100% (state senate)
- [TX House District 80](/us/states/tx/districts/house/80.md) — 86% (state house)
- [TX House District 42](/us/states/tx/districts/house/42.md) — 14% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
