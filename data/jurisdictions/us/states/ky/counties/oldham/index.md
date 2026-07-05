---
type: Jurisdiction
title: "Oldham County, KY"
classification: county
fips: "21185"
state: "KY"
demographics:
  population: 69257
  population_under_18: 17135
  population_18_64: 42026
  population_65_plus: 10096
  median_household_income: 122497
  poverty_rate: 4.3
  homeownership_rate: 87.11
  unemployment_rate: 3.49
  median_home_value: 393100
  gini_index: 0.4503
  vacancy_rate: 3.41
  race_white: 59951
  race_black: 2042
  race_asian: 1162
  race_native: 97
  hispanic: 3466
  bachelors_plus: 30810
districts:
  - to: "us/states/ky/districts/04"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/ky/districts/senate/6"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ky/districts/house/59"
    rel: in-district
    area_weight: 0.8561
  - to: "us/states/ky/districts/house/33"
    rel: in-district
    area_weight: 0.114
  - to: "us/states/ky/districts/house/48"
    rel: in-district
    area_weight: 0.0295
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Oldham County, KY

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 69257 |
| Under 18 | 17135 |
| 18–64 | 42026 |
| 65+ | 10096 |
| Median household income | 122497 |
| Poverty rate | 4.3 |
| Homeownership rate | 87.11 |
| Unemployment rate | 3.49 |
| Median home value | 393100 |
| Gini index | 0.4503 |
| Vacancy rate | 3.41 |
| White | 59951 |
| Black | 2042 |
| Asian | 1162 |
| Native | 97 |
| Hispanic/Latino | 3466 |
| Bachelor's or higher | 30810 |

## Districts

- [KY-04](/us/states/ky/districts/04.md) — 100% (congressional)
- [KY Senate District 6](/us/states/ky/districts/senate/6.md) — 100% (state senate)
- [KY House District 59](/us/states/ky/districts/house/59.md) — 86% (state house)
- [KY House District 33](/us/states/ky/districts/house/33.md) — 11% (state house)
- [KY House District 48](/us/states/ky/districts/house/48.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
