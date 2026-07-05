---
type: Jurisdiction
title: "Delaware County, OK"
classification: county
fips: "40041"
state: "OK"
demographics:
  population: 41279
  population_under_18: 8170
  population_18_64: 22508
  population_65_plus: 10601
  median_household_income: 56676
  poverty_rate: 18.96
  homeownership_rate: 77.06
  unemployment_rate: 5.16
  median_home_value: 175300
  gini_index: 0.475
  vacancy_rate: 29.66
  race_white: 26130
  race_black: 153
  race_asian: 635
  race_native: 8397
  hispanic: 1862
  bachelors_plus: 8038
districts:
  - to: "us/states/ok/districts/02"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ok/districts/senate/4"
    rel: in-district
    area_weight: 0.8859
  - to: "us/states/ok/districts/senate/1"
    rel: in-district
    area_weight: 0.114
  - to: "us/states/ok/districts/house/5"
    rel: in-district
    area_weight: 0.6222
  - to: "us/states/ok/districts/house/86"
    rel: in-district
    area_weight: 0.3207
  - to: "us/states/ok/districts/house/7"
    rel: in-district
    area_weight: 0.0571
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Delaware County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 41279 |
| Under 18 | 8170 |
| 18–64 | 22508 |
| 65+ | 10601 |
| Median household income | 56676 |
| Poverty rate | 18.96 |
| Homeownership rate | 77.06 |
| Unemployment rate | 5.16 |
| Median home value | 175300 |
| Gini index | 0.475 |
| Vacancy rate | 29.66 |
| White | 26130 |
| Black | 153 |
| Asian | 635 |
| Native | 8397 |
| Hispanic/Latino | 1862 |
| Bachelor's or higher | 8038 |

## Districts

- [OK-02](/us/states/ok/districts/02.md) — 100% (congressional)
- [OK Senate District 4](/us/states/ok/districts/senate/4.md) — 89% (state senate)
- [OK Senate District 1](/us/states/ok/districts/senate/1.md) — 11% (state senate)
- [OK House District 5](/us/states/ok/districts/house/5.md) — 62% (state house)
- [OK House District 86](/us/states/ok/districts/house/86.md) — 32% (state house)
- [OK House District 7](/us/states/ok/districts/house/7.md) — 6% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
