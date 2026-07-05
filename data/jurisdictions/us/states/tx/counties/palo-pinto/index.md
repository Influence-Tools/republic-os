---
type: Jurisdiction
title: "Palo Pinto County, TX"
classification: county
fips: "48363"
state: "TX"
demographics:
  population: 29295
  population_under_18: 6809
  population_18_64: 16478
  population_65_plus: 6008
  median_household_income: 67674
  poverty_rate: 16.75
  homeownership_rate: 71.02
  unemployment_rate: 6.1
  median_home_value: 198000
  gini_index: 0.4492
  vacancy_rate: 26.12
  race_white: 23144
  race_black: 698
  race_asian: 255
  race_native: 370
  hispanic: 6034
  bachelors_plus: 4712
districts:
  - to: "us/states/tx/districts/25"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/senate/10"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/house/60"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Palo Pinto County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 29295 |
| Under 18 | 6809 |
| 18–64 | 16478 |
| 65+ | 6008 |
| Median household income | 67674 |
| Poverty rate | 16.75 |
| Homeownership rate | 71.02 |
| Unemployment rate | 6.1 |
| Median home value | 198000 |
| Gini index | 0.4492 |
| Vacancy rate | 26.12 |
| White | 23144 |
| Black | 698 |
| Asian | 255 |
| Native | 370 |
| Hispanic/Latino | 6034 |
| Bachelor's or higher | 4712 |

## Districts

- [TX-25](/us/states/tx/districts/25.md) — 100% (congressional)
- [TX Senate District 10](/us/states/tx/districts/senate/10.md) — 100% (state senate)
- [TX House District 60](/us/states/tx/districts/house/60.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
