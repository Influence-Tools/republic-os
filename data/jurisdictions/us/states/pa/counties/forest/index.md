---
type: Jurisdiction
title: "Forest County, PA"
classification: county
fips: "42053"
state: "PA"
demographics:
  population: 6715
  population_under_18: 248
  population_18_64: 4791
  population_65_plus: 1676
  median_household_income: 52191
  poverty_rate: 11.93
  homeownership_rate: 78.33
  unemployment_rate: 2.46
  median_home_value: 115300
  gini_index: 0.4036
  vacancy_rate: 72.32
  race_white: 5290
  race_black: 961
  race_asian: 31
  race_native: 24
  hispanic: 344
  bachelors_plus: 936
districts:
  - to: "us/states/pa/districts/15"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/pa/districts/senate/21"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/pa/districts/house/65"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Forest County, PA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6715 |
| Under 18 | 248 |
| 18–64 | 4791 |
| 65+ | 1676 |
| Median household income | 52191 |
| Poverty rate | 11.93 |
| Homeownership rate | 78.33 |
| Unemployment rate | 2.46 |
| Median home value | 115300 |
| Gini index | 0.4036 |
| Vacancy rate | 72.32 |
| White | 5290 |
| Black | 961 |
| Asian | 31 |
| Native | 24 |
| Hispanic/Latino | 344 |
| Bachelor's or higher | 936 |

## Districts

- [PA-15](/us/states/pa/districts/15.md) — 100% (congressional)
- [PA Senate District 21](/us/states/pa/districts/senate/21.md) — 100% (state senate)
- [PA House District 65](/us/states/pa/districts/house/65.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
