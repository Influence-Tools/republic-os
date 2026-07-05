---
type: Jurisdiction
title: "Skamania County, WA"
classification: county
fips: "53059"
state: "WA"
demographics:
  population: 12402
  population_under_18: 2081
  population_18_64: 7297
  population_65_plus: 3024
  median_household_income: 93265
  poverty_rate: 8.07
  homeownership_rate: 80.02
  unemployment_rate: 5.19
  median_home_value: 529500
  gini_index: 0.4362
  vacancy_rate: 15.97
  race_white: 10742
  race_black: 98
  race_asian: 158
  race_native: 120
  hispanic: 832
  bachelors_plus: 3869
districts:
  - to: "us/states/wa/districts/03"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/wa/districts/senate/17"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/wa/districts/house/17"
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

# Skamania County, WA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12402 |
| Under 18 | 2081 |
| 18–64 | 7297 |
| 65+ | 3024 |
| Median household income | 93265 |
| Poverty rate | 8.07 |
| Homeownership rate | 80.02 |
| Unemployment rate | 5.19 |
| Median home value | 529500 |
| Gini index | 0.4362 |
| Vacancy rate | 15.97 |
| White | 10742 |
| Black | 98 |
| Asian | 158 |
| Native | 120 |
| Hispanic/Latino | 832 |
| Bachelor's or higher | 3869 |

## Districts

- [WA-03](/us/states/wa/districts/03.md) — 100% (congressional)
- [WA Senate District 17](/us/states/wa/districts/senate/17.md) — 100% (state senate)
- [WA House District 17](/us/states/wa/districts/house/17.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
