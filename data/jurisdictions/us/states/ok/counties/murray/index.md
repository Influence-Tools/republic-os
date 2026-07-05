---
type: Jurisdiction
title: "Murray County, OK"
classification: county
fips: "40099"
state: "OK"
demographics:
  population: 13753
  population_under_18: 3123
  population_18_64: 7790
  population_65_plus: 2840
  median_household_income: 66322
  poverty_rate: 12.65
  homeownership_rate: 72.09
  unemployment_rate: 2.48
  median_home_value: 159800
  gini_index: 0.4878
  vacancy_rate: 24.39
  race_white: 9682
  race_black: 152
  race_asian: 0
  race_native: 1906
  hispanic: 994
  bachelors_plus: 2394
districts:
  - to: "us/states/ok/districts/04"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ok/districts/senate/14"
    rel: in-district
    area_weight: 0.6093
  - to: "us/states/ok/districts/senate/13"
    rel: in-district
    area_weight: 0.3907
  - to: "us/states/ok/districts/house/22"
    rel: in-district
    area_weight: 0.7501
  - to: "us/states/ok/districts/house/48"
    rel: in-district
    area_weight: 0.2498
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Murray County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13753 |
| Under 18 | 3123 |
| 18–64 | 7790 |
| 65+ | 2840 |
| Median household income | 66322 |
| Poverty rate | 12.65 |
| Homeownership rate | 72.09 |
| Unemployment rate | 2.48 |
| Median home value | 159800 |
| Gini index | 0.4878 |
| Vacancy rate | 24.39 |
| White | 9682 |
| Black | 152 |
| Asian | 0 |
| Native | 1906 |
| Hispanic/Latino | 994 |
| Bachelor's or higher | 2394 |

## Districts

- [OK-04](/us/states/ok/districts/04.md) — 100% (congressional)
- [OK Senate District 14](/us/states/ok/districts/senate/14.md) — 61% (state senate)
- [OK Senate District 13](/us/states/ok/districts/senate/13.md) — 39% (state senate)
- [OK House District 22](/us/states/ok/districts/house/22.md) — 75% (state house)
- [OK House District 48](/us/states/ok/districts/house/48.md) — 25% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
