---
type: Jurisdiction
title: "Clayton County, IA"
classification: county
fips: "19043"
state: "IA"
demographics:
  population: 17013
  population_under_18: 3680
  population_18_64: 9073
  population_65_plus: 4260
  median_household_income: 67242
  poverty_rate: 10.91
  homeownership_rate: 77.99
  unemployment_rate: 2.52
  median_home_value: 168500
  gini_index: 0.4279
  vacancy_rate: 14.63
  race_white: 16159
  race_black: 112
  race_asian: 56
  race_native: 10
  hispanic: 394
  bachelors_plus: 2242
districts:
  - to: "us/states/ia/districts/02"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/senate/32"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ia/districts/house/64"
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

# Clayton County, IA

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 17013 |
| Under 18 | 3680 |
| 18–64 | 9073 |
| 65+ | 4260 |
| Median household income | 67242 |
| Poverty rate | 10.91 |
| Homeownership rate | 77.99 |
| Unemployment rate | 2.52 |
| Median home value | 168500 |
| Gini index | 0.4279 |
| Vacancy rate | 14.63 |
| White | 16159 |
| Black | 112 |
| Asian | 56 |
| Native | 10 |
| Hispanic/Latino | 394 |
| Bachelor's or higher | 2242 |

## Districts

- [IA-02](/us/states/ia/districts/02.md) — 100% (congressional)
- [IA Senate District 32](/us/states/ia/districts/senate/32.md) — 100% (state senate)
- [IA House District 64](/us/states/ia/districts/house/64.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
