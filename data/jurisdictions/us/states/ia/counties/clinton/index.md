---
type: Jurisdiction
title: "Clinton County, IA"
classification: county
fips: "19045"
state: "IA"
demographics:
  population: 46268
  population_under_18: 10582
  population_18_64: 26308
  population_65_plus: 9378
  median_household_income: 66981
  poverty_rate: 13.19
  homeownership_rate: 74.55
  unemployment_rate: 3.37
  median_home_value: 160600
  gini_index: 0.4445
  vacancy_rate: 9.61
  race_white: 41393
  race_black: 1434
  race_asian: 310
  race_native: 126
  hispanic: 1668
  bachelors_plus: 9475
districts:
  - to: "us/states/ia/districts/01"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/senate/35"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/house/69"
    rel: in-district
    area_weight: 0.3252
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Clinton County, IA

County jurisdiction — 12 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 46268 |
| Under 18 | 10582 |
| 18–64 | 26308 |
| 65+ | 9378 |
| Median household income | 66981 |
| Poverty rate | 13.19 |
| Homeownership rate | 74.55 |
| Unemployment rate | 3.37 |
| Median home value | 160600 |
| Gini index | 0.4445 |
| Vacancy rate | 9.61 |
| White | 41393 |
| Black | 1434 |
| Asian | 310 |
| Native | 126 |
| Hispanic/Latino | 1668 |
| Bachelor's or higher | 9475 |

## Districts

- [IA-01](/us/states/ia/districts/01.md) — 100% (congressional)
- [IA Senate District 35](/us/states/ia/districts/senate/35.md) — 100% (state senate)
- [IA House District 69](/us/states/ia/districts/house/69.md) — 33% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
