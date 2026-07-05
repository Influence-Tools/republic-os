---
type: Jurisdiction
title: "Lincoln County, NC"
classification: county
fips: "37109"
state: "NC"
demographics:
  population: 92716
  population_under_18: 19131
  population_18_64: 55523
  population_65_plus: 18062
  median_household_income: 80016
  poverty_rate: 11.25
  homeownership_rate: 78.92
  unemployment_rate: 3.34
  median_home_value: 321000
  gini_index: 0.4729
  vacancy_rate: 6.82
  race_white: 77009
  race_black: 5472
  race_asian: 733
  race_native: 300
  hispanic: 7542
  bachelors_plus: 24776
districts:
  - to: "us/states/nc/districts/10"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/nc/districts/senate/44"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/nc/districts/house/97"
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

# Lincoln County, NC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 92716 |
| Under 18 | 19131 |
| 18–64 | 55523 |
| 65+ | 18062 |
| Median household income | 80016 |
| Poverty rate | 11.25 |
| Homeownership rate | 78.92 |
| Unemployment rate | 3.34 |
| Median home value | 321000 |
| Gini index | 0.4729 |
| Vacancy rate | 6.82 |
| White | 77009 |
| Black | 5472 |
| Asian | 733 |
| Native | 300 |
| Hispanic/Latino | 7542 |
| Bachelor's or higher | 24776 |

## Districts

- [NC-10](/us/states/nc/districts/10.md) — 100% (congressional)
- [NC Senate District 44](/us/states/nc/districts/senate/44.md) — 100% (state senate)
- [NC House District 97](/us/states/nc/districts/house/97.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
