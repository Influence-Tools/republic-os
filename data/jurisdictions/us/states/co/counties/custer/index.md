---
type: Jurisdiction
title: "Custer County, CO"
classification: county
fips: "08027"
state: "CO"
demographics:
  population: 5247
  population_under_18: 719
  population_18_64: 2790
  population_65_plus: 1738
  median_household_income: 72674
  poverty_rate: 12.7
  homeownership_rate: 85.33
  unemployment_rate: 3.73
  median_home_value: 392100
  gini_index: 0.4664
  vacancy_rate: 42.3
  race_white: 4746
  race_black: 0
  race_asian: 56
  race_native: 6
  hispanic: 219
  bachelors_plus: 2584
districts:
  - to: "us/states/co/districts/07"
    rel: in-district
    area_weight: 0.9963
  - to: "us/states/co/districts/senate/4"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/co/districts/house/60"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Custer County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5247 |
| Under 18 | 719 |
| 18–64 | 2790 |
| 65+ | 1738 |
| Median household income | 72674 |
| Poverty rate | 12.7 |
| Homeownership rate | 85.33 |
| Unemployment rate | 3.73 |
| Median home value | 392100 |
| Gini index | 0.4664 |
| Vacancy rate | 42.3 |
| White | 4746 |
| Black | 0 |
| Asian | 56 |
| Native | 6 |
| Hispanic/Latino | 219 |
| Bachelor's or higher | 2584 |

## Districts

- [CO-07](/us/states/co/districts/07.md) — 100% (congressional)
- [CO Senate District 4](/us/states/co/districts/senate/4.md) — 100% (state senate)
- [CO House District 60](/us/states/co/districts/house/60.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
