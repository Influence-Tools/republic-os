---
type: Jurisdiction
title: "Wasco County, OR"
classification: county
fips: "41065"
state: "OR"
demographics:
  population: 26552
  population_under_18: 5682
  population_18_64: 15185
  population_65_plus: 5685
  median_household_income: 64175
  poverty_rate: 11.63
  homeownership_rate: 67.51
  unemployment_rate: 7.66
  median_home_value: 367400
  gini_index: 0.4878
  vacancy_rate: 13.4
  race_white: 20024
  race_black: 114
  race_asian: 185
  race_native: 522
  hispanic: 5470
  bachelors_plus: 5862
districts:
  - to: "us/states/or/districts/02"
    rel: in-district
    area_weight: 0.9991
  - to: "us/states/or/districts/senate/29"
    rel: in-district
    area_weight: 0.9526
  - to: "us/states/or/districts/senate/26"
    rel: in-district
    area_weight: 0.0472
  - to: "us/states/or/districts/house/57"
    rel: in-district
    area_weight: 0.9526
  - to: "us/states/or/districts/house/52"
    rel: in-district
    area_weight: 0.0472
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, or]
timestamp: "2026-07-03"
---

# Wasco County, OR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 26552 |
| Under 18 | 5682 |
| 18–64 | 15185 |
| 65+ | 5685 |
| Median household income | 64175 |
| Poverty rate | 11.63 |
| Homeownership rate | 67.51 |
| Unemployment rate | 7.66 |
| Median home value | 367400 |
| Gini index | 0.4878 |
| Vacancy rate | 13.4 |
| White | 20024 |
| Black | 114 |
| Asian | 185 |
| Native | 522 |
| Hispanic/Latino | 5470 |
| Bachelor's or higher | 5862 |

## Districts

- [OR-02](/us/states/or/districts/02.md) — 100% (congressional)
- [OR Senate District 29](/us/states/or/districts/senate/29.md) — 95% (state senate)
- [OR Senate District 26](/us/states/or/districts/senate/26.md) — 5% (state senate)
- [OR House District 57](/us/states/or/districts/house/57.md) — 95% (state house)
- [OR House District 52](/us/states/or/districts/house/52.md) — 5% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
