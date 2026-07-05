---
type: Jurisdiction
title: "Titus County, TX"
classification: county
fips: "48449"
state: "TX"
demographics:
  population: 31363
  population_under_18: 8837
  population_18_64: 17763
  population_65_plus: 4763
  median_household_income: 58425
  poverty_rate: 17.1
  homeownership_rate: 70.6
  unemployment_rate: 3.09
  median_home_value: 174000
  gini_index: 0.4437
  vacancy_rate: 8.15
  race_white: 16774
  race_black: 3222
  race_asian: 0
  race_native: 210
  hispanic: 14103
  bachelors_plus: 4087
districts:
  - to: "us/states/tx/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/1"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/5"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Titus County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 31363 |
| Under 18 | 8837 |
| 18–64 | 17763 |
| 65+ | 4763 |
| Median household income | 58425 |
| Poverty rate | 17.1 |
| Homeownership rate | 70.6 |
| Unemployment rate | 3.09 |
| Median home value | 174000 |
| Gini index | 0.4437 |
| Vacancy rate | 8.15 |
| White | 16774 |
| Black | 3222 |
| Asian | 0 |
| Native | 210 |
| Hispanic/Latino | 14103 |
| Bachelor's or higher | 4087 |

## Districts

- [TX-01](/us/states/tx/districts/01.md) — 100% (congressional)
- [TX Senate District 1](/us/states/tx/districts/senate/1.md) — 100% (state senate)
- [TX House District 5](/us/states/tx/districts/house/5.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
