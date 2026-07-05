---
type: Jurisdiction
title: "Robeson County, NC"
classification: county
fips: "37155"
state: "NC"
demographics:
  population: 116902
  population_under_18: 30188
  population_18_64: 67961
  population_65_plus: 18753
  median_household_income: 41978
  poverty_rate: 27.23
  homeownership_rate: 65.84
  unemployment_rate: 5.96
  median_home_value: 94500
  gini_index: 0.5084
  vacancy_rate: 12.17
  race_white: 28260
  race_black: 27308
  race_asian: 1013
  race_native: 45465
  hispanic: 12723
  bachelors_plus: 14807
districts:
  - to: "us/states/nc/districts/08"
    rel: in-district
    area_weight: 0.5577
  - to: "us/states/nc/districts/07"
    rel: in-district
    area_weight: 0.4423
  - to: "us/states/nc/districts/senate/24"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/nc/districts/house/47"
    rel: in-district
    area_weight: 0.5972
  - to: "us/states/nc/districts/house/46"
    rel: in-district
    area_weight: 0.4027
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Robeson County, NC

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 116902 |
| Under 18 | 30188 |
| 18–64 | 67961 |
| 65+ | 18753 |
| Median household income | 41978 |
| Poverty rate | 27.23 |
| Homeownership rate | 65.84 |
| Unemployment rate | 5.96 |
| Median home value | 94500 |
| Gini index | 0.5084 |
| Vacancy rate | 12.17 |
| White | 28260 |
| Black | 27308 |
| Asian | 1013 |
| Native | 45465 |
| Hispanic/Latino | 12723 |
| Bachelor's or higher | 14807 |

## Districts

- [NC-08](/us/states/nc/districts/08.md) — 56% (congressional)
- [NC-07](/us/states/nc/districts/07.md) — 44% (congressional)
- [NC Senate District 24](/us/states/nc/districts/senate/24.md) — 100% (state senate)
- [NC House District 47](/us/states/nc/districts/house/47.md) — 60% (state house)
- [NC House District 46](/us/states/nc/districts/house/46.md) — 40% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
