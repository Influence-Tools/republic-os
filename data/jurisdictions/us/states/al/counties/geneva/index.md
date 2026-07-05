---
type: Jurisdiction
title: "Geneva County, AL"
classification: county
fips: "01061"
state: "AL"
demographics:
  population: 26887
  population_under_18: 5905
  population_18_64: 15530
  population_65_plus: 5452
  median_household_income: 52771
  poverty_rate: 19.18
  homeownership_rate: 78.11
  unemployment_rate: 5.63
  median_home_value: 130700
  gini_index: 0.4241
  vacancy_rate: 15.39
  race_white: 22492
  race_black: 2316
  race_asian: 168
  race_native: 66
  hispanic: 1437
  bachelors_plus: 3231
districts:
  - to: "us/states/al/districts/01"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/al/districts/senate/29"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/al/districts/house/87"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Geneva County, AL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 26887 |
| Under 18 | 5905 |
| 18–64 | 15530 |
| 65+ | 5452 |
| Median household income | 52771 |
| Poverty rate | 19.18 |
| Homeownership rate | 78.11 |
| Unemployment rate | 5.63 |
| Median home value | 130700 |
| Gini index | 0.4241 |
| Vacancy rate | 15.39 |
| White | 22492 |
| Black | 2316 |
| Asian | 168 |
| Native | 66 |
| Hispanic/Latino | 1437 |
| Bachelor's or higher | 3231 |

## Districts

- [AL-01](/us/states/al/districts/01.md) — 100% (congressional)
- [AL Senate District 29](/us/states/al/districts/senate/29.md) — 100% (state senate)
- [AL House District 87](/us/states/al/districts/house/87.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
