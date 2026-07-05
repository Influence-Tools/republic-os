---
type: Jurisdiction
title: "Columbus County, NC"
classification: county
fips: "37047"
state: "NC"
demographics:
  population: 50140
  population_under_18: 10334
  population_18_64: 29430
  population_65_plus: 10376
  median_household_income: 49442
  poverty_rate: 18.18
  homeownership_rate: 71.09
  unemployment_rate: 4.39
  median_home_value: 146000
  gini_index: 0.4727
  vacancy_rate: 14.92
  race_white: 29839
  race_black: 14082
  race_asian: 249
  race_native: 2036
  hispanic: 2831
  bachelors_plus: 6912
districts:
  - to: "us/states/nc/districts/07"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/nc/districts/senate/8"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/nc/districts/house/46"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Columbus County, NC

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 50140 |
| Under 18 | 10334 |
| 18–64 | 29430 |
| 65+ | 10376 |
| Median household income | 49442 |
| Poverty rate | 18.18 |
| Homeownership rate | 71.09 |
| Unemployment rate | 4.39 |
| Median home value | 146000 |
| Gini index | 0.4727 |
| Vacancy rate | 14.92 |
| White | 29839 |
| Black | 14082 |
| Asian | 249 |
| Native | 2036 |
| Hispanic/Latino | 2831 |
| Bachelor's or higher | 6912 |

## Districts

- [NC-07](/us/states/nc/districts/07.md) — 100% (congressional)
- [NC Senate District 8](/us/states/nc/districts/senate/8.md) — 100% (state senate)
- [NC House District 46](/us/states/nc/districts/house/46.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
