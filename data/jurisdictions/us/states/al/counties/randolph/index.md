---
type: Jurisdiction
title: "Randolph County, AL"
classification: county
fips: "01111"
state: "AL"
demographics:
  population: 22510
  population_under_18: 5246
  population_18_64: 6488
  population_65_plus: 10776
  median_household_income: 52338
  poverty_rate: 19.91
  homeownership_rate: 77.21
  unemployment_rate: 3.77
  median_home_value: 181600
  gini_index: 0.4781
  vacancy_rate: 25.86
  race_white: 17027
  race_black: 3496
  race_asian: 128
  race_native: 35
  hispanic: 669
  bachelors_plus: 4105
districts:
  - to: "us/states/al/districts/03"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/al/districts/senate/13"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/al/districts/house/37"
    rel: in-district
    area_weight: 0.9994
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Randolph County, AL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 22510 |
| Under 18 | 5246 |
| 18–64 | 6488 |
| 65+ | 10776 |
| Median household income | 52338 |
| Poverty rate | 19.91 |
| Homeownership rate | 77.21 |
| Unemployment rate | 3.77 |
| Median home value | 181600 |
| Gini index | 0.4781 |
| Vacancy rate | 25.86 |
| White | 17027 |
| Black | 3496 |
| Asian | 128 |
| Native | 35 |
| Hispanic/Latino | 669 |
| Bachelor's or higher | 4105 |

## Districts

- [AL-03](/us/states/al/districts/03.md) — 100% (congressional)
- [AL Senate District 13](/us/states/al/districts/senate/13.md) — 100% (state senate)
- [AL House District 37](/us/states/al/districts/house/37.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
