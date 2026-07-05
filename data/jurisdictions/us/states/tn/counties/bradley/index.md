---
type: Jurisdiction
title: "Bradley County, TN"
classification: county
fips: "47011"
state: "TN"
demographics:
  population: 111065
  population_under_18: 27391
  population_18_64: 35059
  population_65_plus: 48615
  median_household_income: 66552
  poverty_rate: 12.69
  homeownership_rate: 67.26
  unemployment_rate: 6.57
  median_home_value: 261900
  gini_index: 0.4421
  vacancy_rate: 7.3
  race_white: 93033
  race_black: 4912
  race_asian: 1297
  race_native: 209
  hispanic: 9320
  bachelors_plus: 26335
districts:
  - to: "us/states/tn/districts/03"
    rel: in-district
    area_weight: 0.9985
  - to: "us/states/tn/districts/senate/1"
    rel: in-district
    area_weight: 0.8945
  - to: "us/states/tn/districts/senate/2"
    rel: in-district
    area_weight: 0.1054
  - to: "us/states/tn/districts/house/22"
    rel: in-district
    area_weight: 0.734
  - to: "us/states/tn/districts/house/24"
    rel: in-district
    area_weight: 0.2657
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Bradley County, TN

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 111065 |
| Under 18 | 27391 |
| 18–64 | 35059 |
| 65+ | 48615 |
| Median household income | 66552 |
| Poverty rate | 12.69 |
| Homeownership rate | 67.26 |
| Unemployment rate | 6.57 |
| Median home value | 261900 |
| Gini index | 0.4421 |
| Vacancy rate | 7.3 |
| White | 93033 |
| Black | 4912 |
| Asian | 1297 |
| Native | 209 |
| Hispanic/Latino | 9320 |
| Bachelor's or higher | 26335 |

## Districts

- [TN-03](/us/states/tn/districts/03.md) — 100% (congressional)
- [TN Senate District 1](/us/states/tn/districts/senate/1.md) — 89% (state senate)
- [TN Senate District 2](/us/states/tn/districts/senate/2.md) — 11% (state senate)
- [TN House District 22](/us/states/tn/districts/house/22.md) — 73% (state house)
- [TN House District 24](/us/states/tn/districts/house/24.md) — 27% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
