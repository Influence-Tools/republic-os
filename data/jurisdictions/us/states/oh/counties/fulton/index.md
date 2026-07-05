---
type: Jurisdiction
title: "Fulton County, OH"
classification: county
fips: "39051"
state: "OH"
demographics:
  population: 42240
  population_under_18: 9750
  population_18_64: 24281
  population_65_plus: 8209
  median_household_income: 72864
  poverty_rate: 9.45
  homeownership_rate: 80.16
  unemployment_rate: 3.86
  median_home_value: 191000
  gini_index: 0.4161
  vacancy_rate: 4.24
  race_white: 37678
  race_black: 158
  race_asian: 183
  race_native: 116
  hispanic: 3938
  bachelors_plus: 8189
districts:
  - to: "us/states/oh/districts/09"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/oh/districts/senate/1"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/oh/districts/house/81"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Fulton County, OH

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 42240 |
| Under 18 | 9750 |
| 18–64 | 24281 |
| 65+ | 8209 |
| Median household income | 72864 |
| Poverty rate | 9.45 |
| Homeownership rate | 80.16 |
| Unemployment rate | 3.86 |
| Median home value | 191000 |
| Gini index | 0.4161 |
| Vacancy rate | 4.24 |
| White | 37678 |
| Black | 158 |
| Asian | 183 |
| Native | 116 |
| Hispanic/Latino | 3938 |
| Bachelor's or higher | 8189 |

## Districts

- [OH-09](/us/states/oh/districts/09.md) — 100% (congressional)
- [OH Senate District 1](/us/states/oh/districts/senate/1.md) — 100% (state senate)
- [OH House District 81](/us/states/oh/districts/house/81.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
