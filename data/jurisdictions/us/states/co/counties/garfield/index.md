---
type: Jurisdiction
title: "Garfield County, CO"
classification: county
fips: "08045"
state: "CO"
demographics:
  population: 62479
  population_under_18: 15339
  population_18_64: 37918
  population_65_plus: 9222
  median_household_income: 91131
  poverty_rate: 8.21
  homeownership_rate: 69.61
  unemployment_rate: 3.37
  median_home_value: 527800
  gini_index: 0.421
  vacancy_rate: 6.21
  race_white: 42812
  race_black: 577
  race_asian: 544
  race_native: 307
  hispanic: 20377
  bachelors_plus: 19229
districts:
  - to: "us/states/co/districts/03"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/co/districts/senate/8"
    rel: in-district
    area_weight: 0.7811
  - to: "us/states/co/districts/senate/5"
    rel: in-district
    area_weight: 0.2188
  - to: "us/states/co/districts/house/57"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, co]
timestamp: "2026-07-03"
---

# Garfield County, CO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 62479 |
| Under 18 | 15339 |
| 18–64 | 37918 |
| 65+ | 9222 |
| Median household income | 91131 |
| Poverty rate | 8.21 |
| Homeownership rate | 69.61 |
| Unemployment rate | 3.37 |
| Median home value | 527800 |
| Gini index | 0.421 |
| Vacancy rate | 6.21 |
| White | 42812 |
| Black | 577 |
| Asian | 544 |
| Native | 307 |
| Hispanic/Latino | 20377 |
| Bachelor's or higher | 19229 |

## Districts

- [CO-03](/us/states/co/districts/03.md) — 100% (congressional)
- [CO Senate District 8](/us/states/co/districts/senate/8.md) — 78% (state senate)
- [CO Senate District 5](/us/states/co/districts/senate/5.md) — 22% (state senate)
- [CO House District 57](/us/states/co/districts/house/57.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
