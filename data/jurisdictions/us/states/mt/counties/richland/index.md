---
type: Jurisdiction
title: "Richland County, MT"
classification: county
fips: "30083"
state: "MT"
demographics:
  population: 11235
  population_under_18: 2802
  population_18_64: 6470
  population_65_plus: 1963
  median_household_income: 73084
  poverty_rate: 6.6
  homeownership_rate: 67.12
  unemployment_rate: 3.27
  median_home_value: 263000
  gini_index: 0.4668
  vacancy_rate: 21.18
  race_white: 10086
  race_black: 30
  race_asian: 48
  race_native: 24
  hispanic: 620
  bachelors_plus: 1965
districts:
  - to: "us/states/mt/districts/02"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mt/districts/senate/15"
    rel: in-district
    area_weight: 0.6883
  - to: "us/states/mt/districts/senate/17"
    rel: in-district
    area_weight: 0.3116
  - to: "us/states/mt/districts/house/30"
    rel: in-district
    area_weight: 0.6883
  - to: "us/states/mt/districts/house/33"
    rel: in-district
    area_weight: 0.3115
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mt]
timestamp: "2026-07-03"
---

# Richland County, MT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11235 |
| Under 18 | 2802 |
| 18–64 | 6470 |
| 65+ | 1963 |
| Median household income | 73084 |
| Poverty rate | 6.6 |
| Homeownership rate | 67.12 |
| Unemployment rate | 3.27 |
| Median home value | 263000 |
| Gini index | 0.4668 |
| Vacancy rate | 21.18 |
| White | 10086 |
| Black | 30 |
| Asian | 48 |
| Native | 24 |
| Hispanic/Latino | 620 |
| Bachelor's or higher | 1965 |

## Districts

- [MT-02](/us/states/mt/districts/02.md) — 100% (congressional)
- [MT Senate District 15](/us/states/mt/districts/senate/15.md) — 69% (state senate)
- [MT Senate District 17](/us/states/mt/districts/senate/17.md) — 31% (state senate)
- [MT House District 30](/us/states/mt/districts/house/30.md) — 69% (state house)
- [MT House District 33](/us/states/mt/districts/house/33.md) — 31% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
