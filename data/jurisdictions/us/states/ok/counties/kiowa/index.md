---
type: Jurisdiction
title: "Kiowa County, OK"
classification: county
fips: "40075"
state: "OK"
demographics:
  population: 8383
  population_under_18: 2021
  population_18_64: 4658
  population_65_plus: 1704
  median_household_income: 44962
  poverty_rate: 22.94
  homeownership_rate: 69.69
  unemployment_rate: 5.18
  median_home_value: 96100
  gini_index: 0.4548
  vacancy_rate: 26.3
  race_white: 6631
  race_black: 302
  race_asian: 45
  race_native: 344
  hispanic: 1019
  bachelors_plus: 1251
districts:
  - to: "us/states/ok/districts/03"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ok/districts/senate/38"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ok/districts/house/63"
    rel: in-district
    area_weight: 0.5717
  - to: "us/states/ok/districts/house/52"
    rel: in-district
    area_weight: 0.4282
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Kiowa County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8383 |
| Under 18 | 2021 |
| 18–64 | 4658 |
| 65+ | 1704 |
| Median household income | 44962 |
| Poverty rate | 22.94 |
| Homeownership rate | 69.69 |
| Unemployment rate | 5.18 |
| Median home value | 96100 |
| Gini index | 0.4548 |
| Vacancy rate | 26.3 |
| White | 6631 |
| Black | 302 |
| Asian | 45 |
| Native | 344 |
| Hispanic/Latino | 1019 |
| Bachelor's or higher | 1251 |

## Districts

- [OK-03](/us/states/ok/districts/03.md) — 100% (congressional)
- [OK Senate District 38](/us/states/ok/districts/senate/38.md) — 100% (state senate)
- [OK House District 63](/us/states/ok/districts/house/63.md) — 57% (state house)
- [OK House District 52](/us/states/ok/districts/house/52.md) — 43% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
