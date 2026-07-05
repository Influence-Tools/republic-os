---
type: Jurisdiction
title: "Abbeville County, SC"
classification: county
fips: "45001"
state: "SC"
demographics:
  population: 24420
  population_under_18: 4797
  population_18_64: 14025
  population_65_plus: 5598
  median_household_income: 52935
  poverty_rate: 15.66
  homeownership_rate: 78.14
  unemployment_rate: 4.02
  median_home_value: 178800
  gini_index: 0.4877
  vacancy_rate: 17.31
  race_white: 16916
  race_black: 6212
  race_asian: 50
  race_native: 5
  hispanic: 526
  bachelors_plus: 4667
districts:
  - to: "us/states/sc/districts/03"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/sc/districts/senate/4"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/sc/districts/house/11"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sc]
timestamp: "2026-07-03"
---

# Abbeville County, SC

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 24420 |
| Under 18 | 4797 |
| 18–64 | 14025 |
| 65+ | 5598 |
| Median household income | 52935 |
| Poverty rate | 15.66 |
| Homeownership rate | 78.14 |
| Unemployment rate | 4.02 |
| Median home value | 178800 |
| Gini index | 0.4877 |
| Vacancy rate | 17.31 |
| White | 16916 |
| Black | 6212 |
| Asian | 50 |
| Native | 5 |
| Hispanic/Latino | 526 |
| Bachelor's or higher | 4667 |

## Districts

- [SC-03](/us/states/sc/districts/03.md) — 100% (congressional)
- [SC Senate District 4](/us/states/sc/districts/senate/4.md) — 100% (state senate)
- [SC House District 11](/us/states/sc/districts/house/11.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
