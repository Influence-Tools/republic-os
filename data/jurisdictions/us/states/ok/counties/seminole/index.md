---
type: Jurisdiction
title: "Seminole County, OK"
classification: county
fips: "40133"
state: "OK"
demographics:
  population: 23494
  population_under_18: 5714
  population_18_64: 13455
  population_65_plus: 4325
  median_household_income: 48062
  poverty_rate: 21.74
  homeownership_rate: 70.96
  unemployment_rate: 6.27
  median_home_value: 99500
  gini_index: 0.4492
  vacancy_rate: 18.97
  race_white: 15117
  race_black: 842
  race_asian: 103
  race_native: 4445
  hispanic: 1331
  bachelors_plus: 3253
districts:
  - to: "us/states/ok/districts/05"
    rel: in-district
    area_weight: 0.9953
  - to: "us/states/ok/districts/senate/28"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ok/districts/house/28"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Seminole County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 23494 |
| Under 18 | 5714 |
| 18–64 | 13455 |
| 65+ | 4325 |
| Median household income | 48062 |
| Poverty rate | 21.74 |
| Homeownership rate | 70.96 |
| Unemployment rate | 6.27 |
| Median home value | 99500 |
| Gini index | 0.4492 |
| Vacancy rate | 18.97 |
| White | 15117 |
| Black | 842 |
| Asian | 103 |
| Native | 4445 |
| Hispanic/Latino | 1331 |
| Bachelor's or higher | 3253 |

## Districts

- [OK-05](/us/states/ok/districts/05.md) — 100% (congressional)
- [OK Senate District 28](/us/states/ok/districts/senate/28.md) — 100% (state senate)
- [OK House District 28](/us/states/ok/districts/house/28.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
