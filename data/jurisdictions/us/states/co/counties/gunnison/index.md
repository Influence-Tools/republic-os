---
type: Jurisdiction
title: "Gunnison County, CO"
classification: county
fips: "08051"
state: "CO"
demographics:
  population: 17241
  population_under_18: 2614
  population_18_64: 12024
  population_65_plus: 2603
  median_household_income: 84527
  poverty_rate: 11.27
  homeownership_rate: 66.79
  unemployment_rate: 4.67
  median_home_value: 621800
  gini_index: 0.446
  vacancy_rate: 32.08
  race_white: 15012
  race_black: 284
  race_asian: 158
  race_native: 108
  hispanic: 1727
  bachelors_plus: 9680
districts:
  - to: "us/states/co/districts/03"
    rel: in-district
    area_weight: 0.9991
  - to: "us/states/co/districts/senate/5"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/co/districts/house/58"
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

# Gunnison County, CO

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 17241 |
| Under 18 | 2614 |
| 18–64 | 12024 |
| 65+ | 2603 |
| Median household income | 84527 |
| Poverty rate | 11.27 |
| Homeownership rate | 66.79 |
| Unemployment rate | 4.67 |
| Median home value | 621800 |
| Gini index | 0.446 |
| Vacancy rate | 32.08 |
| White | 15012 |
| Black | 284 |
| Asian | 158 |
| Native | 108 |
| Hispanic/Latino | 1727 |
| Bachelor's or higher | 9680 |

## Districts

- [CO-03](/us/states/co/districts/03.md) — 100% (congressional)
- [CO Senate District 5](/us/states/co/districts/senate/5.md) — 100% (state senate)
- [CO House District 58](/us/states/co/districts/house/58.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
