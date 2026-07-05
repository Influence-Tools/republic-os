---
type: Jurisdiction
title: "Washington County, OK"
classification: county
fips: "40147"
state: "OK"
demographics:
  population: 53326
  population_under_18: 12820
  population_18_64: 29703
  population_65_plus: 10803
  median_household_income: 60162
  poverty_rate: 16.06
  homeownership_rate: 71.87
  unemployment_rate: 4.36
  median_home_value: 173200
  gini_index: 0.4825
  vacancy_rate: 11.73
  race_white: 38484
  race_black: 1289
  race_asian: 1078
  race_native: 4548
  hispanic: 3694
  bachelors_plus: 14234
districts:
  - to: "us/states/ok/districts/02"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ok/districts/senate/29"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ok/districts/house/10"
    rel: in-district
    area_weight: 0.653
  - to: "us/states/ok/districts/house/11"
    rel: in-district
    area_weight: 0.347
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Washington County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 53326 |
| Under 18 | 12820 |
| 18–64 | 29703 |
| 65+ | 10803 |
| Median household income | 60162 |
| Poverty rate | 16.06 |
| Homeownership rate | 71.87 |
| Unemployment rate | 4.36 |
| Median home value | 173200 |
| Gini index | 0.4825 |
| Vacancy rate | 11.73 |
| White | 38484 |
| Black | 1289 |
| Asian | 1078 |
| Native | 4548 |
| Hispanic/Latino | 3694 |
| Bachelor's or higher | 14234 |

## Districts

- [OK-02](/us/states/ok/districts/02.md) — 100% (congressional)
- [OK Senate District 29](/us/states/ok/districts/senate/29.md) — 100% (state senate)
- [OK House District 10](/us/states/ok/districts/house/10.md) — 65% (state house)
- [OK House District 11](/us/states/ok/districts/house/11.md) — 35% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
