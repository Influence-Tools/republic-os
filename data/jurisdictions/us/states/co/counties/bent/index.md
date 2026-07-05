---
type: Jurisdiction
title: "Bent County, CO"
classification: county
fips: "08011"
state: "CO"
demographics:
  population: 5549
  population_under_18: 889
  population_18_64: 3612
  population_65_plus: 1048
  median_household_income: 50179
  poverty_rate: 28.36
  homeownership_rate: 65.17
  unemployment_rate: 5.77
  median_home_value: 146900
  gini_index: 0.4409
  vacancy_rate: 13.75
  race_white: 3737
  race_black: 179
  race_asian: 52
  race_native: 128
  hispanic: 1801
  bachelors_plus: 901
districts:
  - to: "us/states/co/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/co/districts/senate/35"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/co/districts/house/47"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Bent County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5549 |
| Under 18 | 889 |
| 18–64 | 3612 |
| 65+ | 1048 |
| Median household income | 50179 |
| Poverty rate | 28.36 |
| Homeownership rate | 65.17 |
| Unemployment rate | 5.77 |
| Median home value | 146900 |
| Gini index | 0.4409 |
| Vacancy rate | 13.75 |
| White | 3737 |
| Black | 179 |
| Asian | 52 |
| Native | 128 |
| Hispanic/Latino | 1801 |
| Bachelor's or higher | 901 |

## Districts

- [CO-04](/us/states/co/districts/04.md) — 100% (congressional)
- [CO Senate District 35](/us/states/co/districts/senate/35.md) — 100% (state senate)
- [CO House District 47](/us/states/co/districts/house/47.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
