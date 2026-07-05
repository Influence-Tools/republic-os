---
type: Jurisdiction
title: "Atoka County, OK"
classification: county
fips: "40005"
state: "OK"
demographics:
  population: 14379
  population_under_18: 3061
  population_18_64: 8604
  population_65_plus: 2714
  median_household_income: 54785
  poverty_rate: 17.3
  homeownership_rate: 74.37
  unemployment_rate: 4.59
  median_home_value: 157600
  gini_index: 0.4511
  vacancy_rate: 17.14
  race_white: 9759
  race_black: 591
  race_asian: 17
  race_native: 1350
  hispanic: 636
  bachelors_plus: 2311
districts:
  - to: "us/states/ok/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ok/districts/senate/6"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ok/districts/house/22"
    rel: in-district
    area_weight: 0.8103
  - to: "us/states/ok/districts/house/19"
    rel: in-district
    area_weight: 0.1897
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Atoka County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14379 |
| Under 18 | 3061 |
| 18–64 | 8604 |
| 65+ | 2714 |
| Median household income | 54785 |
| Poverty rate | 17.3 |
| Homeownership rate | 74.37 |
| Unemployment rate | 4.59 |
| Median home value | 157600 |
| Gini index | 0.4511 |
| Vacancy rate | 17.14 |
| White | 9759 |
| Black | 591 |
| Asian | 17 |
| Native | 1350 |
| Hispanic/Latino | 636 |
| Bachelor's or higher | 2311 |

## Districts

- [OK-02](/us/states/ok/districts/02.md) — 100% (congressional)
- [OK Senate District 6](/us/states/ok/districts/senate/6.md) — 100% (state senate)
- [OK House District 22](/us/states/ok/districts/house/22.md) — 81% (state house)
- [OK House District 19](/us/states/ok/districts/house/19.md) — 19% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
