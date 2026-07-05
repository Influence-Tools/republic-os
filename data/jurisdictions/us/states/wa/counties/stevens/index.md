---
type: Jurisdiction
title: "Stevens County, WA"
classification: county
fips: "53065"
state: "WA"
demographics:
  population: 48067
  population_under_18: 10166
  population_18_64: 25723
  population_65_plus: 12178
  median_household_income: 69327
  poverty_rate: 12.04
  homeownership_rate: 79.82
  unemployment_rate: 5.3
  median_home_value: 350600
  gini_index: 0.4589
  vacancy_rate: 14.96
  race_white: 40868
  race_black: 197
  race_asian: 430
  race_native: 1954
  hispanic: 2012
  bachelors_plus: 10492
districts:
  - to: "us/states/wa/districts/05"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/wa/districts/senate/7"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/wa/districts/house/7"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wa]
timestamp: "2026-07-03"
---

# Stevens County, WA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 48067 |
| Under 18 | 10166 |
| 18–64 | 25723 |
| 65+ | 12178 |
| Median household income | 69327 |
| Poverty rate | 12.04 |
| Homeownership rate | 79.82 |
| Unemployment rate | 5.3 |
| Median home value | 350600 |
| Gini index | 0.4589 |
| Vacancy rate | 14.96 |
| White | 40868 |
| Black | 197 |
| Asian | 430 |
| Native | 1954 |
| Hispanic/Latino | 2012 |
| Bachelor's or higher | 10492 |

## Districts

- [WA-05](/us/states/wa/districts/05.md) — 100% (congressional)
- [WA Senate District 7](/us/states/wa/districts/senate/7.md) — 100% (state senate)
- [WA House District 7](/us/states/wa/districts/house/7.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
