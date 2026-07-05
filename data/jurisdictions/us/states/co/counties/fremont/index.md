---
type: Jurisdiction
title: "Fremont County, CO"
classification: county
fips: "08043"
state: "CO"
demographics:
  population: 49634
  population_under_18: 7936
  population_18_64: 30327
  population_65_plus: 11371
  median_household_income: 62664
  poverty_rate: 13.35
  homeownership_rate: 75.63
  unemployment_rate: 4.26
  median_home_value: 324000
  gini_index: 0.4732
  vacancy_rate: 12.76
  race_white: 41815
  race_black: 1693
  race_asian: 457
  race_native: 1029
  hispanic: 6546
  bachelors_plus: 10947
districts:
  - to: "us/states/co/districts/07"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/co/districts/senate/4"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/co/districts/house/60"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Fremont County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 49634 |
| Under 18 | 7936 |
| 18–64 | 30327 |
| 65+ | 11371 |
| Median household income | 62664 |
| Poverty rate | 13.35 |
| Homeownership rate | 75.63 |
| Unemployment rate | 4.26 |
| Median home value | 324000 |
| Gini index | 0.4732 |
| Vacancy rate | 12.76 |
| White | 41815 |
| Black | 1693 |
| Asian | 457 |
| Native | 1029 |
| Hispanic/Latino | 6546 |
| Bachelor's or higher | 10947 |

## Districts

- [CO-07](/us/states/co/districts/07.md) — 100% (congressional)
- [CO Senate District 4](/us/states/co/districts/senate/4.md) — 100% (state senate)
- [CO House District 60](/us/states/co/districts/house/60.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
