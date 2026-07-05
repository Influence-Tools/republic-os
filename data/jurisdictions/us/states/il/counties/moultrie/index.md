---
type: Jurisdiction
title: "Moultrie County, IL"
classification: county
fips: "17139"
state: "IL"
demographics:
  population: 14424
  population_under_18: 3632
  population_18_64: 8053
  population_65_plus: 2739
  median_household_income: 71784
  poverty_rate: 9.16
  homeownership_rate: 75.98
  unemployment_rate: 2.19
  median_home_value: 134000
  gini_index: 0.4252
  vacancy_rate: 6.78
  race_white: 13753
  race_black: 150
  race_asian: 8
  race_native: 0
  hispanic: 241
  bachelors_plus: 2493
districts:
  - to: "us/states/il/districts/15"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/il/districts/senate/54"
    rel: in-district
    area_weight: 0.9689
  - to: "us/states/il/districts/senate/51"
    rel: in-district
    area_weight: 0.0311
  - to: "us/states/il/districts/house/107"
    rel: in-district
    area_weight: 0.9689
  - to: "us/states/il/districts/house/101"
    rel: in-district
    area_weight: 0.0311
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Moultrie County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14424 |
| Under 18 | 3632 |
| 18–64 | 8053 |
| 65+ | 2739 |
| Median household income | 71784 |
| Poverty rate | 9.16 |
| Homeownership rate | 75.98 |
| Unemployment rate | 2.19 |
| Median home value | 134000 |
| Gini index | 0.4252 |
| Vacancy rate | 6.78 |
| White | 13753 |
| Black | 150 |
| Asian | 8 |
| Native | 0 |
| Hispanic/Latino | 241 |
| Bachelor's or higher | 2493 |

## Districts

- [IL-15](/us/states/il/districts/15.md) — 100% (congressional)
- [IL Senate District 54](/us/states/il/districts/senate/54.md) — 97% (state senate)
- [IL Senate District 51](/us/states/il/districts/senate/51.md) — 3% (state senate)
- [IL House District 107](/us/states/il/districts/house/107.md) — 97% (state house)
- [IL House District 101](/us/states/il/districts/house/101.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
