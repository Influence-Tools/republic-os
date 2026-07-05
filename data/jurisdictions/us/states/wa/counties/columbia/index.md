---
type: Jurisdiction
title: "Columbia County, WA"
classification: county
fips: "53013"
state: "WA"
demographics:
  population: 4014
  population_under_18: 723
  population_18_64: 2114
  population_65_plus: 1177
  median_household_income: 71810
  poverty_rate: 9.31
  homeownership_rate: 77.71
  unemployment_rate: 3.87
  median_home_value: 271200
  gini_index: 0.4324
  vacancy_rate: 16.01
  race_white: 3337
  race_black: 22
  race_asian: 75
  race_native: 13
  hispanic: 335
  bachelors_plus: 1065
districts:
  - to: "us/states/wa/districts/05"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/wa/districts/senate/9"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/wa/districts/house/9"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wa]
timestamp: "2026-07-03"
---

# Columbia County, WA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4014 |
| Under 18 | 723 |
| 18–64 | 2114 |
| 65+ | 1177 |
| Median household income | 71810 |
| Poverty rate | 9.31 |
| Homeownership rate | 77.71 |
| Unemployment rate | 3.87 |
| Median home value | 271200 |
| Gini index | 0.4324 |
| Vacancy rate | 16.01 |
| White | 3337 |
| Black | 22 |
| Asian | 75 |
| Native | 13 |
| Hispanic/Latino | 335 |
| Bachelor's or higher | 1065 |

## Districts

- [WA-05](/us/states/wa/districts/05.md) — 100% (congressional)
- [WA Senate District 9](/us/states/wa/districts/senate/9.md) — 100% (state senate)
- [WA House District 9](/us/states/wa/districts/house/9.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
