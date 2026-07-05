---
type: Jurisdiction
title: "Sequoyah County, OK"
classification: county
fips: "40135"
state: "OK"
demographics:
  population: 39860
  population_under_18: 9536
  population_18_64: 22895
  population_65_plus: 7429
  median_household_income: 51093
  poverty_rate: 20.19
  homeownership_rate: 70.82
  unemployment_rate: 4.71
  median_home_value: 139400
  gini_index: 0.4515
  vacancy_rate: 15.86
  race_white: 24654
  race_black: 799
  race_asian: 272
  race_native: 7468
  hispanic: 2022
  bachelors_plus: 5303
districts:
  - to: "us/states/ok/districts/02"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ok/districts/senate/4"
    rel: in-district
    area_weight: 0.7465
  - to: "us/states/ok/districts/senate/7"
    rel: in-district
    area_weight: 0.2533
  - to: "us/states/ok/districts/house/2"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Sequoyah County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 39860 |
| Under 18 | 9536 |
| 18–64 | 22895 |
| 65+ | 7429 |
| Median household income | 51093 |
| Poverty rate | 20.19 |
| Homeownership rate | 70.82 |
| Unemployment rate | 4.71 |
| Median home value | 139400 |
| Gini index | 0.4515 |
| Vacancy rate | 15.86 |
| White | 24654 |
| Black | 799 |
| Asian | 272 |
| Native | 7468 |
| Hispanic/Latino | 2022 |
| Bachelor's or higher | 5303 |

## Districts

- [OK-02](/us/states/ok/districts/02.md) — 100% (congressional)
- [OK Senate District 4](/us/states/ok/districts/senate/4.md) — 75% (state senate)
- [OK Senate District 7](/us/states/ok/districts/senate/7.md) — 25% (state senate)
- [OK House District 2](/us/states/ok/districts/house/2.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
