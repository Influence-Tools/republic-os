---
type: Jurisdiction
title: "Perry County, AR"
classification: county
fips: "05105"
state: "AR"
demographics:
  population: 10101
  population_under_18: 2202
  population_18_64: 5769
  population_65_plus: 2130
  median_household_income: 55764
  poverty_rate: 14.24
  homeownership_rate: 80.39
  unemployment_rate: 4.13
  median_home_value: 130200
  gini_index: 0.4275
  vacancy_rate: 17.66
  race_white: 9104
  race_black: 312
  race_asian: 12
  race_native: 40
  hispanic: 353
  bachelors_plus: 1527
districts:
  - to: "us/states/ar/districts/02"
    rel: in-district
    area_weight: 0.9986
  - to: "us/states/ar/districts/senate/5"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ar/districts/house/54"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Perry County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10101 |
| Under 18 | 2202 |
| 18–64 | 5769 |
| 65+ | 2130 |
| Median household income | 55764 |
| Poverty rate | 14.24 |
| Homeownership rate | 80.39 |
| Unemployment rate | 4.13 |
| Median home value | 130200 |
| Gini index | 0.4275 |
| Vacancy rate | 17.66 |
| White | 9104 |
| Black | 312 |
| Asian | 12 |
| Native | 40 |
| Hispanic/Latino | 353 |
| Bachelor's or higher | 1527 |

## Districts

- [AR-02](/us/states/ar/districts/02.md) — 100% (congressional)
- [AR Senate District 5](/us/states/ar/districts/senate/5.md) — 100% (state senate)
- [AR House District 54](/us/states/ar/districts/house/54.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
