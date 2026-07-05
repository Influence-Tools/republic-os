---
type: Jurisdiction
title: "Carbon County, MT"
classification: county
fips: "30009"
state: "MT"
demographics:
  population: 11116
  population_under_18: 1907
  population_18_64: 6091
  population_65_plus: 3118
  median_household_income: 80261
  poverty_rate: 7.79
  homeownership_rate: 78.0
  unemployment_rate: 4.46
  median_home_value: 420800
  gini_index: 0.4556
  vacancy_rate: 27.75
  race_white: 10137
  race_black: 31
  race_asian: 3
  race_native: 36
  hispanic: 337
  bachelors_plus: 3998
districts:
  - to: "us/states/mt/districts/02"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mt/districts/senate/28"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/mt/districts/house/55"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mt]
timestamp: "2026-07-03"
---

# Carbon County, MT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11116 |
| Under 18 | 1907 |
| 18–64 | 6091 |
| 65+ | 3118 |
| Median household income | 80261 |
| Poverty rate | 7.79 |
| Homeownership rate | 78.0 |
| Unemployment rate | 4.46 |
| Median home value | 420800 |
| Gini index | 0.4556 |
| Vacancy rate | 27.75 |
| White | 10137 |
| Black | 31 |
| Asian | 3 |
| Native | 36 |
| Hispanic/Latino | 337 |
| Bachelor's or higher | 3998 |

## Districts

- [MT-02](/us/states/mt/districts/02.md) — 100% (congressional)
- [MT Senate District 28](/us/states/mt/districts/senate/28.md) — 100% (state senate)
- [MT House District 55](/us/states/mt/districts/house/55.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
