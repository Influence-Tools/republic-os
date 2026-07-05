---
type: Jurisdiction
title: "Pocahontas County, IA"
classification: county
fips: "19151"
state: "IA"
demographics:
  population: 7046
  population_under_18: 1644
  population_18_64: 3720
  population_65_plus: 1682
  median_household_income: 61875
  poverty_rate: 10.33
  homeownership_rate: 77.27
  unemployment_rate: 5.4
  median_home_value: 98100
  gini_index: 0.3946
  vacancy_rate: 17.83
  race_white: 6327
  race_black: 91
  race_asian: 12
  race_native: 17
  hispanic: 412
  bachelors_plus: 1117
districts:
  - to: "us/states/ia/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ia/districts/senate/4"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ia/districts/house/7"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Pocahontas County, IA

County jurisdiction — 4 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7046 |
| Under 18 | 1644 |
| 18–64 | 3720 |
| 65+ | 1682 |
| Median household income | 61875 |
| Poverty rate | 10.33 |
| Homeownership rate | 77.27 |
| Unemployment rate | 5.4 |
| Median home value | 98100 |
| Gini index | 0.3946 |
| Vacancy rate | 17.83 |
| White | 6327 |
| Black | 91 |
| Asian | 12 |
| Native | 17 |
| Hispanic/Latino | 412 |
| Bachelor's or higher | 1117 |

## Districts

- [IA-04](/us/states/ia/districts/04.md) — 100% (congressional)
- [IA Senate District 4](/us/states/ia/districts/senate/4.md) — 100% (state senate)
- [IA House District 7](/us/states/ia/districts/house/7.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
