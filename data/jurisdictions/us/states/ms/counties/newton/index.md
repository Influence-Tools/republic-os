---
type: Jurisdiction
title: "Newton County, MS"
classification: county
fips: "28101"
state: "MS"
demographics:
  population: 21093
  population_under_18: 5075
  population_18_64: 12380
  population_65_plus: 3638
  median_household_income: 50540
  poverty_rate: 24.68
  homeownership_rate: 79.06
  unemployment_rate: 4.74
  median_home_value: 106300
  gini_index: 0.4948
  vacancy_rate: 15.8
  race_white: 12661
  race_black: 6664
  race_asian: 111
  race_native: 675
  hispanic: 404
  bachelors_plus: 3963
districts:
  - to: "us/states/ms/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ms/districts/senate/31"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ms/districts/house/78"
    rel: in-district
    area_weight: 0.5853
  - to: "us/states/ms/districts/house/84"
    rel: in-district
    area_weight: 0.1794
  - to: "us/states/ms/districts/house/81"
    rel: in-district
    area_weight: 0.1518
  - to: "us/states/ms/districts/house/83"
    rel: in-district
    area_weight: 0.0836
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Newton County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 21093 |
| Under 18 | 5075 |
| 18–64 | 12380 |
| 65+ | 3638 |
| Median household income | 50540 |
| Poverty rate | 24.68 |
| Homeownership rate | 79.06 |
| Unemployment rate | 4.74 |
| Median home value | 106300 |
| Gini index | 0.4948 |
| Vacancy rate | 15.8 |
| White | 12661 |
| Black | 6664 |
| Asian | 111 |
| Native | 675 |
| Hispanic/Latino | 404 |
| Bachelor's or higher | 3963 |

## Districts

- [MS-03](/us/states/ms/districts/03.md) — 100% (congressional)
- [MS Senate District 31](/us/states/ms/districts/senate/31.md) — 100% (state senate)
- [MS House District 78](/us/states/ms/districts/house/78.md) — 59% (state house)
- [MS House District 84](/us/states/ms/districts/house/84.md) — 18% (state house)
- [MS House District 81](/us/states/ms/districts/house/81.md) — 15% (state house)
- [MS House District 83](/us/states/ms/districts/house/83.md) — 8% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
