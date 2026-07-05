---
type: Jurisdiction
title: "Cherokee County, NC"
classification: county
fips: "37039"
state: "NC"
demographics:
  population: 29562
  population_under_18: 4716
  population_18_64: 15543
  population_65_plus: 9303
  median_household_income: 53628
  poverty_rate: 12.36
  homeownership_rate: 83.7
  unemployment_rate: 4.07
  median_home_value: 232300
  gini_index: 0.4195
  vacancy_rate: 28.05
  race_white: 26739
  race_black: 527
  race_asian: 156
  race_native: 347
  hispanic: 1088
  bachelors_plus: 7570
districts:
  - to: "us/states/nc/districts/11"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/nc/districts/senate/50"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/nc/districts/house/120"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Cherokee County, NC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 29562 |
| Under 18 | 4716 |
| 18–64 | 15543 |
| 65+ | 9303 |
| Median household income | 53628 |
| Poverty rate | 12.36 |
| Homeownership rate | 83.7 |
| Unemployment rate | 4.07 |
| Median home value | 232300 |
| Gini index | 0.4195 |
| Vacancy rate | 28.05 |
| White | 26739 |
| Black | 527 |
| Asian | 156 |
| Native | 347 |
| Hispanic/Latino | 1088 |
| Bachelor's or higher | 7570 |

## Districts

- [NC-11](/us/states/nc/districts/11.md) — 100% (congressional)
- [NC Senate District 50](/us/states/nc/districts/senate/50.md) — 100% (state senate)
- [NC House District 120](/us/states/nc/districts/house/120.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
