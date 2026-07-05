---
type: Jurisdiction
title: "Caswell County, NC"
classification: county
fips: "37033"
state: "NC"
demographics:
  population: 22404
  population_under_18: 4110
  population_18_64: 13126
  population_65_plus: 5168
  median_household_income: 59755
  poverty_rate: 18.62
  homeownership_rate: 75.16
  unemployment_rate: 5.16
  median_home_value: 164500
  gini_index: 0.4437
  vacancy_rate: 16.07
  race_white: 13503
  race_black: 6874
  race_asian: 93
  race_native: 9
  hispanic: 1141
  bachelors_plus: 3915
districts:
  - to: "us/states/nc/districts/13"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/nc/districts/senate/23"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/nc/districts/house/50"
    rel: in-district
    area_weight: 0.9993
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Caswell County, NC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 22404 |
| Under 18 | 4110 |
| 18–64 | 13126 |
| 65+ | 5168 |
| Median household income | 59755 |
| Poverty rate | 18.62 |
| Homeownership rate | 75.16 |
| Unemployment rate | 5.16 |
| Median home value | 164500 |
| Gini index | 0.4437 |
| Vacancy rate | 16.07 |
| White | 13503 |
| Black | 6874 |
| Asian | 93 |
| Native | 9 |
| Hispanic/Latino | 1141 |
| Bachelor's or higher | 3915 |

## Districts

- [NC-13](/us/states/nc/districts/13.md) — 100% (congressional)
- [NC Senate District 23](/us/states/nc/districts/senate/23.md) — 100% (state senate)
- [NC House District 50](/us/states/nc/districts/house/50.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
