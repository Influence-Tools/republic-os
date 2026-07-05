---
type: Jurisdiction
title: "Hale County, TX"
classification: county
fips: "48189"
state: "TX"
demographics:
  population: 32131
  population_under_18: 8446
  population_18_64: 19110
  population_65_plus: 4575
  median_household_income: 51897
  poverty_rate: 20.54
  homeownership_rate: 60.54
  unemployment_rate: 5.28
  median_home_value: 116500
  gini_index: 0.4589
  vacancy_rate: 17.68
  race_white: 16893
  race_black: 1489
  race_asian: 288
  race_native: 523
  hispanic: 19688
  bachelors_plus: 4179
districts:
  - to: "us/states/tx/districts/19"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/28"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/88"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Hale County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 32131 |
| Under 18 | 8446 |
| 18–64 | 19110 |
| 65+ | 4575 |
| Median household income | 51897 |
| Poverty rate | 20.54 |
| Homeownership rate | 60.54 |
| Unemployment rate | 5.28 |
| Median home value | 116500 |
| Gini index | 0.4589 |
| Vacancy rate | 17.68 |
| White | 16893 |
| Black | 1489 |
| Asian | 288 |
| Native | 523 |
| Hispanic/Latino | 19688 |
| Bachelor's or higher | 4179 |

## Districts

- [TX-19](/us/states/tx/districts/19.md) — 100% (congressional)
- [TX Senate District 28](/us/states/tx/districts/senate/28.md) — 100% (state senate)
- [TX House District 88](/us/states/tx/districts/house/88.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
