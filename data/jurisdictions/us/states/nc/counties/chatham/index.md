---
type: Jurisdiction
title: "Chatham County, NC"
classification: county
fips: "37037"
state: "NC"
demographics:
  population: 80151
  population_under_18: 15516
  population_18_64: 44444
  population_65_plus: 20191
  median_household_income: 94317
  poverty_rate: 11.05
  homeownership_rate: 80.57
  unemployment_rate: 2.93
  median_home_value: 446200
  gini_index: 0.4934
  vacancy_rate: 8.1
  race_white: 56974
  race_black: 8152
  race_asian: 1791
  race_native: 388
  hispanic: 10930
  bachelors_plus: 42787
districts:
  - to: "us/states/nc/districts/09"
    rel: in-district
    area_weight: 0.6929
  - to: "us/states/nc/districts/04"
    rel: in-district
    area_weight: 0.3056
  - to: "us/states/nc/districts/senate/20"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/nc/districts/house/54"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Chatham County, NC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 80151 |
| Under 18 | 15516 |
| 18–64 | 44444 |
| 65+ | 20191 |
| Median household income | 94317 |
| Poverty rate | 11.05 |
| Homeownership rate | 80.57 |
| Unemployment rate | 2.93 |
| Median home value | 446200 |
| Gini index | 0.4934 |
| Vacancy rate | 8.1 |
| White | 56974 |
| Black | 8152 |
| Asian | 1791 |
| Native | 388 |
| Hispanic/Latino | 10930 |
| Bachelor's or higher | 42787 |

## Districts

- [NC-09](/us/states/nc/districts/09.md) — 69% (congressional)
- [NC-04](/us/states/nc/districts/04.md) — 31% (congressional)
- [NC Senate District 20](/us/states/nc/districts/senate/20.md) — 100% (state senate)
- [NC House District 54](/us/states/nc/districts/house/54.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
