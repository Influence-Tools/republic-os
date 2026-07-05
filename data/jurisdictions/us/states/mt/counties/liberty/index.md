---
type: Jurisdiction
title: "Liberty County, MT"
classification: county
fips: "30051"
state: "MT"
demographics:
  population: 1952
  population_under_18: 531
  population_18_64: 1000
  population_65_plus: 421
  median_household_income: 57857
  poverty_rate: 25.79
  homeownership_rate: 63.4
  unemployment_rate: 0.6
  median_home_value: 169100
  gini_index: 0.5099
  vacancy_rate: 13.5
  race_white: 1823
  race_black: 0
  race_asian: 14
  race_native: 46
  hispanic: 1
  bachelors_plus: 455
districts:
  - to: "us/states/mt/districts/02"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mt/districts/senate/14"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/mt/districts/house/28"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mt]
timestamp: "2026-07-03"
---

# Liberty County, MT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1952 |
| Under 18 | 531 |
| 18–64 | 1000 |
| 65+ | 421 |
| Median household income | 57857 |
| Poverty rate | 25.79 |
| Homeownership rate | 63.4 |
| Unemployment rate | 0.6 |
| Median home value | 169100 |
| Gini index | 0.5099 |
| Vacancy rate | 13.5 |
| White | 1823 |
| Black | 0 |
| Asian | 14 |
| Native | 46 |
| Hispanic/Latino | 1 |
| Bachelor's or higher | 455 |

## Districts

- [MT-02](/us/states/mt/districts/02.md) — 100% (congressional)
- [MT Senate District 14](/us/states/mt/districts/senate/14.md) — 100% (state senate)
- [MT House District 28](/us/states/mt/districts/house/28.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
