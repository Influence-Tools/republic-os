---
type: Jurisdiction
title: "Ashe County, NC"
classification: county
fips: "37009"
state: "NC"
demographics:
  population: 26950
  population_under_18: 4547
  population_18_64: 15060
  population_65_plus: 7343
  median_household_income: 56866
  poverty_rate: 13.49
  homeownership_rate: 79.38
  unemployment_rate: 4.8
  median_home_value: 243100
  gini_index: 0.4431
  vacancy_rate: 29.14
  race_white: 25019
  race_black: 272
  race_asian: 119
  race_native: 139
  hispanic: 1630
  bachelors_plus: 7102
districts:
  - to: "us/states/nc/districts/05"
    rel: in-district
    area_weight: 0.999
  - to: "us/states/nc/districts/senate/47"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/nc/districts/house/93"
    rel: in-district
    area_weight: 0.9994
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Ashe County, NC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 26950 |
| Under 18 | 4547 |
| 18–64 | 15060 |
| 65+ | 7343 |
| Median household income | 56866 |
| Poverty rate | 13.49 |
| Homeownership rate | 79.38 |
| Unemployment rate | 4.8 |
| Median home value | 243100 |
| Gini index | 0.4431 |
| Vacancy rate | 29.14 |
| White | 25019 |
| Black | 272 |
| Asian | 119 |
| Native | 139 |
| Hispanic/Latino | 1630 |
| Bachelor's or higher | 7102 |

## Districts

- [NC-05](/us/states/nc/districts/05.md) — 100% (congressional)
- [NC Senate District 47](/us/states/nc/districts/senate/47.md) — 100% (state senate)
- [NC House District 93](/us/states/nc/districts/house/93.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
