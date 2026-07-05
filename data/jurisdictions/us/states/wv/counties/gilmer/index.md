---
type: Jurisdiction
title: "Gilmer County, WV"
classification: county
fips: "54021"
state: "WV"
demographics:
  population: 7288
  population_under_18: 1083
  population_18_64: 4877
  population_65_plus: 1328
  median_household_income: 47981
  poverty_rate: 18.99
  homeownership_rate: 75.64
  unemployment_rate: 6.79
  median_home_value: 83800
  gini_index: 0.4339
  vacancy_rate: 27.69
  race_white: 5915
  race_black: 1008
  race_asian: 16
  race_native: 9
  hispanic: 299
  bachelors_plus: 1261
districts:
  - to: "us/states/wv/districts/01"
    rel: in-district
    area_weight: 0.9971
  - to: "us/states/wv/districts/senate/12"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/wv/districts/house/62"
    rel: in-district
    area_weight: 0.6985
  - to: "us/states/wv/districts/house/63"
    rel: in-district
    area_weight: 0.3013
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Gilmer County, WV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7288 |
| Under 18 | 1083 |
| 18–64 | 4877 |
| 65+ | 1328 |
| Median household income | 47981 |
| Poverty rate | 18.99 |
| Homeownership rate | 75.64 |
| Unemployment rate | 6.79 |
| Median home value | 83800 |
| Gini index | 0.4339 |
| Vacancy rate | 27.69 |
| White | 5915 |
| Black | 1008 |
| Asian | 16 |
| Native | 9 |
| Hispanic/Latino | 299 |
| Bachelor's or higher | 1261 |

## Districts

- [WV-01](/us/states/wv/districts/01.md) — 100% (congressional)
- [WV Senate District 12](/us/states/wv/districts/senate/12.md) — 100% (state senate)
- [WV House District 62](/us/states/wv/districts/house/62.md) — 70% (state house)
- [WV House District 63](/us/states/wv/districts/house/63.md) — 30% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
