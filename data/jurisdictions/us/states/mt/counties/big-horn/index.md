---
type: Jurisdiction
title: "Big Horn County, MT"
classification: county
fips: "30003"
state: "MT"
demographics:
  population: 12891
  population_under_18: 4041
  population_18_64: 7036
  population_65_plus: 1814
  median_household_income: 58750
  poverty_rate: 22.08
  homeownership_rate: 66.71
  unemployment_rate: 13.24
  median_home_value: 143400
  gini_index: 0.4435
  vacancy_rate: 15.46
  race_white: 3851
  race_black: 34
  race_asian: 25
  race_native: 8607
  hispanic: 610
  bachelors_plus: 1748
districts:
  - to: "us/states/mt/districts/02"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/mt/districts/senate/21"
    rel: in-district
    area_weight: 0.8287
  - to: "us/states/mt/districts/senate/18"
    rel: in-district
    area_weight: 0.1712
  - to: "us/states/mt/districts/house/42"
    rel: in-district
    area_weight: 0.4431
  - to: "us/states/mt/districts/house/41"
    rel: in-district
    area_weight: 0.3855
  - to: "us/states/mt/districts/house/35"
    rel: in-district
    area_weight: 0.1712
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mt]
timestamp: "2026-07-03"
---

# Big Horn County, MT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12891 |
| Under 18 | 4041 |
| 18–64 | 7036 |
| 65+ | 1814 |
| Median household income | 58750 |
| Poverty rate | 22.08 |
| Homeownership rate | 66.71 |
| Unemployment rate | 13.24 |
| Median home value | 143400 |
| Gini index | 0.4435 |
| Vacancy rate | 15.46 |
| White | 3851 |
| Black | 34 |
| Asian | 25 |
| Native | 8607 |
| Hispanic/Latino | 610 |
| Bachelor's or higher | 1748 |

## Districts

- [MT-02](/us/states/mt/districts/02.md) — 100% (congressional)
- [MT Senate District 21](/us/states/mt/districts/senate/21.md) — 83% (state senate)
- [MT Senate District 18](/us/states/mt/districts/senate/18.md) — 17% (state senate)
- [MT House District 42](/us/states/mt/districts/house/42.md) — 44% (state house)
- [MT House District 41](/us/states/mt/districts/house/41.md) — 39% (state house)
- [MT House District 35](/us/states/mt/districts/house/35.md) — 17% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
