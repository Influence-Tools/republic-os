---
type: Jurisdiction
title: "Cleveland County, NC"
classification: county
fips: "37045"
state: "NC"
demographics:
  population: 100991
  population_under_18: 22528
  population_18_64: 59467
  population_65_plus: 18996
  median_household_income: 58534
  poverty_rate: 16.6
  homeownership_rate: 70.89
  unemployment_rate: 5.19
  median_home_value: 200000
  gini_index: 0.4432
  vacancy_rate: 12.31
  race_white: 72350
  race_black: 18099
  race_asian: 1098
  race_native: 353
  hispanic: 4792
  bachelors_plus: 20887
districts:
  - to: "us/states/nc/districts/14"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/nc/districts/senate/44"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/nc/districts/house/110"
    rel: in-district
    area_weight: 0.5098
  - to: "us/states/nc/districts/house/111"
    rel: in-district
    area_weight: 0.49
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Cleveland County, NC

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 100991 |
| Under 18 | 22528 |
| 18–64 | 59467 |
| 65+ | 18996 |
| Median household income | 58534 |
| Poverty rate | 16.6 |
| Homeownership rate | 70.89 |
| Unemployment rate | 5.19 |
| Median home value | 200000 |
| Gini index | 0.4432 |
| Vacancy rate | 12.31 |
| White | 72350 |
| Black | 18099 |
| Asian | 1098 |
| Native | 353 |
| Hispanic/Latino | 4792 |
| Bachelor's or higher | 20887 |

## Districts

- [NC-14](/us/states/nc/districts/14.md) — 100% (congressional)
- [NC Senate District 44](/us/states/nc/districts/senate/44.md) — 100% (state senate)
- [NC House District 110](/us/states/nc/districts/house/110.md) — 51% (state house)
- [NC House District 111](/us/states/nc/districts/house/111.md) — 49% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
