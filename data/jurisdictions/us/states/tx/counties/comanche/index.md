---
type: Jurisdiction
title: "Comanche County, TX"
classification: county
fips: "48093"
state: "TX"
demographics:
  population: 13950
  population_under_18: 3186
  population_18_64: 7426
  population_65_plus: 3338
  median_household_income: 59635
  poverty_rate: 16.16
  homeownership_rate: 80.45
  unemployment_rate: 6.21
  median_home_value: 155600
  gini_index: 0.4409
  vacancy_rate: 22.84
  race_white: 9727
  race_black: 60
  race_asian: 47
  race_native: 69
  hispanic: 4110
  bachelors_plus: 2755
districts:
  - to: "us/states/tx/districts/25"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/tx/districts/senate/22"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/68"
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

# Comanche County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13950 |
| Under 18 | 3186 |
| 18–64 | 7426 |
| 65+ | 3338 |
| Median household income | 59635 |
| Poverty rate | 16.16 |
| Homeownership rate | 80.45 |
| Unemployment rate | 6.21 |
| Median home value | 155600 |
| Gini index | 0.4409 |
| Vacancy rate | 22.84 |
| White | 9727 |
| Black | 60 |
| Asian | 47 |
| Native | 69 |
| Hispanic/Latino | 4110 |
| Bachelor's or higher | 2755 |

## Districts

- [TX-25](/us/states/tx/districts/25.md) — 100% (congressional)
- [TX Senate District 22](/us/states/tx/districts/senate/22.md) — 100% (state senate)
- [TX House District 68](/us/states/tx/districts/house/68.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
