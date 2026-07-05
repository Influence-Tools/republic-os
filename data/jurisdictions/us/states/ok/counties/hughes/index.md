---
type: Jurisdiction
title: "Hughes County, OK"
classification: county
fips: "40063"
state: "OK"
demographics:
  population: 13389
  population_under_18: 2872
  population_18_64: 7983
  population_65_plus: 2534
  median_household_income: 51581
  poverty_rate: 20.21
  homeownership_rate: 74.1
  unemployment_rate: 4.94
  median_home_value: 102000
  gini_index: 0.4265
  vacancy_rate: 30.23
  race_white: 8404
  race_black: 706
  race_asian: 60
  race_native: 2654
  hispanic: 838
  bachelors_plus: 2145
districts:
  - to: "us/states/ok/districts/02"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/ok/districts/senate/13"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ok/districts/house/18"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Hughes County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13389 |
| Under 18 | 2872 |
| 18–64 | 7983 |
| 65+ | 2534 |
| Median household income | 51581 |
| Poverty rate | 20.21 |
| Homeownership rate | 74.1 |
| Unemployment rate | 4.94 |
| Median home value | 102000 |
| Gini index | 0.4265 |
| Vacancy rate | 30.23 |
| White | 8404 |
| Black | 706 |
| Asian | 60 |
| Native | 2654 |
| Hispanic/Latino | 838 |
| Bachelor's or higher | 2145 |

## Districts

- [OK-02](/us/states/ok/districts/02.md) — 100% (congressional)
- [OK Senate District 13](/us/states/ok/districts/senate/13.md) — 100% (state senate)
- [OK House District 18](/us/states/ok/districts/house/18.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
