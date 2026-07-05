---
type: Jurisdiction
title: "Logan County, ND"
classification: county
fips: "38047"
state: "ND"
demographics:
  population: 1819
  population_under_18: 380
  population_18_64: 912
  population_65_plus: 527
  median_household_income: 62750
  poverty_rate: 12.43
  homeownership_rate: 83.01
  unemployment_rate: 1.74
  median_home_value: 102000
  gini_index: 0.4534
  vacancy_rate: 27.38
  race_white: 1713
  race_black: 4
  race_asian: 3
  race_native: 8
  hispanic: 71
  bachelors_plus: 376
districts:
  - to: "us/states/nd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nd/districts/senate/28"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/nd/districts/house/28"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nd]
timestamp: "2026-07-03"
---

# Logan County, ND

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1819 |
| Under 18 | 380 |
| 18–64 | 912 |
| 65+ | 527 |
| Median household income | 62750 |
| Poverty rate | 12.43 |
| Homeownership rate | 83.01 |
| Unemployment rate | 1.74 |
| Median home value | 102000 |
| Gini index | 0.4534 |
| Vacancy rate | 27.38 |
| White | 1713 |
| Black | 4 |
| Asian | 3 |
| Native | 8 |
| Hispanic/Latino | 71 |
| Bachelor's or higher | 376 |

## Districts

- [ND-00](/us/states/nd/districts/00.md) — 100% (congressional)
- [ND Senate District 28](/us/states/nd/districts/senate/28.md) — 100% (state senate)
- [ND House District 28](/us/states/nd/districts/house/28.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
