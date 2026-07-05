---
type: Jurisdiction
title: "McDowell County, WV"
classification: county
fips: "54047"
state: "WV"
demographics:
  population: 17943
  population_under_18: 3266
  population_18_64: 10756
  population_65_plus: 3921
  median_household_income: 31559
  poverty_rate: 34.18
  homeownership_rate: 77.27
  unemployment_rate: 8.23
  median_home_value: 50000
  gini_index: 0.4619
  vacancy_rate: 30.73
  race_white: 15784
  race_black: 1611
  race_asian: 9
  race_native: 17
  hispanic: 373
  bachelors_plus: 1216
districts:
  - to: "us/states/wv/districts/01"
    rel: in-district
    area_weight: 0.9991
  - to: "us/states/wv/districts/senate/6"
    rel: in-district
    area_weight: 0.999
  - to: "us/states/wv/districts/house/36"
    rel: in-district
    area_weight: 0.9732
  - to: "us/states/wv/districts/house/34"
    rel: in-district
    area_weight: 0.0258
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# McDowell County, WV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 17943 |
| Under 18 | 3266 |
| 18–64 | 10756 |
| 65+ | 3921 |
| Median household income | 31559 |
| Poverty rate | 34.18 |
| Homeownership rate | 77.27 |
| Unemployment rate | 8.23 |
| Median home value | 50000 |
| Gini index | 0.4619 |
| Vacancy rate | 30.73 |
| White | 15784 |
| Black | 1611 |
| Asian | 9 |
| Native | 17 |
| Hispanic/Latino | 373 |
| Bachelor's or higher | 1216 |

## Districts

- [WV-01](/us/states/wv/districts/01.md) — 100% (congressional)
- [WV Senate District 6](/us/states/wv/districts/senate/6.md) — 100% (state senate)
- [WV House District 36](/us/states/wv/districts/house/36.md) — 97% (state house)
- [WV House District 34](/us/states/wv/districts/house/34.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
