---
type: Jurisdiction
title: "Lincoln County, MT"
classification: county
fips: "30053"
state: "MT"
demographics:
  population: 21175
  population_under_18: 3823
  population_18_64: 10970
  population_65_plus: 6382
  median_household_income: 47143
  poverty_rate: 15.44
  homeownership_rate: 77.63
  unemployment_rate: 5.06
  median_home_value: 296500
  gini_index: 0.4484
  vacancy_rate: 17.48
  race_white: 19142
  race_black: 12
  race_asian: 61
  race_native: 240
  hispanic: 654
  bachelors_plus: 4051
districts:
  - to: "us/states/mt/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mt/districts/senate/1"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mt/districts/house/1"
    rel: in-district
    area_weight: 0.7162
  - to: "us/states/mt/districts/house/2"
    rel: in-district
    area_weight: 0.2837
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mt]
timestamp: "2026-07-03"
---

# Lincoln County, MT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 21175 |
| Under 18 | 3823 |
| 18–64 | 10970 |
| 65+ | 6382 |
| Median household income | 47143 |
| Poverty rate | 15.44 |
| Homeownership rate | 77.63 |
| Unemployment rate | 5.06 |
| Median home value | 296500 |
| Gini index | 0.4484 |
| Vacancy rate | 17.48 |
| White | 19142 |
| Black | 12 |
| Asian | 61 |
| Native | 240 |
| Hispanic/Latino | 654 |
| Bachelor's or higher | 4051 |

## Districts

- [MT-01](/us/states/mt/districts/01.md) — 100% (congressional)
- [MT Senate District 1](/us/states/mt/districts/senate/1.md) — 100% (state senate)
- [MT House District 1](/us/states/mt/districts/house/1.md) — 72% (state house)
- [MT House District 2](/us/states/mt/districts/house/2.md) — 28% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
