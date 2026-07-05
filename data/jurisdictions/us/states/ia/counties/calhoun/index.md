---
type: Jurisdiction
title: "Calhoun County, IA"
classification: county
fips: "19025"
state: "IA"
demographics:
  population: 9803
  population_under_18: 2130
  population_18_64: 5353
  population_65_plus: 2320
  median_household_income: 64964
  poverty_rate: 9.26
  homeownership_rate: 80.52
  unemployment_rate: 2.57
  median_home_value: 118800
  gini_index: 0.4521
  vacancy_rate: 16.78
  race_white: 9026
  race_black: 158
  race_asian: 22
  race_native: 17
  hispanic: 266
  bachelors_plus: 1981
districts:
  - to: "us/states/ia/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ia/districts/senate/4"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ia/districts/house/7"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Calhoun County, IA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9803 |
| Under 18 | 2130 |
| 18–64 | 5353 |
| 65+ | 2320 |
| Median household income | 64964 |
| Poverty rate | 9.26 |
| Homeownership rate | 80.52 |
| Unemployment rate | 2.57 |
| Median home value | 118800 |
| Gini index | 0.4521 |
| Vacancy rate | 16.78 |
| White | 9026 |
| Black | 158 |
| Asian | 22 |
| Native | 17 |
| Hispanic/Latino | 266 |
| Bachelor's or higher | 1981 |

## Districts

- [IA-04](/us/states/ia/districts/04.md) — 100% (congressional)
- [IA Senate District 4](/us/states/ia/districts/senate/4.md) — 100% (state senate)
- [IA House District 7](/us/states/ia/districts/house/7.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
