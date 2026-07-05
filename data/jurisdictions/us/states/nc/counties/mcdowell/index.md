---
type: Jurisdiction
title: "McDowell County, NC"
classification: county
fips: "37111"
state: "NC"
demographics:
  population: 44817
  population_under_18: 8692
  population_18_64: 26724
  population_65_plus: 9401
  median_household_income: 57168
  poverty_rate: 14.81
  homeownership_rate: 75.59
  unemployment_rate: 4.07
  median_home_value: 171100
  gini_index: 0.4223
  vacancy_rate: 13.61
  race_white: 39241
  race_black: 1730
  race_asian: 506
  race_native: 196
  hispanic: 3170
  bachelors_plus: 7837
districts:
  - to: "us/states/nc/districts/11"
    rel: in-district
    area_weight: 0.9965
  - to: "us/states/nc/districts/senate/46"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/nc/districts/house/85"
    rel: in-district
    area_weight: 0.8264
  - to: "us/states/nc/districts/house/113"
    rel: in-district
    area_weight: 0.1734
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# McDowell County, NC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 44817 |
| Under 18 | 8692 |
| 18–64 | 26724 |
| 65+ | 9401 |
| Median household income | 57168 |
| Poverty rate | 14.81 |
| Homeownership rate | 75.59 |
| Unemployment rate | 4.07 |
| Median home value | 171100 |
| Gini index | 0.4223 |
| Vacancy rate | 13.61 |
| White | 39241 |
| Black | 1730 |
| Asian | 506 |
| Native | 196 |
| Hispanic/Latino | 3170 |
| Bachelor's or higher | 7837 |

## Districts

- [NC-11](/us/states/nc/districts/11.md) — 100% (congressional)
- [NC Senate District 46](/us/states/nc/districts/senate/46.md) — 100% (state senate)
- [NC House District 85](/us/states/nc/districts/house/85.md) — 83% (state house)
- [NC House District 113](/us/states/nc/districts/house/113.md) — 17% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
