---
type: Jurisdiction
title: "Asotin County, WA"
classification: county
fips: "53003"
state: "WA"
demographics:
  population: 22467
  population_under_18: 4400
  population_18_64: 12406
  population_65_plus: 5661
  median_household_income: 72283
  poverty_rate: 14.16
  homeownership_rate: 73.23
  unemployment_rate: 5.01
  median_home_value: 325600
  gini_index: 0.4556
  vacancy_rate: 6.81
  race_white: 19815
  race_black: 210
  race_asian: 256
  race_native: 254
  hispanic: 1028
  bachelors_plus: 5617
districts:
  - to: "us/states/wa/districts/05"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/wa/districts/senate/9"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/wa/districts/house/9"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wa]
timestamp: "2026-07-03"
---

# Asotin County, WA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 22467 |
| Under 18 | 4400 |
| 18–64 | 12406 |
| 65+ | 5661 |
| Median household income | 72283 |
| Poverty rate | 14.16 |
| Homeownership rate | 73.23 |
| Unemployment rate | 5.01 |
| Median home value | 325600 |
| Gini index | 0.4556 |
| Vacancy rate | 6.81 |
| White | 19815 |
| Black | 210 |
| Asian | 256 |
| Native | 254 |
| Hispanic/Latino | 1028 |
| Bachelor's or higher | 5617 |

## Districts

- [WA-05](/us/states/wa/districts/05.md) — 100% (congressional)
- [WA Senate District 9](/us/states/wa/districts/senate/9.md) — 100% (state senate)
- [WA House District 9](/us/states/wa/districts/house/9.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
