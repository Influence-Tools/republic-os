---
type: Jurisdiction
title: "Hoke County, NC"
classification: county
fips: "37093"
state: "NC"
demographics:
  population: 53835
  population_under_18: 14495
  population_18_64: 33055
  population_65_plus: 6285
  median_household_income: 64912
  poverty_rate: 17.08
  homeownership_rate: 72.97
  unemployment_rate: 6.61
  median_home_value: 219300
  gini_index: 0.4873
  vacancy_rate: 7.95
  race_white: 20773
  race_black: 17664
  race_asian: 839
  race_native: 3741
  hispanic: 8415
  bachelors_plus: 10904
districts:
  - to: "us/states/nc/districts/09"
    rel: in-district
    area_weight: 0.9987
  - to: "us/states/nc/districts/senate/24"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/nc/districts/house/48"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Hoke County, NC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 53835 |
| Under 18 | 14495 |
| 18–64 | 33055 |
| 65+ | 6285 |
| Median household income | 64912 |
| Poverty rate | 17.08 |
| Homeownership rate | 72.97 |
| Unemployment rate | 6.61 |
| Median home value | 219300 |
| Gini index | 0.4873 |
| Vacancy rate | 7.95 |
| White | 20773 |
| Black | 17664 |
| Asian | 839 |
| Native | 3741 |
| Hispanic/Latino | 8415 |
| Bachelor's or higher | 10904 |

## Districts

- [NC-09](/us/states/nc/districts/09.md) — 100% (congressional)
- [NC Senate District 24](/us/states/nc/districts/senate/24.md) — 100% (state senate)
- [NC House District 48](/us/states/nc/districts/house/48.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
