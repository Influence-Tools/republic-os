---
type: Jurisdiction
title: "Lake County, CA"
classification: county
fips: "06033"
state: "CA"
demographics:
  population: 68152
  population_under_18: 14934
  population_18_64: 36928
  population_65_plus: 16290
  median_household_income: 60621
  poverty_rate: 16.97
  homeownership_rate: 72.16
  unemployment_rate: 11.06
  median_home_value: 324300
  gini_index: 0.4842
  vacancy_rate: 21.69
  race_white: 46044
  race_black: 1523
  race_asian: 999
  race_native: 2053
  hispanic: 16796
  bachelors_plus: 11566
districts:
  - to: "us/states/ca/districts/04"
    rel: in-district
    area_weight: 0.9933
  - to: "us/states/ca/districts/senate/2"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ca/districts/house/4"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# Lake County, CA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 68152 |
| Under 18 | 14934 |
| 18–64 | 36928 |
| 65+ | 16290 |
| Median household income | 60621 |
| Poverty rate | 16.97 |
| Homeownership rate | 72.16 |
| Unemployment rate | 11.06 |
| Median home value | 324300 |
| Gini index | 0.4842 |
| Vacancy rate | 21.69 |
| White | 46044 |
| Black | 1523 |
| Asian | 999 |
| Native | 2053 |
| Hispanic/Latino | 16796 |
| Bachelor's or higher | 11566 |

## Districts

- [CA-04](/us/states/ca/districts/04.md) — 99% (congressional)
- [CA Senate District 2](/us/states/ca/districts/senate/2.md) — 100% (state senate)
- [CA House District 4](/us/states/ca/districts/house/4.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
