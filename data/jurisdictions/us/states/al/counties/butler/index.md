---
type: Jurisdiction
title: "Butler County, AL"
classification: county
fips: "01013"
state: "AL"
demographics:
  population: 18630
  population_under_18: 4112
  population_18_64: 10417
  population_65_plus: 4101
  median_household_income: 44755
  poverty_rate: 22.41
  homeownership_rate: 65.84
  unemployment_rate: 6.47
  median_home_value: 99800
  gini_index: 0.5094
  vacancy_rate: 23.15
  race_white: 9468
  race_black: 8327
  race_asian: 248
  race_native: 85
  hispanic: 316
  bachelors_plus: 2497
districts:
  - to: "us/states/al/districts/02"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/al/districts/senate/23"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/al/districts/house/90"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Butler County, AL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 18630 |
| Under 18 | 4112 |
| 18–64 | 10417 |
| 65+ | 4101 |
| Median household income | 44755 |
| Poverty rate | 22.41 |
| Homeownership rate | 65.84 |
| Unemployment rate | 6.47 |
| Median home value | 99800 |
| Gini index | 0.5094 |
| Vacancy rate | 23.15 |
| White | 9468 |
| Black | 8327 |
| Asian | 248 |
| Native | 85 |
| Hispanic/Latino | 316 |
| Bachelor's or higher | 2497 |

## Districts

- [AL-02](/us/states/al/districts/02.md) — 100% (congressional)
- [AL Senate District 23](/us/states/al/districts/senate/23.md) — 100% (state senate)
- [AL House District 90](/us/states/al/districts/house/90.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
