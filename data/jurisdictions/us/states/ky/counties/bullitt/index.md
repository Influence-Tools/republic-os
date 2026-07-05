---
type: Jurisdiction
title: "Bullitt County, KY"
classification: county
fips: "21029"
state: "KY"
demographics:
  population: 84027
  population_under_18: 17795
  population_18_64: 51647
  population_65_plus: 14585
  median_household_income: 80558
  poverty_rate: 9.69
  homeownership_rate: 84.93
  unemployment_rate: 4.26
  median_home_value: 247200
  gini_index: 0.4031
  vacancy_rate: 5.54
  race_white: 76760
  race_black: 1092
  race_asian: 604
  race_native: 17
  hispanic: 2769
  bachelors_plus: 15991
districts:
  - to: "us/states/ky/districts/02"
    rel: in-district
    area_weight: 0.9978
  - to: "us/states/ky/districts/senate/38"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/ky/districts/house/49"
    rel: in-district
    area_weight: 0.545
  - to: "us/states/ky/districts/house/26"
    rel: in-district
    area_weight: 0.4518
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Bullitt County, KY

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 84027 |
| Under 18 | 17795 |
| 18–64 | 51647 |
| 65+ | 14585 |
| Median household income | 80558 |
| Poverty rate | 9.69 |
| Homeownership rate | 84.93 |
| Unemployment rate | 4.26 |
| Median home value | 247200 |
| Gini index | 0.4031 |
| Vacancy rate | 5.54 |
| White | 76760 |
| Black | 1092 |
| Asian | 604 |
| Native | 17 |
| Hispanic/Latino | 2769 |
| Bachelor's or higher | 15991 |

## Districts

- [KY-02](/us/states/ky/districts/02.md) — 100% (congressional)
- [KY Senate District 38](/us/states/ky/districts/senate/38.md) — 100% (state senate)
- [KY House District 49](/us/states/ky/districts/house/49.md) — 55% (state house)
- [KY House District 26](/us/states/ky/districts/house/26.md) — 45% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
