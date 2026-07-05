---
type: Jurisdiction
title: "Transylvania County, NC"
classification: county
fips: "37175"
state: "NC"
demographics:
  population: 33691
  population_under_18: 5273
  population_18_64: 17992
  population_65_plus: 10426
  median_household_income: 66184
  poverty_rate: 13.21
  homeownership_rate: 74.66
  unemployment_rate: 2.78
  median_home_value: 373600
  gini_index: 0.4621
  vacancy_rate: 24.3
  race_white: 29769
  race_black: 1207
  race_asian: 229
  race_native: 60
  hispanic: 1753
  bachelors_plus: 14380
districts:
  - to: "us/states/nc/districts/11"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/nc/districts/senate/50"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/nc/districts/house/119"
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

# Transylvania County, NC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 33691 |
| Under 18 | 5273 |
| 18–64 | 17992 |
| 65+ | 10426 |
| Median household income | 66184 |
| Poverty rate | 13.21 |
| Homeownership rate | 74.66 |
| Unemployment rate | 2.78 |
| Median home value | 373600 |
| Gini index | 0.4621 |
| Vacancy rate | 24.3 |
| White | 29769 |
| Black | 1207 |
| Asian | 229 |
| Native | 60 |
| Hispanic/Latino | 1753 |
| Bachelor's or higher | 14380 |

## Districts

- [NC-11](/us/states/nc/districts/11.md) — 100% (congressional)
- [NC Senate District 50](/us/states/nc/districts/senate/50.md) — 100% (state senate)
- [NC House District 119](/us/states/nc/districts/house/119.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
