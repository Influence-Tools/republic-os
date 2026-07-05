---
type: Jurisdiction
title: "Craig County, OK"
classification: county
fips: "40035"
state: "OK"
demographics:
  population: 14302
  population_under_18: 3253
  population_18_64: 8328
  population_65_plus: 2721
  median_household_income: 51922
  poverty_rate: 19.02
  homeownership_rate: 73.72
  unemployment_rate: 5.13
  median_home_value: 150500
  gini_index: 0.4376
  vacancy_rate: 18.66
  race_white: 8852
  race_black: 479
  race_asian: 232
  race_native: 2815
  hispanic: 566
  bachelors_plus: 1938
districts:
  - to: "us/states/ok/districts/02"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ok/districts/senate/1"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ok/districts/house/7"
    rel: in-district
    area_weight: 0.6774
  - to: "us/states/ok/districts/house/6"
    rel: in-district
    area_weight: 0.3225
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Craig County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14302 |
| Under 18 | 3253 |
| 18–64 | 8328 |
| 65+ | 2721 |
| Median household income | 51922 |
| Poverty rate | 19.02 |
| Homeownership rate | 73.72 |
| Unemployment rate | 5.13 |
| Median home value | 150500 |
| Gini index | 0.4376 |
| Vacancy rate | 18.66 |
| White | 8852 |
| Black | 479 |
| Asian | 232 |
| Native | 2815 |
| Hispanic/Latino | 566 |
| Bachelor's or higher | 1938 |

## Districts

- [OK-02](/us/states/ok/districts/02.md) — 100% (congressional)
- [OK Senate District 1](/us/states/ok/districts/senate/1.md) — 100% (state senate)
- [OK House District 7](/us/states/ok/districts/house/7.md) — 68% (state house)
- [OK House District 6](/us/states/ok/districts/house/6.md) — 32% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
