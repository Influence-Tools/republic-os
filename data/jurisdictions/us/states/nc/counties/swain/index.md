---
type: Jurisdiction
title: "Swain County, NC"
classification: county
fips: "37173"
state: "NC"
demographics:
  population: 14013
  population_under_18: 2916
  population_18_64: 8308
  population_65_plus: 2789
  median_household_income: 52349
  poverty_rate: 19.11
  homeownership_rate: 72.66
  unemployment_rate: 7.61
  median_home_value: 207000
  gini_index: 0.4623
  vacancy_rate: 30.32
  race_white: 8333
  race_black: 363
  race_asian: 69
  race_native: 3855
  hispanic: 767
  bachelors_plus: 3114
districts:
  - to: "us/states/nc/districts/11"
    rel: in-district
    area_weight: 0.9987
  - to: "us/states/nc/districts/senate/50"
    rel: in-district
    area_weight: 0.9987
  - to: "us/states/nc/districts/house/119"
    rel: in-district
    area_weight: 0.9984
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Swain County, NC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14013 |
| Under 18 | 2916 |
| 18–64 | 8308 |
| 65+ | 2789 |
| Median household income | 52349 |
| Poverty rate | 19.11 |
| Homeownership rate | 72.66 |
| Unemployment rate | 7.61 |
| Median home value | 207000 |
| Gini index | 0.4623 |
| Vacancy rate | 30.32 |
| White | 8333 |
| Black | 363 |
| Asian | 69 |
| Native | 3855 |
| Hispanic/Latino | 767 |
| Bachelor's or higher | 3114 |

## Districts

- [NC-11](/us/states/nc/districts/11.md) — 100% (congressional)
- [NC Senate District 50](/us/states/nc/districts/senate/50.md) — 100% (state senate)
- [NC House District 119](/us/states/nc/districts/house/119.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
