---
type: Jurisdiction
title: "Wolfe County, KY"
classification: county
fips: "21237"
state: "KY"
demographics:
  population: 6443
  population_under_18: 1444
  population_18_64: 3750
  population_65_plus: 1249
  median_household_income: 30417
  poverty_rate: 37.74
  homeownership_rate: 73.55
  unemployment_rate: 13.13
  median_home_value: 75800
  gini_index: 0.4185
  vacancy_rate: 12.45
  race_white: 6126
  race_black: 10
  race_asian: 0
  race_native: 5
  hispanic: 102
  bachelors_plus: 613
districts:
  - to: "us/states/ky/districts/05"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ky/districts/senate/30"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ky/districts/house/89"
    rel: in-district
    area_weight: 0.999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Wolfe County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6443 |
| Under 18 | 1444 |
| 18–64 | 3750 |
| 65+ | 1249 |
| Median household income | 30417 |
| Poverty rate | 37.74 |
| Homeownership rate | 73.55 |
| Unemployment rate | 13.13 |
| Median home value | 75800 |
| Gini index | 0.4185 |
| Vacancy rate | 12.45 |
| White | 6126 |
| Black | 10 |
| Asian | 0 |
| Native | 5 |
| Hispanic/Latino | 102 |
| Bachelor's or higher | 613 |

## Districts

- [KY-05](/us/states/ky/districts/05.md) — 100% (congressional)
- [KY Senate District 30](/us/states/ky/districts/senate/30.md) — 100% (state senate)
- [KY House District 89](/us/states/ky/districts/house/89.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
