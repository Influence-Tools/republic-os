---
type: Jurisdiction
title: "Edwards County, KS"
classification: county
fips: "20047"
state: "KS"
demographics:
  population: 2779
  population_under_18: 645
  population_18_64: 1509
  population_65_plus: 625
  median_household_income: 52692
  poverty_rate: 18.87
  homeownership_rate: 79.17
  unemployment_rate: 6.79
  median_home_value: 70900
  gini_index: 0.4537
  vacancy_rate: 24.98
  race_white: 2152
  race_black: 4
  race_asian: 2
  race_native: 19
  hispanic: 633
  bachelors_plus: 538
districts:
  - to: "us/states/ks/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/senate/33"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/house/115"
    rel: in-district
    area_weight: 0.8257
  - to: "us/states/ks/districts/house/122"
    rel: in-district
    area_weight: 0.1743
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Edwards County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2779 |
| Under 18 | 645 |
| 18–64 | 1509 |
| 65+ | 625 |
| Median household income | 52692 |
| Poverty rate | 18.87 |
| Homeownership rate | 79.17 |
| Unemployment rate | 6.79 |
| Median home value | 70900 |
| Gini index | 0.4537 |
| Vacancy rate | 24.98 |
| White | 2152 |
| Black | 4 |
| Asian | 2 |
| Native | 19 |
| Hispanic/Latino | 633 |
| Bachelor's or higher | 538 |

## Districts

- [KS-04](/us/states/ks/districts/04.md) — 100% (congressional)
- [KS Senate District 33](/us/states/ks/districts/senate/33.md) — 100% (state senate)
- [KS House District 115](/us/states/ks/districts/house/115.md) — 83% (state house)
- [KS House District 122](/us/states/ks/districts/house/122.md) — 17% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
