---
type: Jurisdiction
title: "Hertford County, NC"
classification: county
fips: "37091"
state: "NC"
demographics:
  population: 19908
  population_under_18: 3837
  population_18_64: 11538
  population_65_plus: 4533
  median_household_income: 45537
  poverty_rate: 22.93
  homeownership_rate: 67.36
  unemployment_rate: 5.97
  median_home_value: 119200
  gini_index: 0.4954
  vacancy_rate: 15.6
  race_white: 6773
  race_black: 11117
  race_asian: 215
  race_native: 342
  hispanic: 1274
  bachelors_plus: 3189
districts:
  - to: "us/states/nc/districts/01"
    rel: in-district
    area_weight: 0.996
  - to: "us/states/nc/districts/senate/1"
    rel: in-district
    area_weight: 0.9953
  - to: "us/states/nc/districts/house/5"
    rel: in-district
    area_weight: 0.9951
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Hertford County, NC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 19908 |
| Under 18 | 3837 |
| 18–64 | 11538 |
| 65+ | 4533 |
| Median household income | 45537 |
| Poverty rate | 22.93 |
| Homeownership rate | 67.36 |
| Unemployment rate | 5.97 |
| Median home value | 119200 |
| Gini index | 0.4954 |
| Vacancy rate | 15.6 |
| White | 6773 |
| Black | 11117 |
| Asian | 215 |
| Native | 342 |
| Hispanic/Latino | 1274 |
| Bachelor's or higher | 3189 |

## Districts

- [NC-01](/us/states/nc/districts/01.md) — 100% (congressional)
- [NC Senate District 1](/us/states/nc/districts/senate/1.md) — 100% (state senate)
- [NC House District 5](/us/states/nc/districts/house/5.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
