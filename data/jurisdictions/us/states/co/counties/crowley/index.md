---
type: Jurisdiction
title: "Crowley County, CO"
classification: county
fips: "08025"
state: "CO"
demographics:
  population: 5647
  population_under_18: 735
  population_18_64: 4038
  population_65_plus: 874
  median_household_income: 48826
  poverty_rate: 19.41
  homeownership_rate: 69.48
  unemployment_rate: 3.91
  median_home_value: 116200
  gini_index: 0.4541
  vacancy_rate: 14.07
  race_white: 3607
  race_black: 371
  race_asian: 95
  race_native: 258
  hispanic: 1637
  bachelors_plus: 735
districts:
  - to: "us/states/co/districts/04"
    rel: in-district
    area_weight: 0.997
  - to: "us/states/co/districts/senate/35"
    rel: in-district
    area_weight: 0.9988
  - to: "us/states/co/districts/house/47"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Crowley County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5647 |
| Under 18 | 735 |
| 18–64 | 4038 |
| 65+ | 874 |
| Median household income | 48826 |
| Poverty rate | 19.41 |
| Homeownership rate | 69.48 |
| Unemployment rate | 3.91 |
| Median home value | 116200 |
| Gini index | 0.4541 |
| Vacancy rate | 14.07 |
| White | 3607 |
| Black | 371 |
| Asian | 95 |
| Native | 258 |
| Hispanic/Latino | 1637 |
| Bachelor's or higher | 735 |

## Districts

- [CO-04](/us/states/co/districts/04.md) — 100% (congressional)
- [CO Senate District 35](/us/states/co/districts/senate/35.md) — 100% (state senate)
- [CO House District 47](/us/states/co/districts/house/47.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
