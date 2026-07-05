---
type: Jurisdiction
title: "Jefferson County, OK"
classification: county
fips: "40067"
state: "OK"
demographics:
  population: 5380
  population_under_18: 1347
  population_18_64: 2907
  population_65_plus: 1126
  median_household_income: 48668
  poverty_rate: 23.13
  homeownership_rate: 70.87
  unemployment_rate: 5.24
  median_home_value: 82500
  gini_index: 0.459
  vacancy_rate: 20.89
  race_white: 4276
  race_black: 65
  race_asian: 3
  race_native: 219
  hispanic: 589
  bachelors_plus: 703
districts:
  - to: "us/states/ok/districts/04"
    rel: in-district
    area_weight: 0.9984
  - to: "us/states/ok/districts/senate/31"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/ok/districts/house/50"
    rel: in-district
    area_weight: 0.9993
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Jefferson County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5380 |
| Under 18 | 1347 |
| 18–64 | 2907 |
| 65+ | 1126 |
| Median household income | 48668 |
| Poverty rate | 23.13 |
| Homeownership rate | 70.87 |
| Unemployment rate | 5.24 |
| Median home value | 82500 |
| Gini index | 0.459 |
| Vacancy rate | 20.89 |
| White | 4276 |
| Black | 65 |
| Asian | 3 |
| Native | 219 |
| Hispanic/Latino | 589 |
| Bachelor's or higher | 703 |

## Districts

- [OK-04](/us/states/ok/districts/04.md) — 100% (congressional)
- [OK Senate District 31](/us/states/ok/districts/senate/31.md) — 100% (state senate)
- [OK House District 50](/us/states/ok/districts/house/50.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
