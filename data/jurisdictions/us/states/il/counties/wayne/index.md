---
type: Jurisdiction
title: "Wayne County, IL"
classification: county
fips: "17191"
state: "IL"
demographics:
  population: 15973
  population_under_18: 3592
  population_18_64: 8871
  population_65_plus: 3510
  median_household_income: 55521
  poverty_rate: 16.12
  homeownership_rate: 78.39
  unemployment_rate: 3.42
  median_home_value: 110700
  gini_index: 0.4615
  vacancy_rate: 10.6
  race_white: 15199
  race_black: 64
  race_asian: 97
  race_native: 44
  hispanic: 330
  bachelors_plus: 2400
districts:
  - to: "us/states/il/districts/12"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/il/districts/senate/58"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/il/districts/house/116"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Wayne County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 15973 |
| Under 18 | 3592 |
| 18–64 | 8871 |
| 65+ | 3510 |
| Median household income | 55521 |
| Poverty rate | 16.12 |
| Homeownership rate | 78.39 |
| Unemployment rate | 3.42 |
| Median home value | 110700 |
| Gini index | 0.4615 |
| Vacancy rate | 10.6 |
| White | 15199 |
| Black | 64 |
| Asian | 97 |
| Native | 44 |
| Hispanic/Latino | 330 |
| Bachelor's or higher | 2400 |

## Districts

- [IL-12](/us/states/il/districts/12.md) — 100% (congressional)
- [IL Senate District 58](/us/states/il/districts/senate/58.md) — 100% (state senate)
- [IL House District 116](/us/states/il/districts/house/116.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
