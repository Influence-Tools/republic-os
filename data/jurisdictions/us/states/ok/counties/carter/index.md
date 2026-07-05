---
type: Jurisdiction
title: "Carter County, OK"
classification: county
fips: "40019"
state: "OK"
demographics:
  population: 48555
  population_under_18: 12121
  population_18_64: 28134
  population_65_plus: 8300
  median_household_income: 60723
  poverty_rate: 16.24
  homeownership_rate: 66.84
  unemployment_rate: 3.82
  median_home_value: 168500
  gini_index: 0.4727
  vacancy_rate: 11.92
  race_white: 32987
  race_black: 3007
  race_asian: 608
  race_native: 3544
  hispanic: 4166
  bachelors_plus: 8639
districts:
  - to: "us/states/ok/districts/04"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ok/districts/senate/14"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ok/districts/house/48"
    rel: in-district
    area_weight: 0.5574
  - to: "us/states/ok/districts/house/49"
    rel: in-district
    area_weight: 0.4426
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Carter County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 48555 |
| Under 18 | 12121 |
| 18–64 | 28134 |
| 65+ | 8300 |
| Median household income | 60723 |
| Poverty rate | 16.24 |
| Homeownership rate | 66.84 |
| Unemployment rate | 3.82 |
| Median home value | 168500 |
| Gini index | 0.4727 |
| Vacancy rate | 11.92 |
| White | 32987 |
| Black | 3007 |
| Asian | 608 |
| Native | 3544 |
| Hispanic/Latino | 4166 |
| Bachelor's or higher | 8639 |

## Districts

- [OK-04](/us/states/ok/districts/04.md) — 100% (congressional)
- [OK Senate District 14](/us/states/ok/districts/senate/14.md) — 100% (state senate)
- [OK House District 48](/us/states/ok/districts/house/48.md) — 56% (state house)
- [OK House District 49](/us/states/ok/districts/house/49.md) — 44% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
