---
type: Jurisdiction
title: "Clay County, NC"
classification: county
fips: "37043"
state: "NC"
demographics:
  population: 11610
  population_under_18: 1865
  population_18_64: 5939
  population_65_plus: 3806
  median_household_income: 56971
  poverty_rate: 12.88
  homeownership_rate: 81.18
  unemployment_rate: 2.65
  median_home_value: 278400
  gini_index: 0.4766
  vacancy_rate: 32.23
  race_white: 10768
  race_black: 256
  race_asian: 66
  race_native: 43
  hispanic: 481
  bachelors_plus: 3757
districts:
  - to: "us/states/nc/districts/11"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/nc/districts/senate/50"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/nc/districts/house/120"
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

# Clay County, NC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11610 |
| Under 18 | 1865 |
| 18–64 | 5939 |
| 65+ | 3806 |
| Median household income | 56971 |
| Poverty rate | 12.88 |
| Homeownership rate | 81.18 |
| Unemployment rate | 2.65 |
| Median home value | 278400 |
| Gini index | 0.4766 |
| Vacancy rate | 32.23 |
| White | 10768 |
| Black | 256 |
| Asian | 66 |
| Native | 43 |
| Hispanic/Latino | 481 |
| Bachelor's or higher | 3757 |

## Districts

- [NC-11](/us/states/nc/districts/11.md) — 100% (congressional)
- [NC Senate District 50](/us/states/nc/districts/senate/50.md) — 100% (state senate)
- [NC House District 120](/us/states/nc/districts/house/120.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
