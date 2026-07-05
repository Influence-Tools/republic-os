---
type: Jurisdiction
title: "Okmulgee County, OK"
classification: county
fips: "40111"
state: "OK"
demographics:
  population: 36899
  population_under_18: 8695
  population_18_64: 21386
  population_65_plus: 6818
  median_household_income: 54029
  poverty_rate: 18.02
  homeownership_rate: 70.1
  unemployment_rate: 7.26
  median_home_value: 121200
  gini_index: 0.4646
  vacancy_rate: 14.89
  race_white: 23071
  race_black: 2584
  race_asian: 170
  race_native: 5592
  hispanic: 1906
  bachelors_plus: 5614
districts:
  - to: "us/states/ok/districts/02"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ok/districts/senate/8"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ok/districts/house/16"
    rel: in-district
    area_weight: 0.832
  - to: "us/states/ok/districts/house/24"
    rel: in-district
    area_weight: 0.1679
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Okmulgee County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 36899 |
| Under 18 | 8695 |
| 18–64 | 21386 |
| 65+ | 6818 |
| Median household income | 54029 |
| Poverty rate | 18.02 |
| Homeownership rate | 70.1 |
| Unemployment rate | 7.26 |
| Median home value | 121200 |
| Gini index | 0.4646 |
| Vacancy rate | 14.89 |
| White | 23071 |
| Black | 2584 |
| Asian | 170 |
| Native | 5592 |
| Hispanic/Latino | 1906 |
| Bachelor's or higher | 5614 |

## Districts

- [OK-02](/us/states/ok/districts/02.md) — 100% (congressional)
- [OK Senate District 8](/us/states/ok/districts/senate/8.md) — 100% (state senate)
- [OK House District 16](/us/states/ok/districts/house/16.md) — 83% (state house)
- [OK House District 24](/us/states/ok/districts/house/24.md) — 17% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
