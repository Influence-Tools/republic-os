---
type: Jurisdiction
title: "Anderson County, KS"
classification: county
fips: "20003"
state: "KS"
demographics:
  population: 7834
  population_under_18: 2009
  population_18_64: 4203
  population_65_plus: 1622
  median_household_income: 70614
  poverty_rate: 11.04
  homeownership_rate: 78.9
  unemployment_rate: 4.1
  median_home_value: 171400
  gini_index: 0.3488
  vacancy_rate: 10.54
  race_white: 7199
  race_black: 83
  race_asian: 0
  race_native: 7
  hispanic: 142
  bachelors_plus: 1030
districts:
  - to: "us/states/ks/districts/03"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/ks/districts/senate/12"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/house/9"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Anderson County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7834 |
| Under 18 | 2009 |
| 18–64 | 4203 |
| 65+ | 1622 |
| Median household income | 70614 |
| Poverty rate | 11.04 |
| Homeownership rate | 78.9 |
| Unemployment rate | 4.1 |
| Median home value | 171400 |
| Gini index | 0.3488 |
| Vacancy rate | 10.54 |
| White | 7199 |
| Black | 83 |
| Asian | 0 |
| Native | 7 |
| Hispanic/Latino | 142 |
| Bachelor's or higher | 1030 |

## Districts

- [KS-03](/us/states/ks/districts/03.md) — 100% (congressional)
- [KS Senate District 12](/us/states/ks/districts/senate/12.md) — 100% (state senate)
- [KS House District 9](/us/states/ks/districts/house/9.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
