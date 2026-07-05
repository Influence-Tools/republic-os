---
type: Jurisdiction
title: "Georgetown County, SC"
classification: county
fips: "45043"
state: "SC"
demographics:
  population: 64811
  population_under_18: 10994
  population_18_64: 33914
  population_65_plus: 19903
  median_household_income: 68713
  poverty_rate: 14.97
  homeownership_rate: 83.95
  unemployment_rate: 4.38
  median_home_value: 289500
  gini_index: 0.4941
  vacancy_rate: 27.02
  race_white: 43061
  race_black: 18109
  race_asian: 184
  race_native: 90
  hispanic: 2353
  bachelors_plus: 21784
districts:
  - to: "us/states/sc/districts/07"
    rel: in-district
    area_weight: 0.847
  - to: "us/states/sc/districts/senate/32"
    rel: in-district
    area_weight: 0.7113
  - to: "us/states/sc/districts/senate/34"
    rel: in-district
    area_weight: 0.137
  - to: "us/states/sc/districts/house/103"
    rel: in-district
    area_weight: 0.5735
  - to: "us/states/sc/districts/house/108"
    rel: in-district
    area_weight: 0.2749
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sc]
timestamp: "2026-07-03"
---

# Georgetown County, SC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 64811 |
| Under 18 | 10994 |
| 18–64 | 33914 |
| 65+ | 19903 |
| Median household income | 68713 |
| Poverty rate | 14.97 |
| Homeownership rate | 83.95 |
| Unemployment rate | 4.38 |
| Median home value | 289500 |
| Gini index | 0.4941 |
| Vacancy rate | 27.02 |
| White | 43061 |
| Black | 18109 |
| Asian | 184 |
| Native | 90 |
| Hispanic/Latino | 2353 |
| Bachelor's or higher | 21784 |

## Districts

- [SC-07](/us/states/sc/districts/07.md) — 85% (congressional)
- [SC Senate District 32](/us/states/sc/districts/senate/32.md) — 71% (state senate)
- [SC Senate District 34](/us/states/sc/districts/senate/34.md) — 14% (state senate)
- [SC House District 103](/us/states/sc/districts/house/103.md) — 57% (state house)
- [SC House District 108](/us/states/sc/districts/house/108.md) — 27% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
