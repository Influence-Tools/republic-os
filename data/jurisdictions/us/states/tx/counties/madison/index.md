---
type: Jurisdiction
title: "Madison County, TX"
classification: county
fips: "48313"
state: "TX"
demographics:
  population: 13648
  population_under_18: 3037
  population_18_64: 8502
  population_65_plus: 2109
  median_household_income: 74596
  poverty_rate: 10.89
  homeownership_rate: 75.29
  unemployment_rate: 7.14
  median_home_value: 176200
  gini_index: 0.3952
  vacancy_rate: 17.27
  race_white: 8080
  race_black: 2111
  race_asian: 155
  race_native: 36
  hispanic: 3573
  bachelors_plus: 2050
districts:
  - to: "us/states/tx/districts/10"
    rel: in-district
    area_weight: 0.9973
  - to: "us/states/tx/districts/senate/5"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/house/12"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Madison County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13648 |
| Under 18 | 3037 |
| 18–64 | 8502 |
| 65+ | 2109 |
| Median household income | 74596 |
| Poverty rate | 10.89 |
| Homeownership rate | 75.29 |
| Unemployment rate | 7.14 |
| Median home value | 176200 |
| Gini index | 0.3952 |
| Vacancy rate | 17.27 |
| White | 8080 |
| Black | 2111 |
| Asian | 155 |
| Native | 36 |
| Hispanic/Latino | 3573 |
| Bachelor's or higher | 2050 |

## Districts

- [TX-10](/us/states/tx/districts/10.md) — 100% (congressional)
- [TX Senate District 5](/us/states/tx/districts/senate/5.md) — 100% (state senate)
- [TX House District 12](/us/states/tx/districts/house/12.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
