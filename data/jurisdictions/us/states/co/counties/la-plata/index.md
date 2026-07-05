---
type: Jurisdiction
title: "La Plata County, CO"
classification: county
fips: "08067"
state: "CO"
demographics:
  population: 56331
  population_under_18: 9867
  population_18_64: 34736
  population_65_plus: 11728
  median_household_income: 86056
  poverty_rate: 11.7
  homeownership_rate: 70.93
  unemployment_rate: 3.82
  median_home_value: 591500
  gini_index: 0.4589
  vacancy_rate: 15.91
  race_white: 45897
  race_black: 140
  race_asian: 459
  race_native: 2836
  hispanic: 7244
  bachelors_plus: 28331
districts:
  - to: "us/states/co/districts/03"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/co/districts/senate/6"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/co/districts/house/59"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# La Plata County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 56331 |
| Under 18 | 9867 |
| 18–64 | 34736 |
| 65+ | 11728 |
| Median household income | 86056 |
| Poverty rate | 11.7 |
| Homeownership rate | 70.93 |
| Unemployment rate | 3.82 |
| Median home value | 591500 |
| Gini index | 0.4589 |
| Vacancy rate | 15.91 |
| White | 45897 |
| Black | 140 |
| Asian | 459 |
| Native | 2836 |
| Hispanic/Latino | 7244 |
| Bachelor's or higher | 28331 |

## Districts

- [CO-03](/us/states/co/districts/03.md) — 100% (congressional)
- [CO Senate District 6](/us/states/co/districts/senate/6.md) — 100% (state senate)
- [CO House District 59](/us/states/co/districts/house/59.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
