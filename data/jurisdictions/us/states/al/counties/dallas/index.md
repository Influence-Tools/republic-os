---
type: Jurisdiction
title: "Dallas County, AL"
classification: county
fips: "01047"
state: "AL"
demographics:
  population: 36858
  population_under_18: 8705
  population_18_64: 20638
  population_65_plus: 7515
  median_household_income: 35627
  poverty_rate: 31.04
  homeownership_rate: 63.82
  unemployment_rate: 10.95
  median_home_value: 94600
  gini_index: 0.5024
  vacancy_rate: 15.78
  race_white: 9936
  race_black: 25810
  race_asian: 226
  race_native: 46
  hispanic: 360
  bachelors_plus: 5834
districts:
  - to: "us/states/al/districts/07"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/al/districts/senate/23"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/al/districts/house/67"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Dallas County, AL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 36858 |
| Under 18 | 8705 |
| 18–64 | 20638 |
| 65+ | 7515 |
| Median household income | 35627 |
| Poverty rate | 31.04 |
| Homeownership rate | 63.82 |
| Unemployment rate | 10.95 |
| Median home value | 94600 |
| Gini index | 0.5024 |
| Vacancy rate | 15.78 |
| White | 9936 |
| Black | 25810 |
| Asian | 226 |
| Native | 46 |
| Hispanic/Latino | 360 |
| Bachelor's or higher | 5834 |

## Districts

- [AL-07](/us/states/al/districts/07.md) — 100% (congressional)
- [AL Senate District 23](/us/states/al/districts/senate/23.md) — 100% (state senate)
- [AL House District 67](/us/states/al/districts/house/67.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
