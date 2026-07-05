---
type: Jurisdiction
title: "Martin County, FL"
classification: county
fips: "12085"
state: "FL"
demographics:
  population: 162176
  population_under_18: 26134
  population_18_64: 83837
  population_65_plus: 52205
  median_household_income: 82943
  poverty_rate: 11.31
  homeownership_rate: 79.64
  unemployment_rate: 4.89
  median_home_value: 432200
  gini_index: 0.5078
  vacancy_rate: 18.43
  race_white: 126895
  race_black: 7761
  race_asian: 2196
  race_native: 616
  hispanic: 25843
  bachelors_plus: 63520
districts:
  - to: "us/states/fl/districts/21"
    rel: in-district
    area_weight: 0.8997
  - to: "us/states/fl/districts/senate/31"
    rel: in-district
    area_weight: 0.8994
  - to: "us/states/fl/districts/house/86"
    rel: in-district
    area_weight: 0.8302
  - to: "us/states/fl/districts/house/85"
    rel: in-district
    area_weight: 0.0692
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, fl]
timestamp: "2026-07-03"
---

# Martin County, FL

County jurisdiction — 38 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 162176 |
| Under 18 | 26134 |
| 18–64 | 83837 |
| 65+ | 52205 |
| Median household income | 82943 |
| Poverty rate | 11.31 |
| Homeownership rate | 79.64 |
| Unemployment rate | 4.89 |
| Median home value | 432200 |
| Gini index | 0.5078 |
| Vacancy rate | 18.43 |
| White | 126895 |
| Black | 7761 |
| Asian | 2196 |
| Native | 616 |
| Hispanic/Latino | 25843 |
| Bachelor's or higher | 63520 |

## Districts

- [FL-21](/us/states/fl/districts/21.md) — 90% (congressional)
- [FL Senate District 31](/us/states/fl/districts/senate/31.md) — 90% (state senate)
- [FL House District 86](/us/states/fl/districts/house/86.md) — 83% (state house)
- [FL House District 85](/us/states/fl/districts/house/85.md) — 7% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
