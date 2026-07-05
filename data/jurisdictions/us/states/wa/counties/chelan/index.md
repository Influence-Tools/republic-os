---
type: Jurisdiction
title: "Chelan County, WA"
classification: county
fips: "53007"
state: "WA"
demographics:
  population: 80172
  population_under_18: 18109
  population_18_64: 45294
  population_65_plus: 16769
  median_household_income: 82381
  poverty_rate: 8.27
  homeownership_rate: 64.6
  unemployment_rate: 3.74
  median_home_value: 490100
  gini_index: 0.4651
  vacancy_rate: 18.5
  race_white: 53704
  race_black: 425
  race_asian: 661
  race_native: 887
  hispanic: 23247
  bachelors_plus: 23640
districts:
  - to: "us/states/wa/districts/08"
    rel: in-district
    area_weight: 0.9978
  - to: "us/states/wa/districts/senate/12"
    rel: in-district
    area_weight: 0.9985
  - to: "us/states/wa/districts/house/12"
    rel: in-district
    area_weight: 0.9985
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wa]
timestamp: "2026-07-03"
---

# Chelan County, WA

County jurisdiction — 3 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 80172 |
| Under 18 | 18109 |
| 18–64 | 45294 |
| 65+ | 16769 |
| Median household income | 82381 |
| Poverty rate | 8.27 |
| Homeownership rate | 64.6 |
| Unemployment rate | 3.74 |
| Median home value | 490100 |
| Gini index | 0.4651 |
| Vacancy rate | 18.5 |
| White | 53704 |
| Black | 425 |
| Asian | 661 |
| Native | 887 |
| Hispanic/Latino | 23247 |
| Bachelor's or higher | 23640 |

## Districts

- [WA-08](/us/states/wa/districts/08.md) — 100% (congressional)
- [WA Senate District 12](/us/states/wa/districts/senate/12.md) — 100% (state senate)
- [WA House District 12](/us/states/wa/districts/house/12.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
