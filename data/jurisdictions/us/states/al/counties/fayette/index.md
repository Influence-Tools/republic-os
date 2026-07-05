---
type: Jurisdiction
title: "Fayette County, AL"
classification: county
fips: "01057"
state: "AL"
demographics:
  population: 16053
  population_under_18: 3410
  population_18_64: 9134
  population_65_plus: 3509
  median_household_income: 49488
  poverty_rate: 21.81
  homeownership_rate: 78.42
  unemployment_rate: 8.44
  median_home_value: 125900
  gini_index: 0.4942
  vacancy_rate: 19.91
  race_white: 13512
  race_black: 1777
  race_asian: 8
  race_native: 22
  hispanic: 150
  bachelors_plus: 2227
districts:
  - to: "us/states/al/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/al/districts/senate/5"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/al/districts/house/16"
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

# Fayette County, AL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16053 |
| Under 18 | 3410 |
| 18–64 | 9134 |
| 65+ | 3509 |
| Median household income | 49488 |
| Poverty rate | 21.81 |
| Homeownership rate | 78.42 |
| Unemployment rate | 8.44 |
| Median home value | 125900 |
| Gini index | 0.4942 |
| Vacancy rate | 19.91 |
| White | 13512 |
| Black | 1777 |
| Asian | 8 |
| Native | 22 |
| Hispanic/Latino | 150 |
| Bachelor's or higher | 2227 |

## Districts

- [AL-04](/us/states/al/districts/04.md) — 100% (congressional)
- [AL Senate District 5](/us/states/al/districts/senate/5.md) — 100% (state senate)
- [AL House District 16](/us/states/al/districts/house/16.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
