---
type: Jurisdiction
title: "Prairie County, AR"
classification: county
fips: "05117"
state: "AR"
demographics:
  population: 8064
  population_under_18: 1660
  population_18_64: 4504
  population_65_plus: 1900
  median_household_income: 51646
  poverty_rate: 11.84
  homeownership_rate: 75.77
  unemployment_rate: 3.04
  median_home_value: 96400
  gini_index: 0.4509
  vacancy_rate: 20.31
  race_white: 6758
  race_black: 796
  race_asian: 0
  race_native: 13
  hispanic: 192
  bachelors_plus: 1359
districts:
  - to: "us/states/ar/districts/01"
    rel: in-district
    area_weight: 0.9986
  - to: "us/states/ar/districts/senate/10"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ar/districts/house/60"
    rel: in-district
    area_weight: 0.6703
  - to: "us/states/ar/districts/house/61"
    rel: in-district
    area_weight: 0.3296
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Prairie County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8064 |
| Under 18 | 1660 |
| 18–64 | 4504 |
| 65+ | 1900 |
| Median household income | 51646 |
| Poverty rate | 11.84 |
| Homeownership rate | 75.77 |
| Unemployment rate | 3.04 |
| Median home value | 96400 |
| Gini index | 0.4509 |
| Vacancy rate | 20.31 |
| White | 6758 |
| Black | 796 |
| Asian | 0 |
| Native | 13 |
| Hispanic/Latino | 192 |
| Bachelor's or higher | 1359 |

## Districts

- [AR-01](/us/states/ar/districts/01.md) — 100% (congressional)
- [AR Senate District 10](/us/states/ar/districts/senate/10.md) — 100% (state senate)
- [AR House District 60](/us/states/ar/districts/house/60.md) — 67% (state house)
- [AR House District 61](/us/states/ar/districts/house/61.md) — 33% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
