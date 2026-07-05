---
type: Jurisdiction
title: "Winneshiek County, IA"
classification: county
fips: "19191"
state: "IA"
demographics:
  population: 19873
  population_under_18: 3714
  population_18_64: 11527
  population_65_plus: 4632
  median_household_income: 79066
  poverty_rate: 8.4
  homeownership_rate: 74.2
  unemployment_rate: 2.32
  median_home_value: 259200
  gini_index: 0.4441
  vacancy_rate: 9.86
  race_white: 18578
  race_black: 81
  race_asian: 107
  race_native: 73
  hispanic: 612
  bachelors_plus: 5596
districts:
  - to: "us/states/ia/districts/02"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ia/districts/senate/32"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/house/63"
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

# Winneshiek County, IA

County jurisdiction — 3 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 19873 |
| Under 18 | 3714 |
| 18–64 | 11527 |
| 65+ | 4632 |
| Median household income | 79066 |
| Poverty rate | 8.4 |
| Homeownership rate | 74.2 |
| Unemployment rate | 2.32 |
| Median home value | 259200 |
| Gini index | 0.4441 |
| Vacancy rate | 9.86 |
| White | 18578 |
| Black | 81 |
| Asian | 107 |
| Native | 73 |
| Hispanic/Latino | 612 |
| Bachelor's or higher | 5596 |

## Districts

- [IA-02](/us/states/ia/districts/02.md) — 100% (congressional)
- [IA Senate District 32](/us/states/ia/districts/senate/32.md) — 100% (state senate)
- [IA House District 63](/us/states/ia/districts/house/63.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
