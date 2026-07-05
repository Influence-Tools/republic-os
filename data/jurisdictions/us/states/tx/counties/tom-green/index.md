---
type: Jurisdiction
title: "Tom Green County, TX"
classification: county
fips: "48451"
state: "TX"
demographics:
  population: 119577
  population_under_18: 28396
  population_18_64: 70886
  population_65_plus: 20295
  median_household_income: 68370
  poverty_rate: 11.11
  homeownership_rate: 65.15
  unemployment_rate: 3.66
  median_home_value: 197000
  gini_index: 0.4512
  vacancy_rate: 10.63
  race_white: 75400
  race_black: 4703
  race_asian: 1669
  race_native: 549
  hispanic: 48530
  bachelors_plus: 26782
districts:
  - to: "us/states/tx/districts/11"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/28"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/house/72"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Tom Green County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 119577 |
| Under 18 | 28396 |
| 18–64 | 70886 |
| 65+ | 20295 |
| Median household income | 68370 |
| Poverty rate | 11.11 |
| Homeownership rate | 65.15 |
| Unemployment rate | 3.66 |
| Median home value | 197000 |
| Gini index | 0.4512 |
| Vacancy rate | 10.63 |
| White | 75400 |
| Black | 4703 |
| Asian | 1669 |
| Native | 549 |
| Hispanic/Latino | 48530 |
| Bachelor's or higher | 26782 |

## Districts

- [TX-11](/us/states/tx/districts/11.md) — 100% (congressional)
- [TX Senate District 28](/us/states/tx/districts/senate/28.md) — 100% (state senate)
- [TX House District 72](/us/states/tx/districts/house/72.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
