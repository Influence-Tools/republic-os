---
type: Jurisdiction
title: "Trumbull County, OH"
classification: county
fips: "39155"
state: "OH"
demographics:
  population: 200929
  population_under_18: 41363
  population_18_64: 114635
  population_65_plus: 44931
  median_household_income: 56435
  poverty_rate: 16.61
  homeownership_rate: 71.29
  unemployment_rate: 4.7
  median_home_value: 141800
  gini_index: 0.4498
  vacancy_rate: 8.38
  race_white: 171239
  race_black: 16379
  race_asian: 1091
  race_native: 154
  hispanic: 4601
  bachelors_plus: 40143
districts:
  - to: "us/states/oh/districts/14"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/oh/districts/senate/32"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/oh/districts/house/65"
    rel: in-district
    area_weight: 0.607
  - to: "us/states/oh/districts/house/64"
    rel: in-district
    area_weight: 0.3929
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Trumbull County, OH

County jurisdiction — 3 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 200929 |
| Under 18 | 41363 |
| 18–64 | 114635 |
| 65+ | 44931 |
| Median household income | 56435 |
| Poverty rate | 16.61 |
| Homeownership rate | 71.29 |
| Unemployment rate | 4.7 |
| Median home value | 141800 |
| Gini index | 0.4498 |
| Vacancy rate | 8.38 |
| White | 171239 |
| Black | 16379 |
| Asian | 1091 |
| Native | 154 |
| Hispanic/Latino | 4601 |
| Bachelor's or higher | 40143 |

## Districts

- [OH-14](/us/states/oh/districts/14.md) — 100% (congressional)
- [OH Senate District 32](/us/states/oh/districts/senate/32.md) — 100% (state senate)
- [OH House District 65](/us/states/oh/districts/house/65.md) — 61% (state house)
- [OH House District 64](/us/states/oh/districts/house/64.md) — 39% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
