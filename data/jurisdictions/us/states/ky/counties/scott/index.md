---
type: Jurisdiction
title: "Scott County, KY"
classification: county
fips: "21209"
state: "KY"
demographics:
  population: 59536
  population_under_18: 14479
  population_18_64: 37079
  population_65_plus: 7978
  median_household_income: 85158
  poverty_rate: 10.58
  homeownership_rate: 71.73
  unemployment_rate: 4.3
  median_home_value: 288500
  gini_index: 0.4133
  vacancy_rate: 4.56
  race_white: 51024
  race_black: 2887
  race_asian: 568
  race_native: 153
  hispanic: 3463
  bachelors_plus: 18685
districts:
  - to: "us/states/ky/districts/06"
    rel: in-district
    area_weight: 0.9949
  - to: "us/states/ky/districts/senate/17"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/ky/districts/house/62"
    rel: in-district
    area_weight: 0.8538
  - to: "us/states/ky/districts/house/88"
    rel: in-district
    area_weight: 0.1457
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Scott County, KY

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 59536 |
| Under 18 | 14479 |
| 18–64 | 37079 |
| 65+ | 7978 |
| Median household income | 85158 |
| Poverty rate | 10.58 |
| Homeownership rate | 71.73 |
| Unemployment rate | 4.3 |
| Median home value | 288500 |
| Gini index | 0.4133 |
| Vacancy rate | 4.56 |
| White | 51024 |
| Black | 2887 |
| Asian | 568 |
| Native | 153 |
| Hispanic/Latino | 3463 |
| Bachelor's or higher | 18685 |

## Districts

- [KY-06](/us/states/ky/districts/06.md) — 99% (congressional)
- [KY Senate District 17](/us/states/ky/districts/senate/17.md) — 100% (state senate)
- [KY House District 62](/us/states/ky/districts/house/62.md) — 85% (state house)
- [KY House District 88](/us/states/ky/districts/house/88.md) — 15% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
