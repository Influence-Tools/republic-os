---
type: Jurisdiction
title: "Edgecombe County, NC"
classification: county
fips: "37065"
state: "NC"
demographics:
  population: 48736
  population_under_18: 11152
  population_18_64: 27393
  population_65_plus: 10191
  median_household_income: 51265
  poverty_rate: 21.73
  homeownership_rate: 60.81
  unemployment_rate: 8.74
  median_home_value: 125100
  gini_index: 0.4567
  vacancy_rate: 15.59
  race_white: 18160
  race_black: 27114
  race_asian: 128
  race_native: 188
  hispanic: 3005
  bachelors_plus: 7812
districts:
  - to: "us/states/nc/districts/01"
    rel: in-district
    area_weight: 0.9985
  - to: "us/states/nc/districts/senate/5"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/nc/districts/house/23"
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

# Edgecombe County, NC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 48736 |
| Under 18 | 11152 |
| 18–64 | 27393 |
| 65+ | 10191 |
| Median household income | 51265 |
| Poverty rate | 21.73 |
| Homeownership rate | 60.81 |
| Unemployment rate | 8.74 |
| Median home value | 125100 |
| Gini index | 0.4567 |
| Vacancy rate | 15.59 |
| White | 18160 |
| Black | 27114 |
| Asian | 128 |
| Native | 188 |
| Hispanic/Latino | 3005 |
| Bachelor's or higher | 7812 |

## Districts

- [NC-01](/us/states/nc/districts/01.md) — 100% (congressional)
- [NC Senate District 5](/us/states/nc/districts/senate/5.md) — 100% (state senate)
- [NC House District 23](/us/states/nc/districts/house/23.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
