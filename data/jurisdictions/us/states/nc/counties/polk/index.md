---
type: Jurisdiction
title: "Polk County, NC"
classification: county
fips: "37149"
state: "NC"
demographics:
  population: 19891
  population_under_18: 3047
  population_18_64: 10357
  population_65_plus: 6487
  median_household_income: 67758
  poverty_rate: 14.01
  homeownership_rate: 76.89
  unemployment_rate: 5.07
  median_home_value: 315000
  gini_index: 0.4985
  vacancy_rate: 18.71
  race_white: 17300
  race_black: 876
  race_asian: 154
  race_native: 42
  hispanic: 1118
  bachelors_plus: 7924
districts:
  - to: "us/states/nc/districts/14"
    rel: in-district
    area_weight: 0.5198
  - to: "us/states/nc/districts/11"
    rel: in-district
    area_weight: 0.4796
  - to: "us/states/nc/districts/senate/48"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/nc/districts/house/113"
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

# Polk County, NC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 19891 |
| Under 18 | 3047 |
| 18–64 | 10357 |
| 65+ | 6487 |
| Median household income | 67758 |
| Poverty rate | 14.01 |
| Homeownership rate | 76.89 |
| Unemployment rate | 5.07 |
| Median home value | 315000 |
| Gini index | 0.4985 |
| Vacancy rate | 18.71 |
| White | 17300 |
| Black | 876 |
| Asian | 154 |
| Native | 42 |
| Hispanic/Latino | 1118 |
| Bachelor's or higher | 7924 |

## Districts

- [NC-14](/us/states/nc/districts/14.md) — 52% (congressional)
- [NC-11](/us/states/nc/districts/11.md) — 48% (congressional)
- [NC Senate District 48](/us/states/nc/districts/senate/48.md) — 100% (state senate)
- [NC House District 113](/us/states/nc/districts/house/113.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
