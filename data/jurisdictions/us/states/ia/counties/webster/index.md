---
type: Jurisdiction
title: "Webster County, IA"
classification: county
fips: "19187"
state: "IA"
demographics:
  population: 36886
  population_under_18: 7885
  population_18_64: 21678
  population_65_plus: 7323
  median_household_income: 68975
  poverty_rate: 12.86
  homeownership_rate: 70.34
  unemployment_rate: 4.82
  median_home_value: 153800
  gini_index: 0.4427
  vacancy_rate: 9.99
  race_white: 31785
  race_black: 1201
  race_asian: 455
  race_native: 96
  hispanic: 2439
  bachelors_plus: 6905
districts:
  - to: "us/states/ia/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ia/districts/senate/4"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/house/8"
    rel: in-district
    area_weight: 0.5272
  - to: "us/states/ia/districts/house/7"
    rel: in-district
    area_weight: 0.4726
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Webster County, IA

County jurisdiction — 4 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 36886 |
| Under 18 | 7885 |
| 18–64 | 21678 |
| 65+ | 7323 |
| Median household income | 68975 |
| Poverty rate | 12.86 |
| Homeownership rate | 70.34 |
| Unemployment rate | 4.82 |
| Median home value | 153800 |
| Gini index | 0.4427 |
| Vacancy rate | 9.99 |
| White | 31785 |
| Black | 1201 |
| Asian | 455 |
| Native | 96 |
| Hispanic/Latino | 2439 |
| Bachelor's or higher | 6905 |

## Districts

- [IA-04](/us/states/ia/districts/04.md) — 100% (congressional)
- [IA Senate District 4](/us/states/ia/districts/senate/4.md) — 100% (state senate)
- [IA House District 8](/us/states/ia/districts/house/8.md) — 53% (state house)
- [IA House District 7](/us/states/ia/districts/house/7.md) — 47% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
