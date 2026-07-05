---
type: Jurisdiction
title: "Floyd County, IA"
classification: county
fips: "19067"
state: "IA"
demographics:
  population: 15328
  population_under_18: 3478
  population_18_64: 8324
  population_65_plus: 3526
  median_household_income: 68557
  poverty_rate: 11.59
  homeownership_rate: 76.61
  unemployment_rate: 3.27
  median_home_value: 143500
  gini_index: 0.4327
  vacancy_rate: 10.99
  race_white: 13794
  race_black: 211
  race_asian: 247
  race_native: 8
  hispanic: 595
  bachelors_plus: 2458
districts:
  - to: "us/states/ia/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ia/districts/senate/29"
    rel: in-district
    area_weight: 0.8356
  - to: "us/states/ia/districts/senate/30"
    rel: in-district
    area_weight: 0.1644
  - to: "us/states/ia/districts/house/58"
    rel: in-district
    area_weight: 0.8356
  - to: "us/states/ia/districts/house/60"
    rel: in-district
    area_weight: 0.1644
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Floyd County, IA

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 15328 |
| Under 18 | 3478 |
| 18–64 | 8324 |
| 65+ | 3526 |
| Median household income | 68557 |
| Poverty rate | 11.59 |
| Homeownership rate | 76.61 |
| Unemployment rate | 3.27 |
| Median home value | 143500 |
| Gini index | 0.4327 |
| Vacancy rate | 10.99 |
| White | 13794 |
| Black | 211 |
| Asian | 247 |
| Native | 8 |
| Hispanic/Latino | 595 |
| Bachelor's or higher | 2458 |

## Districts

- [IA-02](/us/states/ia/districts/02.md) — 100% (congressional)
- [IA Senate District 29](/us/states/ia/districts/senate/29.md) — 84% (state senate)
- [IA Senate District 30](/us/states/ia/districts/senate/30.md) — 16% (state senate)
- [IA House District 58](/us/states/ia/districts/house/58.md) — 84% (state house)
- [IA House District 60](/us/states/ia/districts/house/60.md) — 16% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
